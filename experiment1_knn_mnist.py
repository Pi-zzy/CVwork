"""
实验一：基于 KNN 算法的手写数字识别
======================================
原理：
1. K 近邻 (KNN) 是一种基于实例的非参数监督学习算法
2. 对未知样本，计算它与所有训练样本的距离 (这里用欧氏距离)
3. 选出距离最近的 K 个邻居
4. 用这 K 个邻居中出现次数最多的类别作为预测结果 (多数投票)

实验步骤：
- 加载 MNIST 数据集
- 自实现 KNN 算法 (向量化欧氏距离 + 排序 + 投票)
- 在 K=1,3,5,7 下分别测试准确率
- 加载用户手写数字图片并预测
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import cv2
from collections import Counter

# Windows 控制台默认 GBK 编码，强制切到 UTF-8 以正常打印中文 / 特殊符号
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

# 设置中文字体，避免 matplotlib 显示中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 工作目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ===================== Windows 中文路径下的安全读写 =====================
def imread_unicode(path, flags=cv2.IMREAD_COLOR):
    """OpenCV 在 Windows 下不支持非 ASCII 路径，用 numpy 中转读取。"""
    data = np.fromfile(path, dtype=np.uint8)
    if data.size == 0:
        return None
    return cv2.imdecode(data, flags)


def imwrite_unicode(path, img):
    """同上，用 imencode + tofile 写出。"""
    ext = os.path.splitext(path)[1]
    ok, buf = cv2.imencode(ext, img)
    if not ok:
        return False
    buf.tofile(path)
    return True


# ===================== 1. 加载 MNIST =====================
def load_mnist(path):
    """加载 MNIST .npz 文件"""
    data = np.load(path)
    x_train, y_train = data['x_train'], data['y_train']
    x_test, y_test = data['x_test'], data['y_test']
    # 展平为 (N, 784) 并归一化到 [0,1]
    x_train = x_train.reshape(len(x_train), -1).astype(np.float32) / 255.0
    x_test = x_test.reshape(len(x_test), -1).astype(np.float32) / 255.0
    return x_train, y_train, x_test, y_test


# ===================== 2. KNN 算法实现 =====================
def euclidean_distances(test_batch, train):
    """
    向量化计算欧氏距离矩阵
    利用公式：||a-b||^2 = ||a||^2 + ||b||^2 - 2 a·b
    test_batch: (M, D), train: (N, D)
    返回: (M, N) 距离矩阵
    """
    test_sq = np.sum(test_batch ** 2, axis=1, keepdims=True)   # (M, 1)
    train_sq = np.sum(train ** 2, axis=1, keepdims=True).T     # (1, N)
    cross = test_batch @ train.T                                # (M, N)
    dist_sq = np.maximum(test_sq + train_sq - 2 * cross, 0)
    return np.sqrt(dist_sq)


def knn_predict(x_train, y_train, x_test, k, batch_size=200):
    """
    KNN 预测：
    1. 分批计算每个测试样本到所有训练样本的欧氏距离
    2. 用 np.argpartition 取出最近的 K 个邻居 (比完全排序快)
    3. 多数投票 (Counter.most_common)
    """
    preds = np.zeros(len(x_test), dtype=np.int64)
    for start in range(0, len(x_test), batch_size):
        end = min(start + batch_size, len(x_test))
        batch = x_test[start:end]
        dists = euclidean_distances(batch, x_train)        # (B, N)
        # 取最近的 K 个邻居下标
        nn_idx = np.argpartition(dists, kth=k, axis=1)[:, :k]
        nn_labels = y_train[nn_idx]                        # (B, K)
        # 投票
        for i in range(end - start):
            preds[start + i] = Counter(nn_labels[i]).most_common(1)[0][0]
    return preds


# ===================== 3. 用户手写数字预处理 =====================
def preprocess_handwritten_image(image_path):
    """
    将一张拍照的数字图片转换为 MNIST 风格 (28x28 灰度)：
    1. 读取并转灰度
    2. 二值化 (THRESH_OTSU + INV，使数字为白色，背景为黑色)
    3. 找到数字轮廓，裁剪
    4. 缩放到 20x20，再放入 28x28 画布，按"质心"对齐到中心
       (与 MNIST 官方一致：MNIST 数字按像素质心居中，而非按外接矩形)
    5. 展平归一化
    """
    img = imread_unicode(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"无法读取图片: {image_path}")

    # 二值化：让笔迹为前景 (白色)，背景为黑色
    _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 找数字所在的矩形 (取所有非零像素的包围框)
    coords = cv2.findNonZero(binary)
    if coords is None:
        return np.zeros(784, dtype=np.float32), np.zeros((28, 28), dtype=np.uint8)
    x, y, w, h = cv2.boundingRect(coords)
    digit = binary[y:y + h, x:x + w]

    # 等比缩放到 20x20
    if h > w:
        new_h = 20
        new_w = max(1, int(round(w * 20.0 / h)))
    else:
        new_w = 20
        new_h = max(1, int(round(h * 20.0 / w)))
    digit_resized = cv2.resize(digit, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # 先把缩放后的数字放入 28x28 画布中心
    canvas = np.zeros((28, 28), dtype=np.uint8)
    sx = (28 - new_w) // 2
    sy = (28 - new_h) // 2
    canvas[sy:sy + new_h, sx:sx + new_w] = digit_resized

    # 再按质心 (center of mass) 微调到画布正中央，与 MNIST 一致
    M = cv2.moments(canvas)
    if M["m00"] > 0:
        cx = M["m10"] / M["m00"]
        cy = M["m01"] / M["m00"]
        shift_x = int(round(14 - cx))
        shift_y = int(round(14 - cy))
        T = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
        canvas = cv2.warpAffine(canvas, T, (28, 28),
                                borderValue=0,
                                flags=cv2.INTER_NEAREST)

    flat = canvas.reshape(-1).astype(np.float32) / 255.0
    return flat, canvas


# ===================== 4. 生成示例手写数字图片 =====================
def make_demo_handwritten_images(x_test, y_test, out_dir, indices=(7, 0, 4)):
    """
    从 MNIST 测试集挑 3 个样本，模拟"手机拍摄的手写数字"：
    - 反色 (白底黑字)
    - 加边距、轻微噪声
    - 放大到约 200x200，保存为 jpg
    """
    paths, labels = [], []
    for k, idx in enumerate(indices):
        sample = (x_test[idx].reshape(28, 28) * 255).astype(np.uint8)
        # 反色：黑字白底
        inv = 255 - sample
        # 加白色边距
        padded = cv2.copyMakeBorder(inv, 30, 30, 30, 30,
                                    cv2.BORDER_CONSTANT, value=255)
        # 放大
        big = cv2.resize(padded, (200, 200), interpolation=cv2.INTER_CUBIC)
        # 加轻微高斯模糊，模拟拍照虚化效果（不加噪声，避免破坏笔画结构）
        big = cv2.GaussianBlur(big, (3, 3), 0)

        out_path = os.path.join(out_dir, f"my_digit_{k + 1}.jpg")
        imwrite_unicode(out_path, big)
        paths.append(out_path)
        labels.append(int(y_test[idx]))
    return paths, labels


# ===================== 5. 主流程 =====================
def main():
    print("=" * 60)
    print("实验一：基于 KNN 的手写数字识别")
    print("=" * 60)

    # 加载数据
    mnist_path = os.path.join(BASE_DIR, "mnist.npz")
    x_train_full, y_train_full, x_test_full, y_test_full = load_mnist(mnist_path)
    print(f"训练集: {x_train_full.shape}, 测试集: {x_test_full.shape}")

    # 为加快实验速度，使用子集 (训练 10000, 测试 1000)
    rng = np.random.RandomState(42)
    train_idx = rng.choice(len(x_train_full), 10000, replace=False)
    test_idx = rng.choice(len(x_test_full), 1000, replace=False)
    x_train = x_train_full[train_idx]
    y_train = y_train_full[train_idx]
    x_test = x_test_full[test_idx]
    y_test = y_test_full[test_idx]
    print(f"实验使用 训练集 {x_train.shape[0]} 条，测试集 {x_test.shape[0]} 条\n")

    # 测试 K=1,3,5,7
    k_values = [1, 3, 5, 7]
    accuracies = {}
    print("【步骤1】不同 K 值下的 MNIST 测试集准确率：")
    print("-" * 40)
    for k in k_values:
        preds = knn_predict(x_train, y_train, x_test, k)
        acc = float(np.mean(preds == y_test))
        accuracies[k] = acc
        print(f"  K = {k} : 准确率 = {acc * 100:.2f} %")
    print()

    # 画准确率折线图
    fig, ax = plt.subplots(figsize=(6, 4))
    ks = list(accuracies.keys())
    vals = [accuracies[k] * 100 for k in ks]

    ax.plot([str(k) for k in ks], vals,
            marker='o', color='#4C72B0', linewidth=2, markersize=7)

    for x, v in zip([str(k) for k in ks], vals):
        ax.text(x, v + 0.05, f"{v:.2f}%", ha='center', fontsize=10)

    ax.set_xlabel("K 值")
    ax.set_ylabel("准确率 (%)")
    ax.set_title("不同 K 值下 KNN 在 MNIST 上的准确率")

    margin = 0.5
    ax.set_ylim(min(vals) - margin, max(vals) + margin)

    plt.tight_layout()
    acc_chart_path = os.path.join(BASE_DIR, "result_knn_accuracy.png")
    plt.savefig(acc_chart_path, dpi=120)
    plt.close()
    print(f"准确率折线图已保存：{acc_chart_path}\n")

    # ---------- 生成 3 张"自己手写"的数字图片 ----------
    print("【步骤2】生成 3 张模拟手写数字图片（白底黑字，模拟拍照效果）...")
    demo_paths, demo_labels = make_demo_handwritten_images(
        x_test_full, y_test_full, BASE_DIR, indices=(1, 8, 61)
    )
    for p, l in zip(demo_paths, demo_labels):
        print(f"  已生成: {os.path.basename(p)}  (真值={l})")
    print()

    # ---------- 用 K=3 识别这 3 张手写数字 ----------
    print("【步骤3】对自定义手写数字进行识别（K=3）：")
    print("-" * 40)
    fig, axes = plt.subplots(2, 3, figsize=(9, 6))
    used_k = 3
    for i, (p, true_label) in enumerate(zip(demo_paths, demo_labels)):
        flat, canvas = preprocess_handwritten_image(p)
        pred = knn_predict(x_train, y_train, flat.reshape(1, -1), used_k)[0]
        ok = "[OK]" if pred == true_label else "[X]"
        print(f"  {os.path.basename(p)}: 真实={true_label}  预测={pred}  {ok}")

        # 上排：原始拍照图
        orig = imread_unicode(p, cv2.IMREAD_GRAYSCALE)
        axes[0, i].imshow(orig, cmap='gray')
        axes[0, i].set_title(f"输入图片\n真值: {true_label}")
        axes[0, i].axis('off')

        # 下排：预处理后的 28x28
        axes[1, i].imshow(canvas, cmap='gray')
        color = 'green' if pred == true_label else 'red'
        axes[1, i].set_title(f"28×28 预处理\nKNN 预测: {pred}", color=color)
        axes[1, i].axis('off')

    plt.suptitle(f"自定义手写数字识别结果 (K={used_k})", fontsize=14)
    plt.tight_layout()
    pred_chart_path = os.path.join(BASE_DIR, "result_knn_handwritten_pred.png")
    plt.savefig(pred_chart_path, dpi=120)
    plt.close()
    print(f"\n手写数字识别结果图已保存：{pred_chart_path}")

    # ---------- 总结 ----------
    print("\n" + "=" * 60)
    print("【实验分析】K 值对分类效果的影响：")
    print("=" * 60)
    print("· K 值过小 (如 K=1)：模型对噪声敏感，单个噪声样本就会改变结果，容易过拟合。")
    print("· K 值过大：邻居中混入太多其他类样本，决策边界过于平滑，导致欠拟合。")
    print("· K 值通常取奇数，避免投票出现平票。")
    print(f"· 本次实验中最佳 K = {max(accuracies, key=accuracies.get)}，"
          f"准确率 {accuracies[max(accuracies, key=accuracies.get)] * 100:.2f}%")


if __name__ == "__main__":
    main()
