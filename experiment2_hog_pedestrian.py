"""
实验二：基于 HOG 特征的行人检测
==================================
原理：
1. HOG (Histogram of Oriented Gradients，方向梯度直方图)
   - 把图像划成若干 cell (通常 8×8 像素)
   - 计算每个 cell 内像素的梯度方向直方图 (一般 9 个 bin)
   - 将相邻 cell 组成 block (通常 2×2 cell)，做 L2 归一化
   - 把所有 block 的特征拼起来，得到对光照、轻微形变鲁棒的特征向量
2. OpenCV 自带一个已经用大量行人样本预训练好的线性 SVM 分类器
   (cv2.HOGDescriptor_getDefaultPeopleDetector)
3. detectMultiScale 用滑动窗口 + 图像金字塔进行多尺度检测，
   返回每个候选框 (x, y, w, h) 和它的置信度

实验步骤：
- 用 OpenCV 读取图片
- 初始化 HOGDescriptor 并加载默认行人 SVM
- detectMultiScale 多尺度检测
- 用 NMS (非极大值抑制) 合并重叠框
- 把结果画到图片上保存
"""

import os
import sys
import cv2
import numpy as np

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_IMAGE = os.path.join(BASE_DIR, "c39963c016ade81a63ce5acc1613b4ec.jpg")
OUTPUT_IMAGE = os.path.join(BASE_DIR, "result_hog_pedestrian.jpg")


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


# ===================== 工具函数：NMS 非极大值抑制 =====================
def non_max_suppression(boxes, weights, overlap_thresh=0.45):
    """
    对 HOG 候选框做 NMS：同一行人常被多个尺度框出，
    用 IoU 阈值合并重叠框，保留置信度最高的那个。
    boxes:   (N, 4)  每行 (x, y, w, h)
    weights: (N,)    每个框的置信度
    return:  保留下来的索引列表
    """
    if len(boxes) == 0:
        return []

    x1 = boxes[:, 0].astype(np.float32)
    y1 = boxes[:, 1].astype(np.float32)
    x2 = x1 + boxes[:, 2]
    y2 = y1 + boxes[:, 3]
    area = (x2 - x1) * (y2 - y1)

    order = np.argsort(weights)[::-1]    # 按置信度从大到小排序
    keep = []
    while len(order) > 0:
        i = order[0]
        keep.append(i)
        # 当前框与剩余所有框的相交区域
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        inter = w * h
        iou = inter / (area[i] + area[order[1:]] - inter + 1e-6)
        # 丢掉与当前框 IoU 太大的框
        order = order[1:][iou < overlap_thresh]
    return keep


# ===================== 主流程 =====================
def main():
    print("=" * 60)
    print("实验二：基于 HOG + SVM 的行人检测")
    print("=" * 60)

    # 1. 读取图片
    img = imread_unicode(INPUT_IMAGE)
    if img is None:
        raise FileNotFoundError(f"找不到图片: {INPUT_IMAGE}")
    print(f"输入图片: {os.path.basename(INPUT_IMAGE)}")
    print(f"图像尺寸 (H×W×C): {img.shape}")

    # 横向放大一些，让小一点的行人也能被检测到
    # HOG 默认窗口 64×128，行人在图中至少要有这个大小
    scale_factor = 1.5
    img_resized = cv2.resize(img, None, fx=scale_factor, fy=scale_factor,
                             interpolation=cv2.INTER_CUBIC)
    print(f"放大后尺寸 (H×W×C): {img_resized.shape}")

    # 2. 初始化 HOG 行人检测器
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    print("HOG 描述子已初始化，已加载 OpenCV 默认行人 SVM")

    # 3. 多尺度检测
    # winStride: 滑动窗口步长 (越小越精细，越慢)
    # padding:   窗口外补零像素，提升边界检测效果
    # scale:     图像金字塔每层缩放比例
    # hitThreshold: SVM 分类阈值，越大越严格
    rects, weights = hog.detectMultiScale(
        img_resized,
        winStride=(4, 4),
        padding=(8, 8),
        scale=1.05,
        hitThreshold=0.0,
    )
    print(f"原始候选框数量: {len(rects)}")

    # 4. NMS 合并重叠框
    if len(rects) > 0:
        weights_flat = np.array(weights).flatten()
        keep = non_max_suppression(rects, weights_flat, overlap_thresh=0.45)
        rects = rects[keep]
        weights_flat = weights_flat[keep]
        print(f"NMS 之后保留: {len(rects)} 个行人框")
    else:
        weights_flat = np.array([])
        print("未检测到行人")

    # 5. 把检测框还原回原图尺寸并绘制
    output = img.copy()
    for (x, y, w, h), score in zip(rects, weights_flat):
        x0 = int(x / scale_factor)
        y0 = int(y / scale_factor)
        x1 = int((x + w) / scale_factor)
        y1 = int((y + h) / scale_factor)
        # 绿色矩形框
        cv2.rectangle(output, (x0, y0), (x1, y1), (0, 255, 0), 2)
        # 置信度文字标签
        label = f"person {float(score):.2f}"
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(output, (x0, y0 - th - 6), (x0 + tw + 4, y0),
                      (0, 255, 0), -1)
        cv2.putText(output, label, (x0 + 2, y0 - 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # 6. 在图片左上角画总人数
    summary = f"Detected: {len(rects)} pedestrian(s)"
    cv2.rectangle(output, (5, 5), (5 + 280, 35), (0, 0, 0), -1)
    cv2.putText(output, summary, (10, 28),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

    # 7. 保存结果
    imwrite_unicode(OUTPUT_IMAGE, output)
    print(f"\n检测结果图已保存：{OUTPUT_IMAGE}")

    # 控制台输出每个框的位置和置信度
    if len(rects) > 0:
        print("\n检测到的行人列表 (原图坐标系)：")
        print("-" * 50)
        print(f"{'编号':<6}{'x':>6}{'y':>6}{'w':>6}{'h':>6}{'置信度':>10}")
        for i, ((x, y, w, h), s) in enumerate(zip(rects, weights_flat), 1):
            print(f"{i:<6}"
                  f"{int(x/scale_factor):>6}"
                  f"{int(y/scale_factor):>6}"
                  f"{int(w/scale_factor):>6}"
                  f"{int(h/scale_factor):>6}"
                  f"{float(s):>10.3f}")

    # 8. 简要分析
    print("\n" + "=" * 60)
    print("【实验分析】")
    print("=" * 60)
    print("· HOG + SVM 是经典的行人检测方法，对正面/侧面、直立行人效果好。")
    print("· detectMultiScale 通过图像金字塔检测不同大小的行人；")
    print("  winStride 越小越精细但更慢，scale 越接近 1 检测越密但更慢。")
    print("· hitThreshold (SVM 阈值) 越大越严，可减少误检但会漏检。")
    print("· 同一个行人常被多个尺度框中，需要用 NMS 合并重叠框。")
    print("· 缺点：对人体被严重遮挡、躯干部分被裁掉、姿态特殊 (蹲/坐) 时易漏检。")


if __name__ == "__main__":
    main()
