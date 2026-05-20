# J2EE 框架设计和项目开发 · 期末复习手册


## 0. 考试题型与分值

| 题型 | 数量 | 单题分 | 总分 |
|---|---|---|---|
| 选择题 | 20 | 1 | 20 |
| 判断题 | 10 | 1 | 10 |
| 简答题 | 8 | 5 | 40 |
| 编程大题 | 若干（前端 HTML 表单 + SQL + 三层架构 + JDBC） | — | 30 |
| **合计** | — | — | **100** |

**时间分配建议**（120 分钟）：
- 选择 + 判断：25 分钟
- 简答：35 分钟（每题 4~5 分钟，分项给点不要写大段散文）
- 编程：50 分钟（HTML 15 + SQL 15 + 三层架构 10 + JDBC 10）
- 检查 10 分钟（代码语法、缺标签、SQL 缺分号、JDBC 资源释放）

**编程题写答策略**：
- HTML 表单：`name`、`type`、`value`、`action`、`method` 都写齐
- SQL：每条 SQL 后跟分号、字符串用单引号、模糊查询 `%` 别忘
- 三层架构：每个类前面注解（`@RestController` / `@Service` / `@Repository` / `@Autowired`）必须正确
- JDBC：六步骤一个不能漏（注册驱动 → 获取连接 → 预编译 → 绑参 → 执行 → 处理结果集 → 关闭资源）

---

# 第一部分 · 知识点速查

## CH1 HTML+CSS 知识点

### 一、Web 基础与前端开发

- **Web 标准**：不同浏览器对同一份代码要呈现一致效果，必须遵循统一标准。Web 标准由三部分组成：**结构（HTML）+ 表现（CSS）+ 行为（JavaScript）**。
- **三者分工**：HTML 只负责页面结构（骨架）；CSS 负责样式（皮肤），如颜色、字体、布局；JS 负责动作效果（轮播、子菜单等动态交互）。
- **B/S vs C/S**：
  - C/S（Client/Server）：需要安装客户端，跨平台差、维护成本高（如 QQ 客户端）。
  - B/S（Browser/Server）：浏览器即客户端，无需安装、跨平台、易升级，本课程开发模式就是 B/S。
- **静态网站 vs 动态网站**：静态网站内容固定（纯 HTML/CSS/JS），所有用户看到的页面一样；动态网站内容由服务端生成（JSP/Servlet 等），可根据用户、数据库实时变化。

### 二、HTML 快速入门

- **基本结构**：`<!DOCTYPE html>` 声明、`<html>` 根、`<head>` 头部（含 `<title>`、`<meta charset="UTF-8">`）、`<body>` 主体。
- **常见标题与排版标签**：
  - 标题：`<h1>`～`<h6>`，**没有 h7**，HTML 标签是规范定义的，不能自己造。
  - 段落 `<p>`：两个 p 之间自动换行，不用再加 `<br>`。
  - 换行 `<br>`、水平线 `<hr>`、加粗 `<b>`（无语义）/ `<strong>`（强调语义，表格里推荐）、超链接 `<a href="...">`。
- **多媒体**：
  - `<img src="..." alt="..." width="..." />`：宽高只设一个会等比缩放。
  - `<audio src="..." controls>` 音频；`<video src="..." controls autoplay width="80%">` 视频。
- **路径**：`./` 当前目录、`../` 上级目录。
- **转义字符**：空格 `&nbsp;`、`<` 写成 `&lt;`、`>` 写成 `&gt;`。但首行缩进**专业写法用 CSS 的 `text-indent`**。

### 三、CSS 选择器与样式

- **三种引入方式**：① 行内式 `style="..."`；② 内嵌式 `<style>` 写在 head；③ 外部式 `<link rel="stylesheet" href="xx.css">`，**外部式最推荐**。
- **三类选择器**（必考优先级）：
  - 元素选择器：`span { }`，范围太广。
  - 类选择器：`.cls { }`，**强调复用**。
  - ID 选择器：`#time { }`，**强调唯一**。
  - 优先级：**ID > 类 > 元素**。
- **颜色表示法**：`red` 关键字、`#FF0000` 十六进制、`rgb(255,0,0)`、`rgba(255,0,0,0.5)`（a 是透明度，0 全透，1 不透）。
- **常用属性**：`color`（字体颜色）、`font-size`、`font-weight`、`line-height`（行高）、`text-indent`（首行缩进）、`text-decoration: none`（去掉超链接下划线）、`text-align`。

### 四、盒子模型（重点）

- 组成：**content（内容） → padding（内边距） → border（边框） → margin（外边距）**。
- 简写顺序：**顺时针 上、右、下、左**。
  - `padding: 20px 20px 20px 20px;`：四个方向全 20px。
  - `padding: 20px 10px;`：上下 20，左右 10。
  - `padding: 20px;`：四个方向全 20。
- `box-sizing`：默认 `content-box`，width/height 只算 content，加 border 后盒子会撑大；设 `border-box` 则 width/height 包含 border。
- **盒子居中**：`margin: 30px auto;`。
- **块级 vs 行内**：
  - `<div>` 独占一行，可设 width/height。
  - `<span>` 一行可显示多个，不能设宽高。

### 五、Flex 弹性布局

- 父容器加 `display: flex` 变成 Flex 容器。
- **对齐属性写在父容器上**（container）。
- `flex-direction: row` 横向；`column` 纵向。
- `justify-content`（主轴对齐）、`align-items`（交叉轴对齐）。

### 六、表单（编程大题必考）

- `<form action="提交地址" method="get/post">`：
  - **GET**：参数拼在 URL 后，明文、长度受限、不安全，适合查询。
  - **POST**：参数在请求体，相对安全、无长度限制，适合提交敏感数据。
- **表单项必须设 `name` 属性**，否则提交时这一项数据不会上传到服务端。
- **四大表单标签 ITSB**：`<input>`、`<textarea>`、`<select>`、`<button>`。
- **三种按钮**：`submit`（提交）、`reset`（重置）、`button`（普通按钮，需配 JS）。
- `<input type="hidden">` 隐藏域：页面不显示但随表单提交。
- `<label for="id">`：扩大可点击区域，点击文字也能选中关联控件。

### 七、表格

- `<table>` → `<thead>`（`<tr>` + `<th>`） → `<tbody>`（`<tr>` + `<td>`）。
- `<th>` 是标题单元格（默认加粗居中），`<td>` 是普通单元格。

### 八、易混淆点（学生最常翻车）

| 混淆点 | 正确说法 |
|---|---|
| `<img>` 的 `align` vs `valign` | `align` 是 HTML4 老属性管水平对齐，`valign` 管垂直对齐（表格里用）；新写法统一用 CSS 的 `text-align` 和 `vertical-align`。 |
| 列表嵌套 | `<ul>`/`<ol>` 里面**只能直接放 `<li>`**，要嵌套子列表必须再写一层 `<ul>` 放到 `<li>` 里面，不能 `<ul>` 直接套 `<ul>`。 |
| `<b>` vs `<strong>` | 视觉都加粗。`<b>` 没语义；`<strong>` 有"强调"语义。 |
| 首行缩进 | 用 CSS 的 `text-indent: 2em`，不要堆 `&nbsp;`。 |
| 类 vs ID 选择器 | 类（`.cls`）可重复用；ID（`#xx`）一页只能用一次。 |
| `box-sizing` 默认 | 默认 `content-box`，加 border 盒子变大；`border-box` 总大小不变。 |


---


### 课件代码示例（HTML+CSS）

> 下面这些代码示例对应老师 PPT 里的截图，对着看更好理解。

#### 1. HTML 基础结构

VSCode 里输入 `!` + Tab 自动生成的最小模板。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

</body>
</html>
```

要点：`<!DOCTYPE html>` 声明 HTML5；`lang="en"` 改成 `zh-CN` 也行；`<meta charset>` 不写中文会乱码。

#### 2. 常见标签示例

标题、段落、换行、分割线、加粗、超链接、图片、音视频一锅端。

```html
<!-- 一到六级标题，没有 h7 -->
<h1>一级标题</h1>
<h2>二级标题</h2>
<h6>六级标题</h6>

<!-- 段落，两个 p 之间自动换行 -->
<p>这是一个段落。</p>

<!-- 换行和水平线 -->
第一行<br>第二行
<hr>

<!-- 加粗：b 没语义，strong 有强调语义 -->
<b>粗体</b>
<strong>强调</strong>

<!-- 超链接：target=_blank 新窗口打开 -->
<a href="https://news.cctv.com" target="_blank">央视网</a>

<!-- 图片：只设一个宽高，另一个等比缩放；alt 是加载失败时的替代文字 -->
<img src="img/1.gif" alt="图片描述" width="80%">

<!-- 音频和视频：controls 显示控件，autoplay 自动播放 -->
<audio src="audio/news.mp3" controls></audio>
<video src="video/news.mp4" controls autoplay width="80%"></video>

<!-- 特殊字符：空格用 &nbsp;，小于号 &lt;，大于号 &gt; -->
&nbsp;&nbsp;首行缩进两个字
```

#### 3. CSS 三种引入方式

```html
<!-- 1. 行内式：直接写在标签的 style 属性里 -->
<h1 style="color: red;">标题</h1>

<!-- 2. 内嵌式：写在 head 里的 style 标签 -->
<head>
    <style>
        h1 { color: red; }
    </style>
</head>

<!-- 3. 外部式：用 link 引入单独的 css 文件（推荐，结构和样式分离） -->
<head>
    <link rel="stylesheet" href="css/news.css">
</head>
```

优先级：行内 > 内嵌 ≈ 外部（同级别看出现顺序）。

#### 4. CSS 选择器示例

```html
<style>
    /* 元素选择器：选所有 span，范围太广 */
    span { color: gray; }

    /* 类选择器：. 开头，强调复用性 */
    .cls { color: blue; }

    /* ID 选择器：# 开头，强调唯一性 */
    #time { color: red; }

    /* 优先级：ID > 类 > 元素 */
</style>

<span>普通 span</span>
<span class="cls">类选择器</span>
<span id="time" class="cls">2024年05月15日 20:07</span>

<!-- 经典用法：去掉超链接下划线 -->
<style>
    a { text-decoration: none; }
</style>
```

#### 5. 颜色表示法（CSS）

```css
color: red;                     /* 关键字 */
color: #FF0000;                 /* 十六进制 */
color: rgb(255, 0, 0);          /* RGB */
color: rgba(255, 0, 0, 0.5);    /* RGBA，第四个值是透明度 0~1 */
```

#### 6. 盒子模型示例

content（内容） + padding（内边距） + border（边框） + margin（外边距）。

```html
<style>
    .box {
        width: 400px;
        height: 300px;
        padding: 20px;          /* 四个方向都 20px */
        border: 10px solid #333;
        margin: 30px auto;      /* 上下 30px，左右 auto 实现水平居中 */
        background: #f0f0f0;
        /* 默认 content-box：width/height 只算 content；
           border-box：width/height 包含 padding 和 border */
        box-sizing: border-box;
    }
</style>

<div class="box">我是一个盒子</div>
```

padding/margin 简写规则：
- `padding: 20px;` 四个方向都 20px
- `padding: 20px 10px;` 上下 20，左右 10
- `padding: 20px 20px 20px 20px;` 顺时针 上、右、下、左

#### 7. Flex 布局示例

```html
<style>
    .container {
        display: flex;
        flex-direction: row;             /* row 横向（默认），column 纵向 */
        justify-content: space-between;  /* 主轴对齐：flex-start / center / space-around */
        align-items: center;             /* 交叉轴对齐 */
        height: 80px;
        background: #1e90ff;
    }
    .item {
        width: 100px;
        height: 50px;
        background: #fff;
    }
</style>

<div class="container">
    <div class="item">首页</div>
    <div class="item">攻略</div>
    <div class="item">视频</div>
</div>
```

记忆点：对齐属性写在 container 上，不要写在 item 上。

#### 8. 表单完整示例

```html
<!-- action 提交地址，method 提交方式：get 参数拼 URL，post 放请求体 -->
<form action="/register" method="post">
    <!-- 表单项必须有 name 属性才能提交 -->
    用户名：<input type="text" name="username" placeholder="请输入用户名"><br>
    密  码：<input type="password" name="password"><br>

    <!-- 单选：同组的 name 必须一致 -->
    性别：
    <input type="radio" name="gender" value="1" id="male">
    <label for="male">男</label>
    <input type="radio" name="gender" value="2" id="female">
    <label for="female">女</label><br>

    <!-- 复选 -->
    爱好：
    <input type="checkbox" name="hobby" value="java">Java
    <input type="checkbox" name="hobby" value="web">Web<br>

    <!-- 文件、日期、邮箱、数字 -->
    头像：<input type="file" name="avatar"><br>
    生日：<input type="date" name="birthday"><br>
    邮箱：<input type="email" name="email"><br>
    年龄：<input type="number" name="age"><br>

    <!-- 隐藏域：页面不显示，但会随表单提交 -->
    <input type="hidden" name="id" value="100">

    <!-- 下拉框 -->
    学历：
    <select name="degree">
        <option value="">---请选择---</option>
        <option value="1">大专</option>
        <option value="2">本科</option>
        <option value="3">硕士</option>
    </select><br>

    <!-- 多行文本 -->
    描述：<textarea name="desc" rows="5" cols="30"></textarea><br>

    <!-- 三种按钮：submit 提交、reset 重置、button 普通按钮 -->
    <button type="submit">提交</button>
    <button type="reset">重置</button>
</form>
```

考点：① 表单项必须有 `name` 才能提交；② `<label for="id">` 关联 input，点文字也能选中；③ get 和 post 的区别。

#### 9. 表格示例

```html
<table border="1" cellspacing="0" width="600">
    <caption>员工信息表</caption>

    <!-- thead 表头，th 是标题单元格，自动加粗居中 -->
    <thead>
        <tr>
            <th>编号</th>
            <th>姓名</th>
            <th>性别</th>
            <th>部门</th>
        </tr>
    </thead>

    <!-- tbody 主体，td 是普通单元格 -->
    <tbody>
        <tr>
            <td>1</td>
            <td>张三</td>
            <td>男</td>
            <td rowspan="2">研发部</td>   <!-- 跨 2 行 -->
        </tr>
        <tr>
            <td>2</td>
            <td>李四</td>
            <td>男</td>
        </tr>
        <tr>
            <td colspan="3">合计</td>     <!-- 跨 3 列 -->
            <td>2 人</td>
        </tr>
    </tbody>
</table>
```

#### 10. 超链接和路径

```html
<!-- 外部链接 -->
<a href="https://www.baidu.com">百度</a>

<!-- 新窗口打开 -->
<a href="https://www.baidu.com" target="_blank">新窗口打开</a>

<!-- 页内锚点：跳到 id=top 的元素 -->
<a href="#top">回到顶部</a>

<!-- 邮件链接 -->
<a href="mailto:abc@163.com">联系我</a>

<!-- 路径写法（重点） -->
<img src="img/1.jpg">       <!-- 相对路径：当前目录下的 img 文件夹 -->
<img src="./img/1.jpg">     <!-- ./ 当前目录，等价于上一句 -->
<img src="../img/1.jpg">    <!-- ../ 上一级目录 -->
<img src="/img/1.jpg">      <!-- 绝对路径：从网站根开始 -->
```

#### 11. 文字常用 CSS 属性

```css
.title {
    font-size: 32px;
    font-weight: bold;          /* 加粗，也可用 700 */
    font-family: "微软雅黑", sans-serif;
    color: #333;
    text-align: center;         /* 水平居中 */
}

.content {
    text-indent: 2em;           /* 首行缩进两个字符（专业做法，不要用 &nbsp;）*/
    line-height: 1.8;           /* 行高 */
    letter-spacing: 1px;        /* 字间距 */
}
```

#### 12. 顶部导航栏（Tlias 案例片段）

```html
<style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 60px;
        background: #1e90ff;
        padding: 0 30px;
        color: #fff;
    }
    .header a {
        color: #fff;
        margin: 0 15px;
        text-decoration: none;
    }
</style>

<div class="header">
    <div class="logo">Tlias 智能学习辅助系统</div>
    <div class="nav">
        <a href="#">首页</a>
        <a href="#">员工管理</a>
        <a href="#">班级管理</a>
        <a href="#">退出</a>
    </div>
</div>
```

---

记忆口诀：
- 表单项四大件 **ITSB**：`input` / `textarea` / `select` / `button`
- 盒子四层：content → padding → border → margin
- 选择器优先级：ID > 类 > 元素
- flex 对齐属性只能放在 container 上，不能放在 item 上

---

## CH2 JavaScript 知识点

### 一、JS 是什么

JavaScript（简称 JS）是一门**跨平台、面向对象的脚本语言**，运行在**客户端浏览器**里，用来给网页加交互行为。HTML 管结构、CSS 管表现、JS 管动作。

要点：
- **脚本语言**，动态执行、不需要编译，浏览器直接解析。
- **弱类型**：变量类型由值决定，可随时改变。
- 和 Java 没关系，只是基础语法长得像。

### 二、引入方式

三种写法：① 行内（写在标签 `onclick` 等属性里）；② 内嵌（`<script>` 写在 HTML 里）；③ 外部（`<script src="xxx.js"></script>`）。

**`<script>` 建议放 `<body>` 底部**，两个原因：
- JS 解析要时间，放头部会阻塞 HTML 渲染。
- JS 经常要操作 DOM，HTML 还没渲染完就执行会拿不到节点、报错。

### 三、变量声明

| 关键字 | 作用域 | 能否重复声明 | 能否修改 |
|---|---|---|---|
| `var` | 函数级/全局 | 可以，后面覆盖前面 | 可以 |
| `let` | 块级 `{}` | 不能 | 可以 |
| `const` | 块级 | 不能 | 不能（常量） |

`var` 是历史包袱，**实际开发推荐 `let` / `const`**。

### 四、数据类型

- **原始类型 5 种**：`number`、`string`、`boolean`、`null`、`undefined`。
- **引用类型**：对象、数组、函数。
- 用 `typeof` 查类型。坑点：`typeof null` 返回 `"object"`。

### 五、运算符与流程控制

- 等号有两种：`==` 只比值（会自动类型转换），`===` 同时比值和类型，**项目里建议用 `===`**。
- 流程控制 `if / else / switch / for / while / do-while`，写法和 Java 一样。

### 六、函数

```javascript
// 1. function 关键字
function add(a, b) { return a + b; }
// 2. 变量式（匿名函数）
var add = function(a, b) { return a + b; }
```

参数不用写类型、不用写返回值类型。

### 七、JS 对象

**Array 数组**：长度可变、类型可混。

```javascript
var arr = [1, "abc", true];
arr.length;          // 长度
arr.push(99);        // 末尾追加
arr.slice(1, 3);     // 截取，不改原数组
for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
```

**String**：`length`、`charAt()`、`indexOf()`、`split()`、`substring()`、`trim()`。

**JSON 对象**：本质是**字符串**，key 必须用双引号包住。
- `JSON.stringify(obj)`：JS 对象 → JSON 字符串。
- `JSON.parse(str)`：JSON 字符串 → JS 对象。

**BOM（Browser Object Model）**：浏览器对象模型。
- `window`：`alert()`、`confirm()`（有确定/取消，返回布尔值）、`prompt()`、`setTimeout()` / `setInterval()`。
- `location`：`location.href` 读取或跳转 URL。
- `history`：`back()` / `forward()`。
- `navigator`：浏览器信息。

**DOM（Document Object Model）**：把 HTML 解析成树形结构。`document` 是入口。

查找节点的几种方法：
- `document.getElementById("id")` ——按 id 查，返回单个 Element。
- `document.getElementsByTagName("p")` ——按标签名，返回数组。
- `document.getElementsByName("xxx")` ——按 name 属性，返回数组。
- `document.getElementsByClassName("cls")` ——按 class，返回数组。
- `document.querySelector("#id .cls")` ——CSS 选择器，返回第一个匹配。
- `document.querySelectorAll("...")` ——CSS 选择器，返回所有匹配。

改内容/样式：`element.innerHTML = "新内容"`、`element.style.color = "red"`。

### 八、事件监听

常见事件：
- `onclick` 单击、`ondblclick` 双击
- `onfocus` 获得焦点、`onblur` 失去焦点
- `onchange` 内容改变、`onsubmit` 表单提交
- `onmouseover` / `onmouseout` 鼠标移入移出
- `onload` 页面加载完成、`onkeydown` 按键

绑定方式：① HTML 内联 `<button onclick="fn()">`；② JS 赋值 `btn.onclick = function(){}`；③ `addEventListener("click", fn)`，**推荐第三种**。


---

## CH2 Vue3 基础知识点

### 什么是 Vue（MVVM 思想）

Vue 是一套**渐进式**的 JavaScript 框架，定位是「构建用户界面」。核心思路就是**数据驱动视图**：后端返回的 JSON 原始数据用户看不懂，开发者用 Vue 把数据遍历、解析、渲染成用户能看懂的页面。MVVM 思想——Model（data 里的数据）和 View（HTML 模板）之间靠 ViewModel（Vue 实例）双向绑定，数据变 → 视图自动变，输入框变 → 数据自动变，不用再手写 `document.getElementById` 去操作 DOM。

### Vue 的引入方式

- **CDN / ES 模块**：`<script type="module">` 里 `import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'`。注意一定要 `type="module"`。
- **离线**：把 vue.esm-browser.js 下到本地引入。
- **npm 工程化**：`npm install vue`，配合 Vite/Webpack。

### 快速入门三件套

1. `createApp({...})`：传入配置对象，返回应用实例。
2. `data() { return {...} }`：data 必须是函数，return 的对象就是响应式数据。
3. `.mount('#app')`：挂载到 id 为 app 的 div 上，**超出范围 Vue 管不到**。
4. 文本插值 `{{ 变量名 }}`：变量必须在 data 里定义过。

### 常用指令

| 指令 | 简写 | 作用 |
|---|---|---|
| `v-bind:href` | `:href` | **单向**绑定属性值（数据 → 视图） |
| `v-on:click` | `@click` | 绑定事件，对应 methods 里的方法 |
| `v-if` | — | 条件渲染，**不满足时元素根本不渲染到 DOM** |
| `v-show` | — | 条件渲染，**元素一直在 DOM 里，靠 `display:none` 切换** |
| `v-for` | — | 列表循环，写法 `v-for="(item, index) in list" :key="item.id"` |
| `v-model` | — | 表单**双向**数据绑定 |

### 几个考点对比

- **v-if vs v-show**：v-if 增删 DOM 节点，适合**条件很少变**的场景；v-show 一直在 DOM 里，靠 display 切换，适合**频繁切换**。
- **v-bind vs v-model**：v-bind 单向；v-model 双向，常用于 `<input>` `<select>` `<textarea>`，本质是 `:value` + `@input` 的语法糖。
- **v-for 配 key**：每个循环项要加 `:key`，Vue 用 key 做 diff 复用 DOM 节点，**用 id 这种唯一值，不要用 index**。

### Vue 生命周期

8 个钩子，重点记 `mounted`——**挂载完成，HTML 页面渲染成功**，一般在这里发 Ajax 请求拉后台数据。其他像 `beforeCreate`、`created`、`beforeMount`、`beforeUpdate`、`updated`、`beforeUnmount`、`unmounted` 了解即可。

### Axios 异步请求

```js
axios.get('https://web-server.itheima.net/emps/list?name=张三')
  .then(result => { console.log(result.data) })
  .catch(err => { console.log(err) })
```

要点：
- `.get(url)` / `.post(url, data)`。
- `.then(res => res.data)` 拿到响应体。
- **异步**：`console.log` 在 `axios.get` 之后写会先打印，再打印回调里的数据。
- 复杂回调可以用 `async / await` 改写。

### 完整最小示例（v-for + Axios + mounted）

```html
<div id="app">
  <table border="1">
    <tr><th>编号</th><th>姓名</th><th>性别</th></tr>
    <tr v-for="(emp, index) in empList" :key="emp.id">
      <td>{{ index + 1 }}</td>
      <td>{{ emp.name }}</td>
      <td>{{ emp.gender === 1 ? '男' : '女' }}</td>
    </tr>
  </table>
</div>

<script type="module">
import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
createApp({
  data() {
    return { empList: [] }
  },
  async mounted() {
    const res = await axios.get('https://web-server.itheima.net/emps/list')
    this.empList = res.data.data
  }
}).mount('#app')
</script>
```

页面挂载完 → 自动发 Axios 请求 → 拿到员工数组赋给 `empList` → `v-for` 自动渲染表格。


---


### 课件代码示例（JS + Vue3）

> 下面这些代码示例对应老师 PPT 里的截图，对着看更好理解。

#### 一、JavaScript 部分

##### 1. JS 三种引入方式

```html
<!-- 1. 内嵌式：写在 script 标签里 -->
<script>
    alert("Hello JS");
</script>

<!-- 2. 外链式：单独 .js 文件，src 引入 -->
<script src="js/news.js"></script>

<!-- 3. 行内式（不推荐）：直接写在 HTML 元素的事件属性里 -->
<button onclick="alert('点击了按钮')">点我</button>
```

注意：`<script>` 一般放在 `<body>` 最后或 `<head>` 中。外链 `<script src="...">` 标签**不能自闭合**，必须写完整闭合标签。

##### 2. 变量声明（var / let / const）

```js
// var：ES5 写法，作用域是函数级，可重复声明
var name = "张三";
var name = "李四";   // 不报错，被覆盖

// let：ES6 写法，作用域是块级（{}），不能重复声明（推荐）
let age = 18;
// let age = 20;  // 报错：Identifier 'age' has already been declared

// const：常量，一旦赋值不能改
const PI = 3.14;
// PI = 3.15;  // 报错

// JS 是弱类型，变量类型由值决定且可变
let x = 10;        // number
x = "hello";       // 现在变成 string
x = true;          // 又变成 boolean
```

##### 3. 数据类型 + typeof

```js
let n = 100;
let s = "hello";
let b = true;
let u;             // undefined
let nl = null;
let arr = [1, 2, 3];
let obj = {name: "张三"};

console.log(typeof n);    // "number"
console.log(typeof s);    // "string"
console.log(typeof b);    // "boolean"
console.log(typeof u);    // "undefined"
console.log(typeof nl);   // "object"（历史遗留 bug）
console.log(typeof arr);  // "object"
console.log(typeof obj);  // "object"
```

##### 4. 运算符与流程控制

```js
// == vs ===：== 只看值，=== 既看值又看类型
console.log(1 == "1");    // true
console.log(1 === "1");   // false

// if-else
let score = 85;
if (score >= 90) {
    console.log("优秀");
} else if (score >= 60) {
    console.log("及格");
} else {
    console.log("不及格");
}

// for 循环
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// while 循环
let n = 0;
while (n < 3) {
    console.log(n);
    n++;
}

// for...of 遍历数组
let arr = [10, 20, 30];
for (let v of arr) {
    console.log(v);
}
```

##### 5. 函数三种写法

```js
// 1. function 关键字声明
function add(a, b) {
    return a + b;
}

// 2. 变量式（匿名函数赋给变量）
var add2 = function(a, b) {
    return a + b;
};

// 3. 箭头函数（ES6，最简洁）
var add3 = (a, b) => a + b;

// 调用方式都一样
console.log(add(1, 2));    // 3
console.log(add2(3, 4));   // 7
console.log(add3(5, 6));   // 11
```

##### 6. JS 对象

#### 6.1 对象字面量

```js
let user = {
    name: "张三",
    age: 18,
    sayHi: function() {
        console.log("Hi, " + this.name);
    }
};

console.log(user.name);    // 张三
user.sayHi();              // Hi, 张三
```

#### 6.2 Array 数组

```js
// 三种创建方式
let arr1 = [1, 2, 3];
let arr2 = new Array(1, 2, 3);
let arr3 = new Array(5);   // 长度 5 的空数组

// 常用方法
arr1.push(4);              // 末尾添加：[1,2,3,4]
arr1.pop();                // 删除末尾：[1,2,3]
arr1.unshift(0);           // 开头添加：[0,1,2,3]
arr1.shift();              // 删除开头：[1,2,3]
arr1.length;               // 长度 3

// 遍历
arr1.forEach(v => console.log(v));
```

#### 6.3 String 字符串

```js
let s = "Hello World";
s.length;              // 11
s.toUpperCase();       // "HELLO WORLD"
s.toLowerCase();       // "hello world"
s.indexOf("World");    // 6
s.substring(0, 5);     // "Hello"
s.split(" ");          // ["Hello", "World"]
s.trim();              // 去掉两端空格
```

#### 6.4 JSON

```js
// JS 对象 → JSON 字符串
let user = {name: "张三", age: 18};
let jsonStr = JSON.stringify(user);
console.log(jsonStr);   // {"name":"张三","age":18}

// JSON 字符串 → JS 对象
let obj = JSON.parse(jsonStr);
console.log(obj.name);  // 张三
```

##### 7. DOM 操作

```html
<div id="time">时间</div>
<div class="news">新闻1</div>
<div class="news">新闻2</div>
<input type="text" name="username">
```

```js
// 1. getElementById：按 ID 取，返回单个元素
let timeDiv = document.getElementById("time");
timeDiv.innerHTML = "2024-05-20 10:30";

// 2. getElementsByClassName：按类取，返回 HTMLCollection
let newsList = document.getElementsByClassName("news");
console.log(newsList.length);  // 2
newsList[0].innerHTML = "改后的新闻1";

// 3. getElementsByTagName：按标签名取
let divs = document.getElementsByTagName("div");

// 4. getElementsByName：按 name 属性取
let inputs = document.getElementsByName("username");

// 5. querySelector：按 CSS 选择器取第一个
let firstNews = document.querySelector(".news");

// 6. querySelectorAll：按 CSS 选择器取全部
let allNews = document.querySelectorAll(".news");
```

##### 8. 事件监听

```html
<button id="btn1" onclick="alert('方式1')">方式1</button>
<button id="btn2">方式2</button>
<button id="btn3">方式3</button>
```

```js
// 方式1：HTML 属性（不推荐，混了结构和行为）

// 方式2：DOM 属性赋值
document.getElementById("btn2").onclick = function() {
    alert("方式2");
};

// 方式3：addEventListener（推荐，可以注册多个）
document.getElementById("btn3").addEventListener("click", function() {
    alert("方式3");
});

// 常见事件
// onclick 点击 / onmouseover 鼠标进入 / onmouseout 鼠标离开
// onchange 值改变 / onkeydown 按键按下 / onload 加载完成
window.onload = function() {
    console.log("页面加载完毕");
};
```

---

#### 二、Vue3 部分

##### 9. Vue 引入和创建实例

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Vue3 入门</title>
</head>
<body>
    <!-- 1. 准备 Vue 接管的 DOM 容器 -->
    <div id="app">
        {{ message }}
    </div>

    <!-- 2. 引入 Vue3（必须 type="module"） -->
    <script type="module">
        import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js';

        // 3. 创建 Vue 实例 + 挂载
        createApp({
            data() {
                return {
                    message: "Hello Vue3"
                };
            }
        }).mount("#app");
    </script>
</body>
</html>
```

##### 10. 常用指令

```html
<div id="app">
    <!-- v-bind：绑定属性。简写为 : -->
    <a v-bind:href="url">百度</a>
    <a :href="url">百度（简写）</a>

    <!-- v-model：双向绑定（表单常用） -->
    <input type="text" v-model="username">
    <p>你输入的：{{ username }}</p>

    <!-- v-on：绑定事件。简写为 @ -->
    <button v-on:click="handleClick">点我</button>
    <button @click="handleClick">点我（简写）</button>

    <!-- v-if / v-else-if / v-else：满足才渲染（不渲染就不进 DOM） -->
    <p v-if="age >= 60">老年</p>
    <p v-else-if="age >= 18">成年</p>
    <p v-else>未成年</p>

    <!-- v-show：满足才显示（DOM 一直在，靠 display 切换） -->
    <p v-show="isShow">显示/隐藏</p>

    <!-- v-for：遍历数组 -->
    <ul>
        <li v-for="(item, index) in list" :key="index">
            {{ index }} - {{ item.name }}
        </li>
    </ul>
</div>

<script type="module">
import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js';

createApp({
    data() {
        return {
            url: "https://www.baidu.com",
            username: "",
            age: 20,
            isShow: true,
            list: [
                {name: "张三"},
                {name: "李四"},
                {name: "王五"}
            ]
        };
    },
    methods: {
        handleClick() {
            alert("点击事件");
        }
    }
}).mount("#app");
</script>
```

##### 11. Axios 异步请求

引入 Axios：

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

```js
// GET 请求
axios.get("https://yapi.smart-xwork.cn/mock/169327/emp/list")
     .then(result => {
         console.log("成功", result.data);
     })
     .catch(err => {
         console.log("失败", err);
     });

// POST 请求（带请求体）
axios.post("https://yapi.smart-xwork.cn/mock/169327/emp/add", {
        name: "张三",
        age: 20
     })
     .then(result => {
         console.log(result.data);
     });

// 通用写法 axios({})
axios({
    method: "get",
    url: "https://yapi.smart-xwork.cn/mock/169327/emp/list"
}).then(result => {
    console.log(result.data);
});
```

##### 12. 生命周期钩子 mounted

`mounted` 在 Vue 实例挂载完成后触发，是发送异步请求初始化数据的最佳位置。

```html
<div id="app">
    <table border="1">
        <tr>
            <th>姓名</th>
            <th>性别</th>
            <th>职位</th>
        </tr>
        <tr v-for="emp in empList">
            <td>{{ emp.name }}</td>
            <td>{{ emp.gender == 1 ? "男" : "女" }}</td>
            <td>{{ emp.job }}</td>
        </tr>
    </table>
</div>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script type="module">
import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js';

createApp({
    data() {
        return {
            empList: []
        };
    },
    // 页面挂载完毕自动跑，最常用的生命周期
    mounted() {
        axios.get("https://yapi.smart-xwork.cn/mock/169327/emp/list")
             .then(result => {
                 this.empList = result.data.data;
             });
    }
}).mount("#app");
</script>
```

Vue3 完整生命周期 8 个钩子：`beforeCreate` → `created` → `beforeMount` → **`mounted`** → `beforeUpdate` → `updated` → `beforeUnmount` → `unmounted`。考试只重点考 `mounted`。

---

## CH3 Maven 基础知识点

### 一、Maven 是什么

Maven 是 Apache 旗下的开源 Java 项目管理与构建工具，本身用 Java 写的，解压即用。安装目录里 `bin` 放 `mvn` 可执行命令、`conf` 放 `settings.xml` 配置文件、`lib` 放 Maven 自己依赖的 jar。

一句话：Maven 就是「管依赖 + 统一结构 + 自动化构建」Java 项目的工具。

### 二、三大作用（必考）

1. **依赖管理**：在 `pom.xml` 里写 `<dependency>` 坐标，Maven 自动去仓库拉取，顺便解决版本冲突。
2. **统一项目结构**：不管 IDEA、Eclipse、MyEclipse，Maven 项目结构一样，跨工具直接导入。
3. **标准化构建**：`compile / test / package / deploy` 命令跨平台。

### 三、坐标三要素（必考）

每个 Maven 项目（jar 包）都有一个全球唯一的坐标：

- `groupId`：组织名（一般用域名反写，如 `org.springframework`）
- `artifactId`：模块名 / jar 包名
- `version`：版本号

`pom.xml` 根标签是 `<project>`，里面 `<modelVersion>4.0.0</modelVersion>` 声明 POM 模型版本。

### 四、三类仓库 + 查找顺序（必考）

- **本地仓库**：自己电脑上的目录，存放下载下来的 jar。
- **中央仓库**：Maven 团队维护的全球唯一仓库（repo1.maven.org）。
- **远程仓库（私服）**：公司团队自建，国内一般配阿里云镜像。

**依赖查找顺序：本地仓库 → 远程仓库（私服） → 中央仓库**。本地有就直接用，没有才往上找，下下来后存进本地仓库下次复用。

### 五、标准项目结构（必考）

```
project/
├── pom.xml                  # 项目配置文件
├── src/
│   ├── main/
│   │   ├── java/            # 主程序源码
│   │   └── resources/       # 主程序资源文件
│   └── test/
│       ├── java/            # 测试代码
│       └── resources/       # 测试资源文件
└── target/                  # 编译输出
```

### 六、生命周期（必考）

三套互相独立的生命周期：**clean**（清理）、**default**（默认构建）、**site**（站点生成）。同一套内阶段有先后顺序，**后面的阶段会自动执行前面的阶段**。

五个核心阶段：

- `clean`：移除上次构建生成的文件（清空 target）
- `compile`：编译源代码
- `test`：跑 JUnit 单元测试
- `package`：把编译结果打成 jar / war
- `install`：把项目安装到本地仓库，路径就是 `groupId/artifactId/version` 拼出来的

**考点**：执行 `package` 时 `compile` 会跑（同 default 套），但 `clean` 不会跑（属于不同套）。`mvn clean install` 会先清理再走 compile → test → package → install。

### 七、依赖范围 scope（必考）

| scope | 主程序（main） | 测试程序（test） | 打包 | 典型例子 |
|---|---|---|---|---|
| compile（默认） | 可用 | 可用 | 参与 | spring-core |
| test | 不可用 | 可用 | 不参与 | junit |
| provided | 可用 | 可用 | 不参与 | servlet-api |
| runtime | 不可用 | 可用 | 参与 | jdbc 驱动 |
| system | 可用 | 可用 | 不参与 | 本地 jar |

JUnit 的 scope 设成 test 后，在 main 里写 `@Test` 会报红，但 test 包不受影响。

### 八、依赖传递与排除依赖（必考）

**依赖传递**：A 依赖 B、B 依赖 C，那 A 里也会有 C。

**排除依赖**：不想要某个传递进来的包，就在 `<dependency>` 里嵌套 `<exclusions>`：

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.4</version>
    <exclusions>
        <exclusion>
            <groupId>io.micrometer</groupId>
            <artifactId>micrometer-observation</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

### 九、JUnit 单元测试

**单元测试**：针对方法写测试代码验证正确性。比 main 方法测试好的地方：单个用例出错不影响其他、能出测试报告。

常用注解：

- `@Test`：标记测试方法
- `@BeforeEach` / `@AfterEach`：每个测试方法前/后都跑一次
- `@BeforeAll` / `@AfterAll`：所有方法前/后只跑一次（必须 static）
- `@DisplayName("...")`：自定义测试显示名
- `@ParameterizedTest` + `@ValueSource(strings={...})`：参数化测试
- `@CsvSource({"a,1", "b,2"})`：传多个参数

常用断言（`org.junit.jupiter.api.Assertions`）：`assertEquals(预期, 实际)`、`assertNotEquals`、`assertTrue`、`assertFalse`、`assertNull`、`assertNotNull`、`assertThrows(异常类, () -> ...)`。

### 十、高频代码片段

**典型 pom.xml 依赖（带 scope）**：

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>6.1.4</version>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.9.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

**JUnit 测试类最小模板**：

```java
package com.itheima;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class UserServiceTest {
    private UserService userService;

    @BeforeEach
    void init() { userService = new UserService(); }

    @Test
    @DisplayName("测试性别判断")
    void testGetGender() {
        assertEquals("男", userService.getGender("110101200001011234"));
    }

    @ParameterizedTest
    @ValueSource(strings = {"", "123", "12345678901234567890"})
    void testInvalidId(String id) {
        assertThrows(RuntimeException.class, () -> userService.getGender(id));
    }
}
```


---


### 课件代码示例（Maven）

> 下面这些代码示例对应老师 PPT 里的截图，对着看更好理解。

#### 1. 完整的 pom.xml 骨架

讲义里反复用到的标准 pom 文件结构，groupId/artifactId/version 三件套就是 Maven 坐标。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itheima</groupId>
    <artifactId>maven-project01</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- 在这里写依赖 -->
    </dependencies>

</project>
```

#### 2. 常见 dependency 写法

去 [mvnrepository.com](https://mvnrepository.com/) 搜对应 jar，复制坐标贴进 `<dependencies>` 即可。

```xml
<dependencies>
    <!-- Spring 上下文（讲义里的示范） -->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-context</artifactId>
        <version>6.1.4</version>
    </dependency>

    <!-- JUnit 5 单元测试 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.10.2</version>
        <scope>test</scope>
    </dependency>

    <!-- MySQL 驱动 -->
    <dependency>
        <groupId>com.mysql</groupId>
        <artifactId>mysql-connector-j</artifactId>
        <version>8.3.0</version>
    </dependency>

    <!-- Spring Boot 起步依赖（Web 场景） -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <version>3.2.4</version>
    </dependency>
</dependencies>
```

#### 3. scope 各种取值示例

讲义专门讲了 `scope=test` 的效果：主程序里就用不了这个依赖了。五种取值对应不同生效阶段。

```xml
<!-- compile：默认值，编译/测试/运行都生效 -->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.4</version>
    <scope>compile</scope>
</dependency>

<!-- provided：编译和测试时生效，运行时由容器提供（如 servlet-api） -->
<dependency>
    <groupId>jakarta.servlet</groupId>
    <artifactId>jakarta.servlet-api</artifactId>
    <version>6.0.0</version>
    <scope>provided</scope>
</dependency>

<!-- runtime：测试和运行时生效，编译时不需要（如 JDBC 驱动） -->
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>8.3.0</version>
    <scope>runtime</scope>
</dependency>

<!-- test：只在 src/test 里能用，主程序看不到 -->
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
</dependency>

<!-- system：本地系统 jar，要配 systemPath，不推荐用 -->
<dependency>
    <groupId>com.local</groupId>
    <artifactId>my-sdk</artifactId>
    <version>1.0</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/my-sdk-1.0.jar</systemPath>
</dependency>
```

#### 4. 依赖排除示例

讲义里的例子：引入 `spring-context` 时会顺带传递进来 `micrometer-observation`，不想要就排掉它。

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.4</version>
    <exclusions>
        <exclusion>
            <groupId>io.micrometer</groupId>
            <artifactId>micrometer-observation</artifactId>
        </exclusion>
    </exclusions>
</dependency>
```

#### 5. settings.xml 配置阿里云镜像

改 `conf/settings.xml`，在 `<mirrors>` 标签里加这一段，下载就走阿里云。

```xml
<mirrors>
    <mirror>
        <id>aliyunmaven</id>
        <mirrorOf>central</mirrorOf>
        <name>阿里云公共仓库</name>
        <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
</mirrors>
```

顺便记一下本地仓库的配置位置（settings.xml 53 行附近）：

```xml
<localRepository>D:\develop\apache-maven-3.6.1\mvn_repo</localRepository>
```

#### 6. JUnit 测试代码模板（五个注解齐全）

`@BeforeAll`/`@AfterAll` 必须 `static`，因为它们在类加载阶段就跑。

```java
package com.itheima;

import org.junit.jupiter.api.*;

public class UserServiceTest {

    @BeforeAll
    public static void beforeAll() {
        System.out.println("所有方法之前跑一次，常用来初始化数据库连接");
    }

    @BeforeEach
    public void beforeEach() {
        System.out.println("每个 @Test 之前都跑一次");
    }

    @Test
    @DisplayName("测试获取年龄")
    public void testGetAge() {
        UserService userService = new UserService();
        int age = userService.getAge("320323200301011234");
        Assertions.assertEquals(22, age);
    }

    @AfterEach
    public void afterEach() {
        System.out.println("每个 @Test 之后都跑一次");
    }

    @AfterAll
    public static void afterAll() {
        System.out.println("所有方法之后跑一次，常用来释放资源");
    }
}
```

#### 7. JUnit 断言示例

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AssertDemoTest {

    @Test
    public void testAssertions() {
        UserService userService = new UserService();

        // 断言相等
        assertEquals("男", userService.getGender("320323200301011233"));

        // 断言为真 / 为假
        assertTrue(userService.getAge("320323200301011234") > 0);
        assertFalse(userService.getGender("320323200301011233").equals("女"));

        // 断言为 null / 不为 null
        assertNull(userService.findById(-1));
        assertNotNull(userService.getGender("320323200301011233"));

        // 断言抛出异常
        assertThrows(IllegalArgumentException.class,
                () -> userService.getAge(null));
    }
}
```

#### 8. JUnit 参数化测试

`@ParameterizedTest` + `@ValueSource` 一次跑多组参数，省得写一堆 `@Test`。

```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import static org.junit.jupiter.api.Assertions.assertNotNull;

public class UserServiceParamTest {

    @ParameterizedTest
    @ValueSource(strings = {
            "320323200301011233",
            "320323199912121234",
            "110101200505056789"
    })
    public void testGetGender(String idCard) {
        UserService userService = new UserService();
        String gender = userService.getGender(idCard);
        assertNotNull(gender);
    }

    // 整数参数化
    @ParameterizedTest
    @ValueSource(ints = {1, 2, 3, 100})
    public void testPositive(int num) {
        org.junit.jupiter.api.Assertions.assertTrue(num > 0);
    }
}
```

参数化测试要加额外依赖：

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-params</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
</dependency>
```

---

## CH4 Web 基础知识点

### 一、SpringBoot Web 入门

SpringBoot 是 Spring 家族中目前最火的项目，相对于直接用 SpringFramework 解决了**配置繁琐**和**入门难度大**两个痛点，核心特点就两条：**简化配置 + 快速开发**。底层最核心的还是 SpringFramework，提供依赖注入、事务管理、Web 开发支持、数据访问、消息服务等能力。

**起步依赖**：`spring-boot-starter-web` 是一组预定义依赖的集合，一次性把 Web 场景所需的库和配置都拉进来。它又依赖 `spring-boot-starter-tomcat`，靠 Maven 依赖传递特性把 Tomcat 也自动带进了项目，这就是**内嵌 Tomcat**——所以一个 `main` 方法就能把 Web 应用跑起来，默认占用 **8080 端口**。注意 SpringBoot 3.x 最低需要 **JDK17**。

**最小 Controller 示例**：

```java
@RestController
public class HelloController {
    @RequestMapping("/hello")
    public String hello() {
        return "Hello SpringBoot";
    }
}
```

启动引导类（`@SpringBootApplication` 标注的类）里调用 `SpringApplication.run(...)`，浏览器访问 `http://localhost:8080/hello` 即可看到返回值。

### 二、HTTP 协议

**定义**：HyperText Transfer Protocol，超文本传输协议，规定浏览器和服务器之间数据传输的格式。

**特点**：
- 基于 TCP：面向连接（三次握手），可靠、基于字节流
- 基于请求-响应模型：一次请求对应一次响应，先请求后响应
- 无状态：服务端不记录上次请求的任何信息。优点是速度快，缺点是多次请求之间没法共享数据（购物车场景需要 Cookie/Session 弥补）

**请求消息格式**（三部分）：
- **请求行**：`请求方式 资源路径 协议/版本`，例如 `GET /brand/findAll?name=OPPO&status=1 HTTP/1.1`
- **请求头**：`key: value` 形式，告诉服务端客户端的浏览器类型、希望的响应形式等
- **请求体**：存放请求参数。**GET 请求参数挂在 URL 后面，没有请求体；POST 请求参数才放在请求体里**。请求头和请求体之间用一个空行隔开

**响应消息格式**（三部分）：
- **响应行**：`协议/版本 状态码 状态码描述`，例如 `HTTP/1.1 200 OK`
- **响应头**：常见有 `Content-Type`（响应内容类型，`text/html`、`application/json`）、`Content-Length`（字节数）、`Content-Encoding`（如 `gzip`）、`Cache-Control`（缓存策略）、`Set-Cookie`
- **响应体**：实际数据，和响应头之间用空行隔开

**GET vs POST**：GET 参数拼在 URL 上、长度有限、相对不安全、能被缓存；POST 参数在请求体里、长度无限制、相对安全、不会被缓存。

### 三、HTTP 状态码

五大类含义：
- **1xx**：信息性，请求已接收、继续处理
- **2xx**：成功
- **3xx**：重定向，需要进一步操作才能完成请求
- **4xx**：客户端错误，请求有语法错误或资源不存在
- **5xx**：服务端错误，服务端抛异常或挂了

常见状态码：
- `200 OK`：请求成功
- `302 Found`：临时重定向
- `304 Not Modified`：资源未修改，用浏览器缓存
- `400 Bad Request`：请求语法错误
- `404 Not Found`：资源不存在
- `405 Method Not Allowed`：请求方式不被允许
- `500 Internal Server Error`：服务端不可预期的错误

### 四、三层架构

之前案例里读文件、处理数据、响应页面的代码全堆在一个 Controller 方法里，业务一复杂就难维护。**单一职责原则**说一个类一个方法只干一件事，所以要分层。

三层结构和**调用方向 Controller → Service → DAO**：
- **Controller（控制层）**：包名 `com.itheima.controller`。接收前端请求、调 Service、把结果响应回去
- **Service（业务逻辑层）**：包名 `com.itheima.service`，实现类放 `com.itheima.service.impl`。处理具体业务逻辑
- **DAO（数据访问层 Data Access Object）**：包名 `com.itheima.dao`，实现类放 `com.itheima.dao.impl`。负责增删改查、与数据库或文件交互

执行流程：前端 → Controller 接收 → 调 Service 处理逻辑 → Service 调 DAO 取数据 → DAO 返回给 Service → Service 返回给 Controller → Controller 响应前端。

**三层架构好处**：复用性强、便于维护、利于扩展。

### 五、IOC 与 DI 核心思想

光分层还不够，分完之后 Controller 里 `new UserServiceImpl()`、Service 里 `new UserDaoImpl()`，层与层照样**耦合**了。设计原则是**高内聚低耦合**：模块内部联系紧密、模块之间依赖越弱越好。

- **IOC（Inversion of Control，控制反转）**：对象创建权由程序员转交给容器（**IOC 容器 / Spring 容器**），容器创建并管理的对象叫 **Bean**
- **DI（Dependency Injection，依赖注入）**：程序运行时需要某个对象，容器自动把这个对象塞进去

**声明 Bean 的四大注解**（都基于 `@Component`）：
- `@Component`：通用，归属不明确的类用它
- `@Controller`：控制层
- `@Service`：业务层
- `@Repository`：数据访问层
- `@RestController` = `@Controller` + `@ResponseBody`，方法返回值自动转 JSON 响应给前端

注意：SpringBoot Web 开发里控制层 Bean 只能用 `@Controller`（或 `@RestController`），Service 和 DAO 层虽然也能用 `@Component` 但不推荐，要用语义更明确的注解。

**组件扫描**：四大注解要生效，得被 `@ComponentScan` 扫到。该注解已经包含在 `@SpringBootApplication` 里，**默认扫描范围是启动类所在包及其子包**。所以启动类要放在最外层包。Bean 名字默认是类名首字母小写。

### 六、依赖注入注解

- **`@Autowired`**：Spring 提供，**默认按类型注入**。三种用法：①属性注入（最简洁）；②构造函数注入（官方推荐）；③setter 注入（少用）
- **`@Qualifier("beanName")`**：同类型 Bean 有多个时按名字指定。**必须配合 `@Autowired` 一起用**
- **`@Resource(name="beanName")`**：JDK 自带，按名字注入。相当于 `@Autowired + @Qualifier`
- **`@Primary`**：多个实现类时，在某个实现类上加这个注解抬高优先级

**`@Autowired` vs `@Resource`**：
- `@Autowired` 是 Spring 提供的，`@Resource` 是 JDK 提供的
- `@Autowired` 默认按类型注入，`@Resource` 默认按名称注入

### 七、B/S vs C/S 架构

| 对比项 | B/S（浏览器/服务器） | C/S（客户端/服务器） |
|---|---|---|
| 维护 | 只维护服务端，方便 | 客户端和服务端都要维护 |
| 客户端 | 浏览器即可，不占空间 | 要装专门客户端，要升级 |
| 体验 | 早期不如 C/S，现在差不多 | 流畅，对网速要求低 |
| 开发 | 只需开发服务端 | 客户端服务端都要开发 |
| 典型场景 | 京东、淘宝 | QQ、微信 |

### 八、三层架构代码骨架（必考拆分模板）

**DAO 层**：

```java
public interface UserDao {
    List<User> findAll();
}

@Repository
public class UserDaoImpl implements UserDao {
    public List<User> findAll() {  /* 读文件/查库 */  return list; }
}
```

**Service 层**：

```java
public interface UserService {
    List<User> findAll();
}

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserDao userDao;
    public List<User> findAll() { return userDao.findAll(); }
}
```

**Controller 层**：

```java
@RestController
public class UserController {
    @Autowired
    private UserService userService;
    @RequestMapping("/list")
    public List<User> list() { return userService.findAll(); }
}
```

注解位置速记：实现类上面贴 `@Repository` / `@Service`，控制器类上面贴 `@RestController`，每层用到下层的接口属性上面贴 `@Autowired`。


---


### 课件代码示例（Web 基础）

> 下面这些代码示例对应老师 PPT 里的截图，对着看更好理解。

#### 1. SpringBoot 启动类

最简单的启动类，一个 `@SpringBootApplication` + `main` 方法就能把内嵌 Tomcat 跑起来。

```java
package com.itheima;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringbootWebQuickstartApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootWebQuickstartApplication.class, args);
    }
}
```

启动类不要放在子包里，要放在最外层包（如 `com.itheima`），这样 `@ComponentScan` 默认扫描范围（启动类所在包及其子包）才能把所有 bean 都扫到。

---

#### 2. 最简 Controller

`@RestController` + `@RequestMapping`，访问 `http://localhost:8080/hello` 返回字符串。

```java
package com.itheima.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @RequestMapping("/hello")
    public String hello() {
        return "Hello World!";
    }
}
```

---

#### 3. 接收请求参数

##### 3.1 `@RequestParam` —— 取 URL 上的 `?name=xxx`

对应 URL：`/user?name=OPPO&status=1`

```java
@RestController
public class UserController {

    @RequestMapping("/user")
    public String getUser(@RequestParam String name,
                          @RequestParam Integer status) {
        return "name=" + name + ", status=" + status;
    }
}
```

##### 3.2 `@PathVariable` —— 取路径中的变量

对应 URL：`/user/100`

```java
@RestController
public class UserController {

    @RequestMapping("/user/{id}")
    public String getById(@PathVariable Integer id) {
        return "查询用户 id=" + id;
    }
}
```

##### 3.3 `@RequestBody` —— 取 POST 请求体里的 JSON

```java
@RestController
public class UserController {

    @RequestMapping("/user/add")
    public String add(@RequestBody User user) {
        return "新增用户：" + user.getName();
    }
}
```

---

#### 4. HTTP 请求报文格式

##### 4.1 GET 请求（参数拼在请求行，没有请求体）

```http
GET /brand/findAll?name=OPPO&status=1 HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml
Accept-Encoding: gzip, deflate
Connection: keep-alive

```

说明：请求行（方法 + 路径 + 协议） → 请求头（`key: value`） → 空行 → GET 没请求体。

##### 4.2 POST 请求（参数放在请求体里）

```http
POST /brand HTTP/1.1
Host: localhost:8080
Content-Type: application/json
Content-Length: 42
User-Agent: Mozilla/5.0

{"name":"OPPO","status":1,"company":"OPPO"}
```

空行就是给服务器一个「请求头到这里结束」的信号。

---

#### 5. HTTP 响应报文格式

```http
HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 138
Content-Encoding: gzip
Cache-Control: max-age=300
Set-Cookie: JSESSIONID=ABC123; Path=/

<html>
  <body>
    <h1>Hello Response</h1>
  </body>
</html>
```

三部分：状态行（协议 + 状态码 + 描述） → 响应头 → 空行 → 响应体。

手动设置响应（链式编程）：

```java
@RequestMapping("/resp")
public ResponseEntity<String> resp() {
    return ResponseEntity.status(401)
            .header("name", "itcast2")
            .body("<h1>hello Response2</h1>");
}
```

实际开发里状态码和响应头一般不手动设，服务器自动处理。

---

#### 6. `@RestController` vs `@Controller` + `@ResponseBody`

##### 6.1 `@RestController` 写法（推荐）

```java
@RestController
public class UserController {
    @RequestMapping("/list")
    public List<User> list() {
        return userService.list();  // 自动转 JSON
    }
}
```

##### 6.2 `@Controller` + `@ResponseBody` 写法

```java
@Controller
public class UserController {

    @RequestMapping("/list")
    @ResponseBody
    public List<User> list() {
        return userService.list();
    }
}
```

不加 `@ResponseBody`，`@Controller` 默认会把返回值当成视图名去找 JSP/Thymeleaf 模板。

---

#### 7. 三层架构目录结构

```
src/main/java/
└── com/itheima/
    ├── SpringbootWebDemoApplication.java   # 启动类，放最外层
    ├── controller/
    │   └── UserController.java             # 接收请求、响应数据
    ├── service/
    │   ├── UserService.java                # 业务接口
    │   └── impl/
    │       └── UserServiceImpl.java        # 业务实现
    ├── dao/
    │   ├── UserDao.java                    # 数据访问接口
    │   └── impl/
    │       └── UserDaoImpl.java            # 数据访问实现
    └── pojo/
        └── User.java                       # 实体类
```

调用流程：前端 → Controller → Service → Dao → 数据源；返回反过来一层层往上传。

---

#### 8. IOC 声明 Bean 的四个注解

bean 名默认是类名首字母小写。

```java
@Component   // 通用
public class MailUtils { }

@Controller  // 控制层（或 @RestController）
public class PageController { }

@Service     // 业务层
public class UserServiceImpl implements UserService { }

@Repository  // 数据层
public class UserDaoImpl implements UserDao { }
```

后三个底层封装的还是 `@Component`，分开命名就是为了标识 bean 归属哪一层。控制层只能用 `@Controller` / `@RestController`，**不能**用 `@Component` 替代。

也可以指定 bean 名：

```java
@Service("myUserService")
public class UserServiceImpl implements UserService { }
```

---

#### 9. 依赖注入 `@Autowired`

##### 9.1 属性注入（简洁，企业常用）

```java
@RestController
public class UserController {
    @Autowired
    private UserService userService;
}
```

##### 9.2 构造函数注入（官方推荐，规范）

```java
@RestController
public class UserController {
    private final UserService userService;

    @Autowired   // 只有一个构造函数时这个注解可以省略
    public UserController(UserService userService) {
        this.userService = userService;
    }
}
```

##### 9.3 setter 注入（用得少）

```java
@RestController
public class UserController {
    private UserService userService;

    @Autowired
    public void setUserService(UserService userService) {
        this.userService = userService;
    }
}
```

---

#### 10. 多 Bean 消歧义

`UserService` 有两个实现 → 直接 `@Autowired` 会报错。三种解决方法：

```java
// 方法一：@Primary 标默认优先
@Primary
@Service
public class UserServiceImpl2 implements UserService { }
```

```java
// 方法二：@Qualifier 指名要谁
@Qualifier("userServiceImpl")
@Autowired
private UserService userService;
```

```java
// 方法三：@Resource 按名注入（JDK 自带）
@Resource(name = "userServiceImpl2")
private UserService userService;
```

**`@Autowired` vs `@Resource`**：前者 Spring 提供、按**类型**注入；后者 JDK 提供、按**名称**注入。

---

## CH5 MySQL 数据库知识点

### 1. 数据库基础概念

- **DB（DataBase）**：数据库，本质上就是存数据的仓库。
- **DBMS（DataBase Management System）**：数据库管理系统，常见的有 MySQL、Oracle、SQL Server、DB2。
- **SQL（Structured Query Language）**：结构化查询语言，操作关系型数据库的统一标准。

三者关系：程序员写 SQL → 发给 DBMS → DBMS 操作 DB 里的数据。

MySQL 默认端口 **3306**，默认管理员账号 `root`。命令行登录：

```bash
mysql -uroot -p
```

### 2. SQL 分类（期末必考）

| 分类 | 全称 | 作用 | 代表关键字 |
|---|---|---|---|
| DDL | Data Definition Language | 定义数据库对象（库、表、字段） | `CREATE`、`DROP`、`ALTER` |
| DML | Data Manipulation Language | 增删改表里的数据 | `INSERT`、`UPDATE`、`DELETE` |
| DQL | Data Query Language | 查询数据 | `SELECT` |
| DCL | Data Control Language | 控制用户权限 | `GRANT`、`REVOKE` |

注释写法：单行 `-- 内容`（`--` 后要有空格）或 `# 内容`；多行 `/* ... */`。

### 3. DDL —— 库和表

**操作数据库**：
```sql
SHOW DATABASES;            -- 查询所有数据库
CREATE DATABASE db01;      -- 创建
USE db01;                  -- 切换
SELECT DATABASE();         -- 看当前用的哪个
DROP DATABASE db01;        -- 删除
```

**常用数据类型**：

- 数值：`TINYINT`（1 字节）、`INT`（4 字节）、`BIGINT`（8 字节）、`DOUBLE`、`DECIMAL`（要精度就用它）
- 字符串：`CHAR(n)` 定长，不够补空格，性能好；`VARCHAR(n)` 变长，按实际占用，省空间。**两者区别就是定长 vs 变长**——手机号、身份证用 char，姓名、地址用 varchar
- 文本：`TEXT`、`LONGTEXT`
- 日期：`DATE`（年月日）、`DATETIME`（年月日时分秒，推荐）、`TIMESTAMP`（截止 2038 年）

**操作表**：
```sql
SHOW TABLES;
DESC emp;                   -- 看表结构
SHOW CREATE TABLE emp;      -- 看建表语句
ALTER TABLE emp ADD age INT COMMENT '年龄';
ALTER TABLE emp MODIFY age TINYINT;
ALTER TABLE emp DROP COLUMN age;
ALTER TABLE emp RENAME TO employee;
DROP TABLE emp;
```

### 4. 约束（5 种）

| 约束 | 关键字 | 含义 |
|---|---|---|
| 主键 | `PRIMARY KEY` | 非空且唯一，一张表只能有一个 |
| 自增 | `AUTO_INCREMENT` | 整数列自动 +1，配合主键用 |
| 非空 | `NOT NULL` | 不能为 null |
| 唯一 | `UNIQUE` | 值不能重复（可以为 null） |
| 默认 | `DEFAULT 值` | 没传时用默认值 |
| 外键 | `FOREIGN KEY` | 维护两张表的关联 |

**典型建表示例（emp 表）**：
```sql
CREATE TABLE emp(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT COMMENT 'ID,主键',
    username VARCHAR(20) NOT NULL UNIQUE COMMENT '用户名',
    password VARCHAR(32) NOT NULL DEFAULT '123456' COMMENT '密码',
    name VARCHAR(10) NOT NULL COMMENT '姓名',
    gender TINYINT UNSIGNED NOT NULL COMMENT '性别 1男 2女',
    phone CHAR(11) NOT NULL UNIQUE COMMENT '手机号',
    job TINYINT UNSIGNED COMMENT '职位',
    salary INT UNSIGNED COMMENT '薪资',
    entry_date DATE COMMENT '入职日期',
    dept_id INT UNSIGNED COMMENT '部门ID',
    create_time DATETIME COMMENT '创建时间',
    update_time DATETIME COMMENT '修改时间',
    CONSTRAINT fk_emp_dept_id FOREIGN KEY (dept_id) REFERENCES dept(id)
) COMMENT '员工表';
```

### 5. DML —— 增删改

**INSERT 三种写法**：
```sql
-- ① 指定字段插单条
INSERT INTO emp(username, name, gender) VALUES ('zs', '张三', 1);
-- ② 全字段插（值的顺序和字段顺序一致）
INSERT INTO emp VALUES (null,'ls','123','李四',1,'13800000000',1,5000,null,1,now(),now());
-- ③ 批量插
INSERT INTO emp(username,name,gender) VALUES ('a','甲',1),('b','乙',2),('c','丙',1);
```

**UPDATE / DELETE**：
```sql
UPDATE emp SET salary = 6000 WHERE id = 1;
DELETE FROM emp WHERE id = 5;
```

注意：`UPDATE` 和 `DELETE` 不写 `WHERE` 会作用到整张表。

**TRUNCATE vs DELETE 区别**：
- `DELETE FROM emp;` 一行一行删，可以带 where，自增 id 不重置。
- `TRUNCATE TABLE emp;` 直接清空表，速度快，自增 id 重置为 1，不能加 where。

### 6. DQL —— 查询

**完整语法顺序**（书写顺序）：
```sql
SELECT 字段列表
FROM 表名
WHERE 条件
GROUP BY 分组字段
HAVING 分组后条件
ORDER BY 排序字段
LIMIT 起始, 条数;
```

**执行顺序（必考）**：`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`。

#### 6.1 条件查询（WHERE）

比较运算符：`>`、`<`、`>=`、`<=`、`=`、`!=` 或 `<>`、`BETWEEN ... AND ...`、`IN(...)`、`LIKE`、`IS NULL`。
逻辑运算符：`AND`（或 `&&`）、`OR`（或 `||`）、`NOT`（或 `!`）。

模糊查询 LIKE 的通配符：`%` 匹配任意多个字符，`_` 匹配单个字符。
```sql
SELECT * FROM emp WHERE name LIKE '张%';     -- 姓张
SELECT * FROM emp WHERE name LIKE '_花_';    -- 中间是花，三个字
SELECT * FROM emp WHERE salary BETWEEN 5000 AND 10000;
SELECT * FROM emp WHERE job IN (1,2,3);
SELECT * FROM emp WHERE entry_date IS NULL;
```

#### 6.2 分组查询（GROUP BY + 聚合）

聚合函数：
- `COUNT(列)`：统计行数，null 不计；`COUNT(*)` 算所有行
- `SUM(列)`：求和
- `AVG(列)`：平均
- `MAX(列)` / `MIN(列)`：最大 / 最小

```sql
SELECT job, COUNT(*), AVG(salary)
FROM emp
WHERE entry_date <= '2024-01-01'
GROUP BY job
HAVING AVG(salary) > 5000;
```

**where 和 having 区别（必考）**：
- where 在分组**前**过滤，having 在分组**后**过滤
- where 后**不能**用聚合函数，having 后可以
- 不满足 where 的行根本不参与分组

#### 6.3 排序与分页

```sql
SELECT * FROM emp ORDER BY entry_date ASC, update_time DESC;
SELECT * FROM emp LIMIT 0, 10;
```

页码公式：**`LIMIT (page-1)*size, size`**。

### 7. 多表关系

- **一对多**：部门和员工。**在多的一方加外键**指向一的一方主键
- **一对一**：用户基本信息表和用户详情表拆分。任一方加外键 + UNIQUE
- **多对多**：学生和课程。必须**建第三张中间表**，中间表至少包含两个外键

外键 SQL：
```sql
ALTER TABLE emp ADD CONSTRAINT fk_emp_dept_id
    FOREIGN KEY (dept_id) REFERENCES dept(id);
```

### 8. 多表查询

#### 8.1 内连接（取交集）

- **隐式内连接**：用 WHERE
```sql
SELECT e.name, d.name FROM emp e, dept d WHERE e.dept_id = d.id;
```
- **显式内连接**：用 INNER JOIN ... ON
```sql
SELECT e.name, d.name FROM emp e INNER JOIN dept d ON e.dept_id = d.id;
```

#### 8.2 外连接

- **左外连接**：以左表为基准，左表全部 + 右表能匹配上的部分，匹配不到补 null
```sql
SELECT e.name, d.name FROM emp e LEFT JOIN dept d ON e.dept_id = d.id;
```
- **右外连接**：反过来，右表全部
```sql
SELECT e.name, d.name FROM emp e RIGHT JOIN dept d ON e.dept_id = d.id;
```

#### 8.3 子查询（嵌套查询）

四种：

- **标量子查询**：返回单个值，配合 `= > <` 用
```sql
SELECT * FROM emp WHERE dept_id = (SELECT id FROM dept WHERE name='教研部');
```
- **列子查询**：返回一列多个值，配合 `IN`、`NOT IN`
```sql
SELECT * FROM emp WHERE dept_id IN (SELECT id FROM dept WHERE name IN ('教研部','咨询部'));
```
- **行子查询**：返回一行多列
```sql
SELECT * FROM emp WHERE (salary, job) = (SELECT salary, job FROM emp WHERE name='张三');
```
- **表子查询**：返回多行多列，当成临时表用，放在 `FROM` 后

### 9. 事务

事务是把一组操作当成整体执行，要么全成功要么全回滚。

**ACID 四大特性（必考）**：
- **原子性 Atomicity**：要么全做完，要么一个都不做
- **一致性 Consistency**：执行前后数据库都处于一致状态
- **隔离性 Isolation**：并发事务之间互不干扰
- **持久性 Durability**：一旦提交，数据永久保存

**事务控制语句**：
```sql
START TRANSACTION;   -- 或 BEGIN; 开启事务
UPDATE account SET balance = balance - 100 WHERE name='A';
UPDATE account SET balance = balance + 100 WHERE name='B';
COMMIT;              -- 提交，出错时用 ROLLBACK 回滚
```

MySQL 默认自动提交（`SET @@autocommit=0;` 可关闭）。

### 10. 高频 SQL 题套路示例

**① 条件 + 模糊**：查询姓张且电话以 138 开头的员工
```sql
SELECT * FROM emp WHERE name LIKE '张%' AND phone LIKE '138%';
```

**② 分组 + having**：统计每个部门平均薪资大于 5000 的部门
```sql
SELECT dept_id, AVG(salary) FROM emp
GROUP BY dept_id HAVING AVG(salary) > 5000;
```

**③ 左外连接**：查询所有员工及其所属部门（包含没分配部门的）
```sql
SELECT e.name, d.name FROM emp e
LEFT JOIN dept d ON e.dept_id = d.id;
```

**④ 子查询**：查询薪资高于教研部平均薪资的员工
```sql
SELECT * FROM emp WHERE salary > (
    SELECT AVG(salary) FROM emp WHERE dept_id =
        (SELECT id FROM dept WHERE name='教研部')
);
```

**⑤ 分页**：第 2 页，每页 5 条，按入职时间倒序
```sql
SELECT * FROM emp ORDER BY entry_date DESC LIMIT 5, 5;
```


---

## CH6 JDBC 与 MyBatis 知识点

### 一、JDBC 概念

JDBC 全称 Java DataBase Connectivity，是 Sun 公司定义的一套用 Java 操作关系型数据库的规范/API（一组接口）。Sun 只定义接口、不给实现，由各家数据库厂商（MySQL、Oracle、SQL Server）提供自己的驱动 jar 包来实现这些接口。同一套 Java 代码，换个驱动就能换数据库。

企业项目里很少直接写裸 JDBC，一般用 MyBatis、MyBatis-Plus、Hibernate、Spring Data JPA 等封装框架。

### 二、JDBC 操作步骤（核心考点）

固定六步，记牢顺序：

1. **注册驱动**：`Class.forName("com.mysql.cj.jdbc.Driver");`
2. **获取连接**：`Connection conn = DriverManager.getConnection(url, user, password);`
3. **获取 Statement / PreparedStatement** 对象
4. **执行 SQL**：查询用 `executeQuery()` 返回 `ResultSet`；增删改用 `executeUpdate()` 返回受影响行数
5. **处理结果集**：`while(rs.next()){ rs.getString("name"); rs.getInt("age"); }`
6. **释放资源**：按 `ResultSet → Statement → Connection` 倒序关闭

#### 2.1 驱动类名差异

- MySQL 5.x 旧版：`com.mysql.jdbc.Driver`
- MySQL 8.x 新版：`com.mysql.cj.jdbc.Driver`（多了个 `cj`，必须用）

新版驱动会通过 SPI 自动注册，理论上 `Class.forName` 可省略，但保险起见还是写。

#### 2.2 JDBC URL 格式

```
jdbc:mysql://localhost:3306/db_name?useSSL=false&serverTimezone=Asia/Shanghai
```

参数说明：`useSSL=false` 关掉 SSL 握手警告；`serverTimezone=Asia/Shanghai` 解决 MySQL 8 必须指定时区的问题。

### 三、Statement vs PreparedStatement

| 对比项 | Statement | PreparedStatement |
|---|---|---|
| SQL 类型 | 静态 SQL，参数直接拼字符串 | 预编译 SQL，用 `?` 占位 |
| 安全性 | 有 SQL 注入风险 | 自动转义，**防 SQL 注入** |
| 性能 | 每次都要编译解析 | 语句结构在 DB 端缓存，重复执行更快 |

#### SQL 注入示例

登录场景，原始 SQL 拼接：

```java
String sql = "select * from user where name='" + name + "' and pwd='" + pwd + "'";
```

如果用户在密码框输入 `' or '1'='1`，SQL 就变成：

```sql
select * from user where name='admin' and pwd='' or '1'='1'
```

`'1'='1'` 恒真，整个 where 永远成立，密码白填都能登进去。用 `PreparedStatement` 的 `?` 占位之后，`'` 会被自动当成普通字符转义，注入就废了。

### 四、JDBC 预编译查询完整模板（实践 6 第三题，必考）

题目：查询 `id <= 4` 且 `age > 20` 的用户。

```java
import java.sql.*;

public class JdbcPreparedDemo {
    public static void main(String[] args) {
        String url  = "jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=Asia/Shanghai";
        String user = "root";
        String pwd  = "123456";

        Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        try {
            // 1. 注册驱动
            Class.forName("com.mysql.cj.jdbc.Driver");
            // 2. 获取连接
            conn = DriverManager.getConnection(url, user, pwd);
            // 3. 预编译 SQL，用 ? 占位
            String sql = "select id, name, age from user where id <= ? and age > ?";
            ps = conn.prepareStatement(sql);
            // 4. 给占位符赋值，下标从 1 开始
            ps.setInt(1, 4);
            ps.setInt(2, 20);
            // 5. 执行查询
            rs = ps.executeQuery();
            // 6. 遍历结果集
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                System.out.println(id + " " + name + " " + age);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 7. 倒序释放资源
            try { if (rs != null) rs.close(); } catch (SQLException e) { e.printStackTrace(); }
            try { if (ps != null) ps.close(); } catch (SQLException e) { e.printStackTrace(); }
            try { if (conn != null) conn.close(); } catch (SQLException e) { e.printStackTrace(); }
        }
    }
}
```

### 五、MyBatis 概念

MyBatis 是一个持久层框架，本质就是对 JDBC 的封装。它把 SQL 语句从 Java 代码里抽出来（写在注解或 XML 里），开发者只关心 SQL 和接口方法的映射，不用管注册驱动、获取连接、释放资源这些重复活。**核心价值：SQL 与 Java 解耦**。

### 六、MyBatis 入门（SpringBoot 整合）

#### 6.1 配置 application.properties

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=123456
```

#### 6.2 Mapper 接口示例（注解方式增删改查）

```java
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface UserMapper {

    @Select("select * from user where id = #{id}")
    User findById(Integer id);

    @Insert("insert into user(name, age) values(#{name}, #{age})")
    int insert(User user);

    @Update("update user set age = #{age} where id = #{id}")
    int updateAge(@Param("id") Integer id, @Param("age") Integer age);

    @Delete("delete from user where id = #{id}")
    int deleteById(Integer id);
}
```

`@Mapper` 标在接口上，SpringBoot 启动时会自动扫描并生成代理实现类，业务层直接 `@Autowired` 注入就能用。

### 七、#{} vs ${}（重点对比）

| 写法 | 本质 | 安全性 | 用途 |
|---|---|---|---|
| `#{}` | 预编译占位，会被翻译成 JDBC 的 `?`，再用 `PreparedStatement.setXxx()` 赋值 | 自动防 SQL 注入 | 传值（where 条件、insert 值等），**绝大多数情况用它** |
| `${}` | 字符串直接拼接到 SQL 里 | 有 SQL 注入风险 | 需要动态拼**表名、列名、order by 字段**这种结构性内容 |

例子：`select * from user where name = #{name}` 安全；`select * from ${tableName}` 用于切表。

### 八、MyBatis XML 映射文件规范

1. **同名同包**：XML 文件名与 Mapper 接口名相同，放在 resources 下镜像目录里。
2. **namespace** 写 Mapper 接口的**全限定类名**。
3. **statement 的 id** 必须和接口方法名**一致**。
4. **不能重复**：同一个方法，注解和 XML 只能保留一种写法，否则启动报错。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.example.mapper.UserMapper">
    <select id="findById" resultType="com.example.entity.User">
        select * from user where id = #{id}
    </select>
</mapper>
```

### 九、数据库连接池

作用是**复用 Connection**，避免每次请求都走「TCP 三次握手 + 认证 + 关闭」的开销。SpringBoot 2.x 默认用 **HikariCP**（号称最快的连接池），备选 **Druid**（带监控页面，国内很流行）。换连接池只要换依赖，业务代码不用动。

### 十、SpringBoot 配置文件：properties vs yml

- `application.properties`：每行 `key=value`，扁平结构。
- `application.yml`：YAML 格式，靠**缩进**表示层级，**不能用 Tab，只能用空格**；`-` 开头表示数组元素。

```yaml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/test
    username: root
    password: 123456
```

两种格式效果一样，yml 更紧凑、层次清晰，但格式严格、错一个空格就报错。项目里通常用 yml。


---


### 课件代码示例（JDBC + MyBatis）

> 下面这些代码示例对应老师 PPT 里的截图，对着看更好理解。

#### 一、JDBC 部分

##### 1. JDBC 完整的查询代码（标准写法）

注册驱动 → 拿连接 → 创建 Statement → 执行 SQL → 遍历 ResultSet → 关闭资源。整个方法 `throws Exception`，不写 try-catch。

```java
public class JdbcSelect {
    public static void main(String[] args) throws Exception {
        // 1. 注册驱动（MySQL 8.x 用 cj 命名空间）
        Class.forName("com.mysql.cj.jdbc.Driver");

        // 2. 获取连接
        String url = "jdbc:mysql://localhost:3306/web01";
        String username = "root";
        String password = "root@1234";
        Connection conn = DriverManager.getConnection(url, username, password);

        // 3. 创建 Statement
        Statement stmt = conn.createStatement();

        // 4. 执行查询
        String sql = "select id, username, password, name, age from user";
        ResultSet rs = stmt.executeQuery(sql);

        // 5. 处理结果集：next() 为 true 说明这一行有数据
        while (rs.next()) {
            Integer id = rs.getInt("id");
            String uname = rs.getString("username");
            String pwd = rs.getString("password");
            String name = rs.getString("name");
            Integer age = rs.getInt("age");
            System.out.println(id + "," + uname + "," + pwd + "," + name + "," + age);
        }

        // 6. 释放资源（顺序与创建相反）
        rs.close();
        stmt.close();
        conn.close();
    }
}
```

##### 2. JDBC 更新代码（INSERT / UPDATE / DELETE）

DML 全部用 `executeUpdate()`，返回值是影响的行数。

```java
public class JdbcUpdate {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/web01", "root", "root@1234");
        Statement stmt = conn.createStatement();

        // INSERT
        int n1 = stmt.executeUpdate(
            "insert into user(username,password,name,age) values('zhouyu','123456','周瑜',20)");
        // UPDATE
        int n2 = stmt.executeUpdate(
            "update user set age = 21 where username = 'zhouyu'");
        // DELETE
        int n3 = stmt.executeUpdate(
            "delete from user where username = 'zhouyu'");

        System.out.println("插入影响行数：" + n1);
        System.out.println("更新影响行数：" + n2);
        System.out.println("删除影响行数：" + n3);

        stmt.close();
        conn.close();
    }
}
```

##### 3. PreparedStatement 预编译查询

SQL 里用 `?` 占位，再用 `setXxx(下标, 值)` 绑参，下标从 1 开始。

```java
public class JdbcPrepared {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/web01", "root", "root@1234");

        String sql = "select * from user where username = ? and password = ?";
        PreparedStatement pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, "daqiao");
        pstmt.setString(2, "123456");

        ResultSet rs = pstmt.executeQuery();
        while (rs.next()) {
            System.out.println(rs.getInt("id") + "," + rs.getString("name"));
        }

        rs.close();
        pstmt.close();
        conn.close();
    }
}
```

##### 4. SQL 注入演示

拼字符串的写法被 `' or '1'='1` 绕过；用 PreparedStatement 后整段参数被当成字符串转义掉。

```java
// 危险写法：字符串拼接（Statement）
String name = "shfhsjfhja";
String pwd  = "' or '1' = '1";   // 精心构造的密码
String sql  = "select * from user where username = '" + name +
              "' and password = '" + pwd + "'";
// 最终拼出：select * from user where username='shfhsjfhja' and password='' or '1'='1'
// or 为真，整条 where 恒成立，登录被绕过。

// 安全写法：预编译（PreparedStatement）
String sql2 = "select * from user where username = ? and password = ?";
PreparedStatement ps = conn.prepareStatement(sql2);
ps.setString(1, name);
ps.setString(2, pwd);   // ' or '1'='1 整体作为字符串参数，不会改变 SQL 结构
ResultSet rs = ps.executeQuery();
```

控制台日志里 `==>` 是发给数据库的预编译命令和参数，`<==` 是数据库返回的信息。

---

#### 二、MyBatis 部分

##### 5. application.properties 配置 MyBatis

数据源四要素全部以 `spring.datasource.` 开头。

```properties
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/web01
spring.datasource.username=root
spring.datasource.password=root@1234

mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

##### 6. Mapper 接口注解方式（@Select / @Insert / @Update / @Delete）

接口上加 `@Mapper`，框架启动时自动生成代理对象交给 Spring IOC 管理。

```java
package com.itheima.mapper;

import com.itheima.pojo.User;
import org.apache.ibatis.annotations.*;
import java.util.List;

@Mapper
public interface UserMapper {

    // 查询全部
    @Select("select * from user")
    List<User> findAll();

    // 新增：#{} 里写 User 对象的属性名
    @Insert("insert into user(username,password,name,age) " +
            "values(#{username},#{password},#{name},#{age})")
    void insert(User user);

    // 修改
    @Update("update user set username = #{username}, password = #{password}, " +
            "name = #{name}, age = #{age} where id = #{id}")
    void update(User user);

    // 删除：返回值 Integer 表示影响行数
    @Delete("delete from user where id = #{id}")
    Integer deleteById(Integer id);
}
```

##### 7. @Param 注解传参（多参数方法）

两个以上形参时必须加 `@Param`，否则字节码里形参名会被擦成 `var1/var2`，`#{}` 取不到。

```java
@Select("select * from user where username = #{username} and password = #{password}")
User findByUsernameAndPassword(@Param("username") String username,
                               @Param("password") String password);
```

不需要 `@Param` 的两种情况：① 只有一个形参（哪怕是对象）；② 基于官方骨架（pom 里有 `spring-boot-starter-parent` 父工程）创建的 SpringBoot 项目，编译时会保留形参名。

##### 8. MyBatis XML 映射文件完整模板

namespace 写对应的 Mapper 接口全限定名，`<select>` 的 `id` 对应接口方法名，`resultType` 是返回的单条记录类型。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.itheima.mapper.UserMapper">

    <!-- 查询：resultType 是单条记录封装的类型 -->
    <select id="findAll" resultType="com.itheima.pojo.User">
        select id, username, password, name, age from user
    </select>

    <!-- 新增 -->
    <insert id="insert">
        insert into user(username, password, name, age)
        values(#{username}, #{password}, #{name}, #{age})
    </insert>

    <!-- 修改 -->
    <update id="update">
        update user
        set username = #{username},
            password = #{password},
            name     = #{name},
            age      = #{age}
        where id = #{id}
    </update>

    <!-- 删除 -->
    <delete id="deleteById">
        delete from user where id = #{id}
    </delete>

</mapper>
```

注意：同一个方法的 SQL，要么用注解、要么用 XML，**不能同时配**。

##### 9. MyBatis 单元测试代码

`@SpringBootTest` 启 Spring 容器，`@Autowired` 直接注入 Mapper 代理对象。

```java
@SpringBootTest
class SpringbootMybatisQuickstartApplicationTests {

    @Autowired
    private UserMapper userMapper;

    @Test
    public void testFindAll() {
        List<User> userList = userMapper.findAll();
        for (User user : userList) {
            System.out.println(user);
        }
    }

    @Test
    public void testInsert() {
        User user = new User();
        // id 不要给，让数据库自增
        user.setUsername("admin");
        user.setPassword("123456");
        user.setName("管理员");
        user.setAge(30);
        userMapper.insert(user);
    }

    @Test
    public void testUpdate() {
        User user = new User();
        user.setId(6);             // 更新必须给 id
        user.setUsername("admin666");
        user.setPassword("123456");
        user.setName("管理员");
        user.setAge(30);
        userMapper.update(user);
    }

    @Test
    public void testDeleteById() {
        userMapper.deleteById(36);
    }
}
```

注意：测试类的包名要跟引导类一致（例如都在 `com.itheima` 下），否则扫不到容器。

##### 10. `#{}` vs `${}` 对比

`#{}` 走预编译、自动转义、防注入；`${}` 是字符串直接拼接、有注入风险。**企业开发一律用 `#{}`**。

```java
// #{} 推荐：底层换成 ? 占位，传 Parameters: 5(Integer)
@Delete("delete from user where id = #{id}")
public Integer deleteById(Integer id);

// ${} 不推荐：直接把值拼进 SQL，等同于硬编码，会被注入
@Delete("delete from user where id = ${id}")
public Integer deleteById(Integer id);
```

日志对照：
```
==> Preparing: delete from user where id = ?    // #{} 是预编译
==> Parameters: 5(Integer)
<== Updates: 1
```

##### 11. Druid 连接池配置（替换默认 Hikari）

两步：pom 加依赖 + properties 改连接池类型。

```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.2.20</version>
</dependency>
```

```properties
spring.datasource.druid.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.druid.url=jdbc:mysql://localhost:3306/web01
spring.datasource.druid.username=root
spring.datasource.druid.password=root@1234
```

切完之后控制台日志里会从 `HikariDataSource` 变成 `com.alibaba.druid.pool.DruidDataSource`。常见连接池：C3P0、DBCP、Druid（阿里）、Hikari（SpringBoot 默认，追光者）。

##### 12. application.yml 完整示例

yml 用缩进表示层级，比 properties 更清爽。规则：**大小写敏感、冒号后必须有空格、缩进只能空格不能 Tab、`#` 是注释**。

```yaml
spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/web01
    username: root
    password: root@1234

mybatis:
  # 扫描 XML 映射文件的位置
  mapper-locations: classpath:mapper/*.xml
  configuration:
    # 打印 SQL 日志
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
```

yml 常见数据格式：

```yaml
user:
  name: zhangsan
  age: 18
  password: 123456

hobby:
  - java
  - game
  - sport
```

注意：值如果以 `0` 开头，要用 `''` 引起来，避免被当成八进制。

---

## MySQL 常用命令速查卡

### 连接登录
- `mysql -h主机 -u用户名 -p` — 连数据库，回车后输密码；本机可省略 `-h`。
- `mysql -uroot -p` — 最常用的本地登录写法。
- `exit;` 或 `quit;` — 退出客户端。

### DDL 数据库
- `SHOW DATABASES;` — 列出所有库。
- `CREATE DATABASE 库名;` — 建库；加 `IF NOT EXISTS` 防报错。
- `DROP DATABASE [IF EXISTS] 库名;` — 删库。
- `USE 库名;` — 切到该库。
- `SELECT DATABASE();` — 看当前用的是哪个库。

### DDL 表（重点 · 建表完整模板）
```sql
CREATE TABLE tb_emp (
  id       INT(11)      PRIMARY KEY AUTO_INCREMENT,   -- 主键自增
  name     VARCHAR(25)  NOT NULL,                      -- 非空
  deptId   INT(11)      DEFAULT 0,                     -- 默认值
  salary   FLOAT        CHECK(salary >= 0),            -- 检查
  email    VARCHAR(50)  UNIQUE,                        -- 唯一
  CONSTRAINT fk_dept FOREIGN KEY (deptId) REFERENCES tb_dept(id)
);
```
- `SHOW TABLES;` — 看当前库的表清单。
- `DESC 表名;` — 看表结构。
- `SHOW CREATE TABLE 表名\G` — 看建表原始 SQL。
- `DROP TABLE [IF EXISTS] 表1, 表2;` — 删表。
- `ALTER TABLE 表 ADD 列名 类型 [约束] [FIRST|AFTER 已有列];` — 加字段。
- `ALTER TABLE 表 MODIFY 列名 新类型;` — 改字段类型。
- `ALTER TABLE 表 CHANGE 旧列 新列 类型;` — 改字段名+类型。
- `ALTER TABLE 表 DROP 列名;` — 删字段。
- `ALTER TABLE 旧表名 RENAME [TO] 新表名;` — 改表名。

### DML 增删改
- `INSERT INTO 表 VALUES (值1, 值2, ...);` — 按表结构顺序全部插。
- `INSERT INTO 表(列1, 列2) VALUES (值1, 值2);` — 指定列插。
- `INSERT INTO 表(列1, 列2) VALUES (v1,v2),(v3,v4),(v5,v6);` — 一次插多行。
- `UPDATE 表 SET 列1=值1, 列2=值2 WHERE 条件;` — 改行，**不带 WHERE 会全表更新**。
- `DELETE FROM 表 WHERE 条件;` — 删行，不带 WHERE 全表清空。
- `TRUNCATE TABLE 表;` — 清空表数据（不可回滚，比 DELETE 快）。

### DQL 查询（考试主角）
基本骨架：
```sql
SELECT [DISTINCT] 字段
FROM 表
[WHERE 条件]
[GROUP BY 字段 [HAVING 聚合条件]]
[ORDER BY 字段 ASC|DESC]
[LIMIT 偏移量, 条数];
```
- `SELECT * FROM emp WHERE salary > 5000 AND deptId = 1;` — 多条件用 `AND/OR/NOT`。
- `WHERE name LIKE '张%';` — 模糊查询，`%` 多字符，`_` 单字符。
- `WHERE age BETWEEN 18 AND 30;` — 区间，等价于 `>=18 AND <=30`。
- `WHERE deptId IN (1,2,3);` — 枚举集合。
- `WHERE remark IS NULL;` — 空值判断不能用 `=`。
- `SELECT CONCAT(f_name,' ',l_name) AS Name FROM emp;` — 拼字符串 + 起别名。

**JOIN 三种连接：**
- 内连接：`SELECT * FROM a INNER JOIN b ON a.id=b.aid;` — 只取两表都匹配的行。
- 左连接：`SELECT * FROM a LEFT JOIN b ON a.id=b.aid;` — 左表全保留，右表没匹配的填 NULL。
- 右连接：`SELECT * FROM a RIGHT JOIN b ON a.id=b.aid;` — 右表全保留。

**分组聚合：**
- `SELECT deptId, COUNT(*), AVG(salary) FROM emp GROUP BY deptId;` — 按部门统计。
- `... GROUP BY deptId HAVING AVG(salary) > 6000;` — HAVING 过滤分组结果，WHERE 过滤行。
- 聚合函数：`COUNT() / SUM() / AVG() / MAX() / MIN()`。

**排序分页：**
- `ORDER BY salary DESC, id ASC` — 多字段排序，DESC 降、ASC 升（默认）。
- `LIMIT 10` — 取前 10 条。
- `LIMIT 20, 10` — 跳过 20 条取 10 条，第 3 页（每页 10 条）就是 `LIMIT 20,10`。

### 索引
- `CREATE INDEX idx_name ON 表(列);` — 建普通索引。
- `CREATE UNIQUE INDEX idx_email ON 表(email);` — 唯一索引。
- `SHOW INDEX FROM 表;` — 看表上的索引。
- `DROP INDEX idx_name ON 表;` — 删索引。

### 事务
- `START TRANSACTION;` 或 `BEGIN;` — 开启事务。
- `COMMIT;` — 提交，改动落地。
- `ROLLBACK;` — 回滚，撤销本次事务的所有改动。
- `SET autocommit = 0;` — 关掉自动提交，必须手动 COMMIT。


---


# 第二部分 · 编程大题模板（30 分）

> 题目来源：CLAUDE 用户提供的题型说明 —— 前端表单 HTML 结构 + SQL 语句 + 三层架构拆分 + JDBC 代码（实践 6 第三题风格）

## 模板一  HTML 表单完整结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>用户注册</title>
</head>
<body>
    <h2>用户注册</h2>
    <form action="/user/register" method="post">
        用户名：<input type="text" name="username" placeholder="请输入用户名"><br><br>
        密码：  <input type="password" name="password"><br><br>
        性别：  <input type="radio" name="gender" value="1" checked>男
                <input type="radio" name="gender" value="2">女<br><br>
        爱好：  <input type="checkbox" name="hobby" value="read">读书
                <input type="checkbox" name="hobby" value="music">音乐
                <input type="checkbox" name="hobby" value="sport">运动<br><br>
        职位：
        <select name="job">
            <option value="">--请选择--</option>
            <option value="1">班主任</option>
            <option value="2">讲师</option>
            <option value="3">学工主管</option>
        </select><br><br>
        头像：<input type="file" name="image"><br><br>
        简介：<textarea name="intro" rows="4" cols="30"></textarea><br><br>
        <input type="submit" value="注册">
        <input type="reset" value="重置">
    </form>
</body>
</html>
```

考点：
- `<form action method>`：action 提交地址，method 通常 post
- 单行文本 `input type="text"`、密码 `password`、单选 `radio`（同组 name 必须一致）、多选 `checkbox`、下拉 `select+option`、多行文本 `textarea`、文件 `file`、提交按钮 `submit`、重置按钮 `reset`
- 表单元素 name 是给后台用的，value 是真正提交的值

---

## 模板二  SQL 语句（DDL + DML + DQL 全套）

### 2.1 建库建表（DDL）

```sql
-- 建库
create database tlias default charset utf8mb4;
use tlias;

-- 部门表
create table dept(
    id          int unsigned primary key auto_increment comment '主键ID',
    name        varchar(10) not null unique             comment '部门名称',
    create_time datetime not null                       comment '创建时间',
    update_time datetime not null                       comment '修改时间'
) comment '部门表';

-- 员工表（含外键到 dept）
create table emp(
    id          int unsigned primary key auto_increment comment 'ID',
    username    varchar(20) not null unique comment '用户名',
    password    varchar(32) default '123456' comment '密码',
    name        varchar(10) not null comment '姓名',
    gender      tinyint unsigned not null comment '性别 1男 2女',
    job         tinyint unsigned comment '职位 1班主任 2讲师 3学工 4教研 5咨询',
    salary      int unsigned comment '工资',
    entry_date  date comment '入职日期',
    dept_id     int unsigned comment '部门ID',
    create_time datetime not null,
    update_time datetime not null,
    constraint fk_emp_dept foreign key (dept_id) references dept(id)
) comment '员工表';
```

### 2.2 增删改（DML）

```sql
-- 插入
insert into emp(username, password, name, gender, job, salary, entry_date, dept_id, create_time, update_time)
values('zhangsan','123','张三',1,2,8000,'2020-01-01',2,now(),now());

-- 批量插入
insert into emp(username,name,gender,create_time,update_time) values
    ('a','张三',1,now(),now()),
    ('b','李四',2,now(),now());

-- 修改
update emp set salary = salary + 100 where id in (2,4,6,8);

-- 删除
delete from emp where id = 30;
```

### 2.3 查询（DQL）—— 必背套路

```sql
-- ① 简单条件 + 别名
select name as '姓名', entry_date as '入职日期' from emp where gender = 2 and job is not null;

-- ② 模糊查询：姓"阮"且 2010 年后入职
select * from emp where name like '阮%' and entry_date > '2010-01-01';

-- ③ 区间查询
select * from emp where entry_date between '2000-01-01' and '2015-01-01';

-- ④ 排序 + 分页
select * from emp where name like '阮%' order by entry_date asc, id desc limit 0, 5;
-- 第 page 页（每页 size 条）通用：limit (page-1)*size, size

-- ⑤ 分组 + 聚合 + having
select job, count(*) as cnt
from emp
where entry_date <= '2015-01-01'
group by job
having count(*) >= 2;

-- ⑥ 内连接（隐式）
select e.name, d.name from emp e, dept d where e.dept_id = d.id;

-- ⑦ 内连接（显式）
select e.name, d.name from emp e inner join dept d on e.dept_id = d.id;

-- ⑧ 左外连接：员工表所有员工 + 对应部门
select e.name, d.name from emp e left join dept d on e.dept_id = d.id;

-- ⑨ 子查询：查询薪资高于平均工资的员工
select * from emp where salary > (select avg(salary) from emp);

-- ⑩ 子查询：教研部所有员工
select * from emp where dept_id = (select id from dept where name = '教研部');
```

---

## 模板三  三层架构拆分（基于 SpringBoot + IOC/DI · 两道题）

> 实践 4 / IOC 作业原型：把单一 Controller 里的所有逻辑按 Controller / Service / Dao 三层拆开，跨层用接口 + 实现类 + `@Autowired` 注入。下面是作业里的两道完整题。

> **统一返回结果类 `Result`**（两道题都用）：

```java
package com.itheima.pojo;

import lombok.Data;

@Data
public class Result {
    private Integer code;     // 1 成功，0 和其它数字为失败
    private String msg;       // 错误信息
    private Object data;      // 数据

    public static Result success() {
        Result r = new Result();
        r.code = 1;
        return r;
    }
    public static Result success(Object object) {
        Result r = new Result();
        r.data = object;
        r.code = 1;
        return r;
    }
    public static Result error(String msg) {
        Result r = new Result();
        r.msg = msg;
        r.code = 0;
        return r;
    }
}
```

---

### 题一  部门管理 `/depts`（读 dept.txt → 返回部门列表）

**Pojo `Dept.java`**

```java
package com.itheima.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Dept {
    private Integer id;
    private String name;
    private LocalDateTime updateTime;
}
```

**Dao 接口 + 实现**

```java
package com.itheima.dao;

import java.util.List;

public interface DeptDao {
    public List<String> list();
}
```

```java
package com.itheima.dao.impl;

import cn.hutool.core.io.IoUtil;
import com.itheima.dao.DeptDao;
import org.springframework.stereotype.Repository;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

@Repository
public class DeptDaoimpl implements DeptDao {
    @Override
    public List<String> list() {
        InputStream in = this.getClass().getClassLoader().getResourceAsStream("dept.txt");
        List<String> lines = IoUtil.readUtf8Lines(in, new ArrayList<String>());
        return lines;
    }
}
```

**Service 接口 + 实现**

```java
package com.itheima.service;

import com.itheima.pojo.Dept;
import java.util.List;

public interface DeptService {
    public List<Dept> list();
}
```

```java
package com.itheima.service.impl;

import com.itheima.dao.DeptDao;
import com.itheima.pojo.Dept;
import com.itheima.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
public class DeptServiceimpl implements DeptService {
    @Autowired
    private DeptDao deptDao;

    @Override
    public List<Dept> list() {
        List<String> lines = deptDao.list();
        List<Dept> deptList = lines.stream().map(line -> {
            String[] parts = line.split(",");
            Integer id = Integer.parseInt(parts[0]);
            String name = parts[1];
            LocalDateTime updateTime = LocalDateTime.parse(parts[2],
                    DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
            return new Dept(id, name, updateTime);
        }).toList();
        return deptList;
    }
}
```

**Controller**

```java
package com.itheima.controller;

import com.itheima.pojo.Dept;
import com.itheima.pojo.Result;
import com.itheima.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class DeptController {
    @Autowired
    private DeptService deptService;

    @RequestMapping("/depts")
    public Result list2() {
        List<Dept> deptList = deptService.list();
        return Result.success(deptList);
    }
}
```

---

### 题二  日志管理 `/logs`（读 log.txt → 返回操作日志列表）

**Pojo `Log.java`**

```java
package com.itheima.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Log {
    private String operateEmpName; // 操作人姓名
    private String operateTime;    // 操作时间
    private String className;      // 操作类名
    private String methodName;     // 操作方法名
    private String costTime;       // 操作耗时
    private String methodParams;   // 操作方法参数
    private String returnValue;    // 操作方法返回值
}
```

**Dao 接口 + 实现**

```java
package com.itheima.dao;

import java.util.ArrayList;

public interface LogDao {
    public ArrayList<String> list();
}
```

```java
package com.itheima.dao.impl;

import cn.hutool.core.io.IoUtil;
import com.itheima.dao.LogDao;
import org.springframework.stereotype.Repository;

import java.io.InputStream;
import java.util.ArrayList;

@Repository
public class LogDaoimpl implements LogDao {
    @Override
    public ArrayList<String> list() {
        InputStream inputStream = this.getClass().getClassLoader().getResourceAsStream("log.txt");
        ArrayList<String> lines = IoUtil.readUtf8Lines(inputStream, new ArrayList<String>());
        return lines;
    }
}
```

**Service 接口 + 实现**

```java
package com.itheima.service;

import com.itheima.pojo.Log;
import java.util.List;

public interface LogService {
    public List<Log> list();
}
```

```java
package com.itheima.service.impl;

import com.itheima.dao.LogDao;
import com.itheima.pojo.Log;
import com.itheima.service.LogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class LogServiceimpl implements LogService {
    @Autowired
    private LogDao logDao;

    @Override
    public List<Log> list() {
        ArrayList<String> lines = logDao.list();
        List<Log> logList = lines.stream().map(line -> {
            String[] parts = line.split(",");
            return new Log(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]);
        }).collect(Collectors.toList());
        return logList;
    }
}
```

**Controller**

```java
package com.itheima.controller;

import com.itheima.pojo.Log;
import com.itheima.pojo.Result;
import com.itheima.service.LogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class LogController {
    @Autowired
    private LogService logService;

    @RequestMapping("/logs")
    private Result list() {
        List<Log> logList = logService.list();
        return Result.success(logList);
    }
}
```

---

**关键注解一览**：

| 注解 | 标识对象 | 所在层 |
|------|---------|--------|
| `@RestController` | 控制器（自带 JSON 序列化）| Controller |
| `@Service` | 业务 Bean | Service |
| `@Repository` | 数据访问 Bean | Dao |
| `@Component` | 通用 Bean | 任何 |
| `@Autowired` | 按类型注入 | 各层间 |
| `@Qualifier("名字")` | 配合 @Autowired 按名注入 | 同类型多实现 |
| `@Resource(name="名")` | JDK 自带、按名注入 | 任何 |
| `@Primary` | 多个实现时指定首选 | Bean 定义处 |

**三层架构答题套路**：
- 包结构：`com.itheima.pojo / dao / dao.impl / service / service.impl / controller`
- 接口和实现分离：`DeptDao` 接口 + `DeptDaoimpl` 实现类（作业里 `impl` 小写无所谓）
- Controller 上 `@RestController` + `@RequestMapping("/xxx")`
- Service 实现上 `@Service`、Dao 实现上 `@Repository`
- 跨层注入用 `@Autowired`，类型按接口（如 `private DeptService deptService`）
- 返回值统一包成 `Result.success(data)`，前端拿 JSON

---

## 模板四  JDBC 预编译查询（实践 6 第三题 · 课件标准写法）

> 题目背景：通过 JDBC 程序，基于预编译 SQL，执行查询，要求查出 4 号记录之前（含 4 号）年龄大于 20 岁的所有用户信息。
> 课件标准写法：`main` 方法直接 `throws Exception`，不写 try-catch-finally，按 5 步顺序往下走。

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class JdbcQueryTest {
    public static void main(String[] args) throws Exception {
        // 1. 注册驱动（MySQL 8.x 必须用 com.mysql.cj.jdbc.Driver）
        Class.forName("com.mysql.cj.jdbc.Driver");

        // 2. 获取连接
        String url = "jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=UTC&useUnicode=true&characterEncoding=utf8";
        String user = "root";
        String password = "123456";
        Connection conn = DriverManager.getConnection(url, user, password);

        // 3. 编写预编译 SQL，获取预编译对象
        String sql = "SELECT id, username, password, name, age FROM user WHERE id <= ? AND age > ?";
        PreparedStatement pstmt = conn.prepareStatement(sql);

        // 4. 绑定参数（下标从 1 开始），执行 SQL
        pstmt.setInt(1, 4);
        pstmt.setInt(2, 20);
        ResultSet rs = pstmt.executeQuery();

        // 5. 处理结果集
        System.out.println("ID\t用户名\t\t密码\t\t姓名\t年龄");
        System.out.println("------------------------------------------------------");
        while (rs.next()) {
            int id = rs.getInt("id");
            String username = rs.getString("username");
            String pwd = rs.getString("password");
            String name = rs.getString("name");
            int age = rs.getInt("age");
            System.out.println(id + "\t" + username + "\t" + pwd + "\t\t" + name + "\t" + age);
        }

        // 6. 释放资源（反向关闭：rs → pstmt → conn）
        rs.close();
        pstmt.close();
        conn.close();
    }
}
```

### JDBC 更新模板（DML 配套 · 实践 6 第二题：硬编码 SQL 更新）

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class JdbcUpdateTest {
    public static void main(String[] args) throws Exception {
        // 1. 注册驱动
        Class.forName("com.mysql.cj.jdbc.Driver");

        // 2. 获取连接
        String url = "jdbc:mysql://localhost:3306/test?useSSL=false&serverTimezone=UTC";
        Connection conn = DriverManager.getConnection(url, "root", "123456");

        // 3. 获取 SQL 执行对象（硬编码 SQL 用 Statement 即可）
        Statement stmt = conn.createStatement();

        // 4. 拼接 SQL，执行更新
        String sql = "UPDATE user SET username='guanyu', password='666888', name='关羽', age=32 WHERE id=4";
        int rows = stmt.executeUpdate(sql);   // DML 用 executeUpdate，返回影响行数
        System.out.println("影响行数：" + rows);

        // 5. 释放资源
        stmt.close();
        conn.close();
    }
}
```

> 注：实践 6 第三题用 `PreparedStatement` 预编译 + `?` 占位 + `setXxx` 绑参；第二题用 `Statement` 拼接固定 SQL。考试照这两段背就够。

**JDBC 五步骤（必背）**：
1. 注册驱动 `Class.forName("com.mysql.cj.jdbc.Driver")`
2. 获取连接 `DriverManager.getConnection(url, user, password)`
3. 获取 SQL 执行对象 `conn.prepareStatement(sql)` 或 `conn.createStatement()`
4. 执行 SQL（查询 `executeQuery()` 返回 `ResultSet`；增删改 `executeUpdate()` 返回 `int`）
5. 释放资源（反向关闭：`rs → pstmt → conn`）

**JDBC 三个关键点**：
1. 驱动类：MySQL 8.x → `com.mysql.cj.jdbc.Driver`（带 `cj`！）；MySQL 5.x → `com.mysql.jdbc.Driver`
2. 占位符 `?` 顺序与 `setXxx` 的下标一一对应，下标**从 1 开始**
3. URL 末尾参数 `useSSL=false&serverTimezone=UTC` 不能少，否则会报时区/SSL 警告

**`PreparedStatement` vs `Statement`**：
- `Statement`：直接拼 SQL 字符串，**有 SQL 注入风险**（如 `' or '1'='1`），只适合写死的 SQL
- `PreparedStatement`：预编译 + `?` 占位 + 参数转义，**防注入 + 性能高**（DB 缓存 SQL 模板）
- 企业项目一律用 `PreparedStatement`

---


# 第三部分 · 简答题题库（20 题分章节·含答案）

> 考试出 8 题（×5 分 = 40 分）。下面每题都按"答：" 顶格 + 分项要点 写，禁用 AI 套话。

## 前端 5 题

### 1. 什么是 C/S 模式，什么是 B/S 模式，试简述两种模式各层的作用并比较其优缺点。

答：
- **C/S（Client/Server）客户机-服务器模式**：客户端是专门安装的软件（如 QQ、微信），服务端提供数据和服务。客户端层负责界面展示和部分业务，服务端层负责数据存储和核心业务。优点是体验流畅、对网速要求低；缺点是客户端要装、要升级、跨平台麻烦。
- **B/S（Browser/Server）浏览器-服务器模式**：客户端就是浏览器，所有逻辑放服务端。表示层 = 浏览器、业务层 = Web 服务器、数据层 = 数据库。优点是无需安装、跨平台、维护方便（只升级服务端）；缺点是体验受网速影响，早期不如 C/S。本课程就是 B/S。

### 2. 什么是静态网站？什么是动态网站？试比较它们之间的区别？

答：
- **静态网站**：服务端返回的就是事先写好的 HTML 文件，每个用户看到的内容一样，文件内容由开发者手写，不会变。代表：纯 HTML/CSS/JS 页面。
- **动态网站**：服务端根据用户请求、数据库内容实时生成 HTML 返回，不同用户、不同时刻看到的内容可能不同。代表：JSP/Servlet、SpringBoot 项目。
- **区别**：① 静态返回的是死文件，动态是程序生成；② 静态不能交互（不能查库、登录），动态可以；③ 静态部署简单，动态需要服务器和数据库。

### 3. 简述 JavaScript 变量的命名规范？

答：
- 只能由**字母、数字、下划线 `_`、美元符号 `$`** 组成。
- **不能以数字开头**。
- **不能使用关键字和保留字**（如 var、let、function、return 等）。
- **大小写敏感**：`name` 和 `Name` 是两个变量。
- 推荐用**驼峰命名**（如 `userName`），常量用全大写下划线（如 `MAX_AGE`）。

### 4. 简述 JavaScript 和 Java 的区别。

答：
- **类型不同**：JS 是脚本语言、解释执行、运行在浏览器；Java 是编译型语言、跑在 JVM 上。
- **类型系统不同**：JS 是**弱类型**，变量类型由值决定可以变；Java 是**强类型**，变量声明时就定死类型。
- **面向对象方式不同**：JS 基于原型 prototype；Java 基于类 class。
- **运行环境不同**：JS 主要在浏览器客户端跑（也可以 Node.js）；Java 跑在服务端、桌面、Android 上。
- **关系**：除了名字像，**两者没有直接关系**，JS 是为了营销才取这个名。

### 5. 加载 CSS 样式的方式有哪些？如何使用？

答：三种方式：
- **行内式**：直接在 HTML 标签的 `style` 属性里写。例如 `<p style="color:red;">文字</p>`。优先级最高，但维护性差，不推荐。
- **内嵌式（内部样式）**：在 `<head>` 标签里用 `<style>` 包裹 CSS 规则。例如 `<style>p{color:red;}</style>`。适合单页面使用。
- **外部式（外联样式）**：CSS 写在独立的 `.css` 文件里，HTML 通过 `<link rel="stylesheet" href="xx.css">` 引入。**最推荐**，能复用、易维护、可缓存。

## CH3 Maven 简答 3 题

### 6. Maven 中有哪几类仓库？依赖查找顺序是什么？什么是坐标，坐标由哪几部分组成？

答：
- **三类仓库**：① 本地仓库（自己机器上的目录，默认 `~/.m2/repository`）；② 远程仓库（公司私服或国内镜像如阿里云）；③ 中央仓库（Maven 团队维护的全球唯一仓库 repo1.maven.org）。
- **查找顺序**：**本地仓库 → 远程仓库（私服） → 中央仓库**。本地有就直接用，没有才往上找，下载下来后存进本地仓库下次复用。
- **坐标**：定位一个 Maven 项目/jar 包的唯一标识，由三部分组成：① `groupId`（组织名，一般用域名反写如 `org.springframework`）；② `artifactId`（模块名/jar 包名）；③ `version`（版本号）。

### 7. Maven 的生命周期分几套？核心 5 个阶段是什么？

答：
- **三套生命周期**：① clean（清理）；② default（默认构建）；③ site（站点生成）。同一套内阶段有先后顺序，**后面的阶段会自动执行前面的阶段**。
- **核心 5 个阶段**：
  - `clean`：移除上次构建生成的文件（清空 target 目录）。
  - `compile`：编译 src/main/java 下的源代码。
  - `test`：跑 src/test/java 下的 JUnit 单元测试。
  - `package`：把编译结果打成 jar/war 包。
  - `install`：把项目安装到本地仓库，供其他项目依赖。

### 8. Maven 的依赖范围是做什么用的？常见取值有哪些？如何设置？

答：
- **作用**：`<scope>` 标签控制依赖在哪些阶段可用（主程序 / 测试程序 / 打包）。
- **常见取值**：
  - `compile`（默认）：主程序、测试程序都能用，参与打包。代表：Spring 核心包。
  - `test`：只在测试程序可用，不参与打包。代表：JUnit。
  - `provided`：主、测都能用，**不参与打包**（容器已经提供）。代表：servlet-api。
  - `runtime`：主程序编译时不用，运行时和测试时才需要。代表：JDBC 驱动。
- **设置方法**：在 `<dependency>` 标签里加 `<scope>test</scope>` 即可。

## CH4 Web 简答 5 题

### 9. HTTP 的状态码分几类？分别表示什么？常见状态码有哪些？

答：分**五大类**：
- **1xx 信息性**：请求已接收、继续处理。
- **2xx 成功**：请求被成功处理。如 `200 OK` 请求成功。
- **3xx 重定向**：需要进一步操作才能完成。如 `302 Found` 临时重定向、`304 Not Modified` 资源未修改用缓存。
- **4xx 客户端错误**：请求有问题。如 `400 Bad Request` 语法错、`404 Not Found` 资源不存在、`405 Method Not Allowed` 请求方式不支持。
- **5xx 服务端错误**：服务器自己挂了。如 `500 Internal Server Error` 服务端异常。

### 10. SpringBoot 中为什么要对代码进行拆分？三层架构每层的作用是什么？

答：
- **为什么拆分**：业务一复杂代码全堆在 Controller 里会乱、难维护、不能复用、改一处碰处处。按**单一职责原则**拆开后可读性、复用性、可扩展性都好。
- **三层及作用**：
  - **Controller（控制层）**：接收前端请求、解析参数，调 Service 处理，把结果响应回前端。
  - **Service（业务逻辑层）**：处理具体业务规则、组合 Dao 操作、做事务管理。
  - **Dao（数据访问层）**：和数据库直接打交道，执行 SQL 增删改查。
- **调用方向**：Controller → Service → Dao（自上而下单向调用）。

### 11. SpringBoot 中如何做到分层解耦？IOC 和 DI 的核心思想是什么？

答：
- **分层解耦做法**：① 各层之间只依赖**接口**而非实现类；② 由 Spring 容器统一创建和管理对象（**IOC**）；③ 用 `@Autowired` 让容器把依赖**自动注入**进来（**DI**），不用手动 `new`。
- **IOC（控制反转）**：原本程序员 `new` 对象的控制权转交给 Spring 容器，容器创建并管理的对象叫 Bean。
- **DI（依赖注入）**：程序运行时需要某个对象，容器自动把它"塞"进来，开发者不用关心对象怎么来的。
- **效果**：换实现类只要改注解，业务代码一行不动。

### 12. Spring 中声明 Bean 的注解有哪些？使用了这个注解 Bean 就一定会生效吗？

答：
- **四个注解**：
  - `@Component`：通用，归类不明确时用。
  - `@Controller`：控制层（Web 接口）。
  - `@Service`：业务层。
  - `@Repository`：数据访问层。
  - 还有 `@RestController` = `@Controller` + `@ResponseBody`，方法返回值自动转 JSON。
- **不一定生效**：注解要被 `@ComponentScan` 扫描到才生效。`@SpringBootApplication` 默认扫描**启动类所在包及其子包**，所以业务类必须放在启动类的同包或子包下，否则不会被识别。

### 13. 依赖注入的注解是什么？多个 Bean 对象时如何注入？

答：
- **依赖注入注解**：
  - `@Autowired`：Spring 提供，**默认按类型注入**。三种用法：属性注入、构造注入（推荐）、setter 注入。
- **同类型多个 Bean 时**：
  - `@Qualifier("beanName")`：配合 `@Autowired` 按名字指定。
  - `@Resource(name="beanName")`：JDK 自带的，按名字注入，相当于上面两个的合体。
  - `@Primary`：在某个实现类上加这个注解抬高优先级，`@Autowired` 优先选它。

## CH5 MySQL 简答 3 题

### 14. char 与 varchar 的区别？设计表时如何选择？

答：
- **char(n)** 是**定长**字符串：占用 n 个字符，不够补空格，多了截断。优点是查询性能好（每行长度固定，定位快）；缺点是存短数据浪费空间。
- **varchar(n)** 是**变长**字符串：最多 n 个字符，按实际长度存。优点是省空间；缺点是查询时要算长度，性能略低于 char。
- **选择原则**：长度**固定**的字段（手机号 11 位、身份证 18 位、性别 'M'/'F'）用 `char`；长度**变化大**的字段（姓名、地址、备注）用 `varchar`。

### 15. DQL 分组查询时，where、group by、having 的执行顺序？where 和 having 区别？

答：
- **执行顺序**：**FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT**。先 where 过滤行，再分组，再 having 过滤组。
- **where 和 having 的区别**：
  - **过滤时机不同**：where 在**分组前**过滤行；having 在**分组后**过滤组。
  - **能否用聚合函数**：where 后**不能**用 `COUNT/SUM/AVG/MAX/MIN`；having 后**可以**用。
  - **作用对象不同**：where 针对单条记录；having 针对分组结果。
  - **执行效率**：where 在分组前过滤掉的行不参与分组，效率更高，能用 where 就别用 having。

### 16. 数据库表结构设计时有哪几种多表关系？如何维护？

答：三种关系：
- **一对一**：如用户基本信息和用户详情。在任一方加外键 + 唯一约束 UNIQUE，让外键值不重复。
- **一对多**：如部门和员工，一个部门有多个员工。**在多的一方加外键**（emp 表加 `dept_id` 指向 `dept(id)`）。
- **多对多**：如学生和课程。必须**建第三张中间表**，中间表至少有两个外键，分别指向两边主键。
- **维护方式**：用 `FOREIGN KEY` 外键约束。语法：`CONSTRAINT fk_emp_dept FOREIGN KEY(dept_id) REFERENCES dept(id);`。

## CH6 JDBC 简答 4 题

### 17. 什么是 JDBC？它在访问数据库时起什么作用？

答：
- **JDBC**（Java DataBase Connectivity）是 Sun 公司定义的一套用 Java 操作关系型数据库的**规范/API**，本质是一组接口。
- **作用**：① 提供统一的 Java 接口让程序连接和操作各种数据库；② 屏蔽不同数据库厂商的差异——Sun 只定义接口，各家厂商（MySQL、Oracle、SQL Server）提供自己的驱动 jar 包实现这些接口；③ 同一套 Java 代码换个驱动就能换数据库。
- **地位**：是 Java 操作数据库的**最底层、最基础**的技术，MyBatis、Hibernate 等高级框架都是建立在 JDBC 之上的封装。

### 18. 简述 JDBC 连接数据库的基本步骤。

答：固定 6 步：
- **① 注册驱动**：`Class.forName("com.mysql.cj.jdbc.Driver");`（MySQL 8.x 必须用带 cj 的）
- **② 获取连接**：`Connection conn = DriverManager.getConnection(url, user, password);`
- **③ 获取 Statement / PreparedStatement** 对象用来执行 SQL
- **④ 执行 SQL**：查询用 `executeQuery()` 返回 `ResultSet`；增删改用 `executeUpdate()` 返回受影响行数
- **⑤ 处理结果集**：`while(rs.next()){ rs.getString(...); rs.getInt(...); }`
- **⑥ 释放资源**：按 ResultSet → Statement → Connection **倒序关闭**

### 19. MyBatis 的映射配置文件规范？什么时候用注解、什么时候用 XML？

答：
- **XML 映射规范**：
  - 文件名与 Mapper 接口**同名同包**（resources 下镜像目录）。
  - `<mapper namespace="...">` 的 namespace 必须是 Mapper 接口的**全限定类名**。
  - `<select>/<insert>/<update>/<delete>` 的 `id` 必须和接口方法名**一致**。
  - 同一方法注解和 XML **只能保留一种**，否则报错。
- **何时用注解**：SQL **简单短小**（一两行能写完）、动态成分少时用注解，写在接口上 `@Select`/`@Insert`/`@Update`/`@Delete`，更直观。
- **何时用 XML**：SQL **复杂或动态**（带 if/foreach 标签、多表 join、长 SQL）用 XML，集中维护、可读性好。

### 20. MyBatis 中 `#{}` 与 `${}` 的区别？推荐用哪个？为什么？

答：
- **`#{}`**：**预编译占位符**。会被翻译成 JDBC 的 `?`，再调 `PreparedStatement.setXxx()` 赋值。**自动转义参数**，能防 SQL 注入。
- **`${}`**：**字符串直接拼接**。把参数值直接拼到 SQL 字符串里，**有 SQL 注入风险**。
- **示例**：`where name = #{name}` 安全；`where name = '${name}'` 容易被注入。
- **推荐用 `#{}`**。原因：① 防 SQL 注入；② SQL 模板在数据库端缓存，重复执行性能高。
- **`${}` 的使用场景**：只有需要动态拼**表名、列名、order by 字段**这种结构性内容时才用，**且参数必须自己严格校验**。

---


# 第四部分 · 判断题练习（10 道·含答案）

> 考试出 10 道（×1 分 = 10 分）。下面是按知识点出的高频判断题，对的打 ✓，错的打 ✗。

1. HTML 中 `<ul>` 和 `<ol>` 的子标签只能是 `<li>`，不能把 `<ul>` 直接套在 `<ul>` 里。
   **答：✓**。子列表必须嵌在 `<li>` 内部。

2. CSS 选择器优先级：ID 选择器 > 类选择器 > 元素选择器。
   **答：✓**。同等情况下 ID 优先级最高。

3. JavaScript 是一种**强类型**的编程语言。
   **答：✗**。JS 是**弱类型**，变量类型由值决定且可以变。

4. Vue 中 `v-if` 和 `v-show` 完全等价，作用一样。
   **答：✗**。`v-if` 不满足条件时元素不渲染到 DOM；`v-show` 用 `display:none` 切换，元素一直在 DOM 里。

5. Maven 执行 `mvn package` 时会自动执行前面的 compile 和 test 阶段，但不会执行 clean。
   **答：✓**。package 属于 default 套，compile/test 都会触发；clean 属于不同生命周期套。

6. HTTP 协议是**有状态**的协议，服务端会自动记住上次请求的信息。
   **答：✗**。HTTP 是**无状态**协议，每次请求-响应都是独立的，需要 Cookie/Session 才能维持状态。

7. 在 SpringBoot 中 `@RestController` 等价于 `@Controller + @ResponseBody`，方法返回值会自动转成 JSON。
   **答：✓**。

8. MySQL 中 `where` 后面可以使用聚合函数（如 `COUNT`、`SUM`）。
   **答：✗**。`where` 后**不能**用聚合函数，要用聚合函数过滤分组结果得用 `having`。

9. JDBC 中 `PreparedStatement` 比 `Statement` 安全的根本原因是它把参数当成字符串转义，从而防止了 SQL 注入。
   **答：✓**。同时还有性能优势：DB 缓存 SQL 模板，重复执行不重新编译。

10. MyBatis 中 `${name}` 和 `#{name}` 都会被翻译成 JDBC 的 `?` 占位符。
    **答：✗**。只有 `#{name}` 会翻译成 `?`（预编译）；`${name}` 是字符串直接拼接，有注入风险。

---


# 第五部分 · 选择题题库（含答案）

> 考试出 20 题（×1 分 = 20 分）。题源：① 老师发布的前端选择题复习范围 15 题（最重要，最可能直接出原题）；② 前端补充复习题 30 题；③ 后端复习题（实践 3/4/5/6 各 15 题）。

## A. 前端选择题复习范围 15 题（最重要，几乎是原题考）

1. 下列动态网页和静态网页的根本区别描述**错误**的是？
   - A. 静态网页服务器端返回的 HTML 文件是事先存储好的
   - B. 动态网页服务器端返回的 HTML 文件是程序生成的
   - C. 静态网页文件里只有 HTML 标记，没有程序代码
   - D. **动态网页中只有程序，不能有 HTML 代码** ✗
   - **答案：D**。动态网页里也可以有 HTML 代码，由程序生成。

2. 下列说法**错误**的是？
   - A. 网站一般拥有固定的域名 ✓
   - B. 通信协议包括 HTTP、FTP、Telnet 和 Mailto 等协议
   - C. WWW，即万维网，是一个基于超级文本的信息查询工具 ✓
   - D. HTML 是一种用来制作网络中超级文本文档的简单标记语言 ✓
   - **答案：B**。Mailto 是 URL 协议方案，不算严格意义上的通信协议。

3. B/S 应用程序体系结构可分为三层，**不属于**这三层的是？
   - A. 表示层  B. 业务层  C. 数据访问层  D. **网络链接层**
   - **答案：D**。三层是表示层、业务层、数据层。

4. WEB 标准的制定者是？
   - A. 微软  B. **W3C（万维网联盟）**  C. Netscape  D. IBM
   - **答案：B**。

5. 下面描述**错误**的是？
   - A. HTML 文件必须由 `<html>` 开头，`</html>` 标记结束
   - B. 文档头信息包含在 `<head>` 与 `</head>` 之间
   - C. **在 `<head>` 和 `</head>` 之间可以包含 `<title>` 和 `<body>` 等信息** ✗
   - D. 文档体包含在 `<body>` 和 `</body>` 标记之间
   - **答案：C**。`<body>` 在 `<head>` 之外，不能放在 `<head>` 里。

6. （  ）是标题标记。
   - A. `<p>`  B. `<br>`  C. `<hr>`  D. **`<hn>`**（即 h1~h6）
   - **答案：D**。

7. 以下有关列表的说法中，**错误**的是？
   - A. 有序列表和无序列表可以互相嵌套
   - B. 指定嵌套列表时，也可以具体指定项目符号或编号样式
   - C. 无序列表应使用 UL 和 LI 标记符进行创建
   - D. **在创建列表时，LI 标记符的结束标记符不可省略** ✗
   - **答案：D**。`</li>` 实际可以省略。

8. 以下有关表单的说明中，**错误**的是？
   - A. 表单通常用于搜集用户信息
   - B. 在 FORM 标记符中使用 action 属性指定表单处理程序的位置
   - C. **表单中只能包含表单控件，而不能包含其他诸如图片之类的内容** ✗
   - D. 在 FORM 标记符中使用 method 属性指定提交表单数据的方法
   - **答案：C**。表单内可以放任意 HTML 内容（图片、文字等）。

9. 以下说法**正确**的是？
   - A. 在 IMG 标记符中使用 align 属性，可以控制图象在页面中的对齐
   - B. **在 IMG 标记符中使用 align 属性，可以控制图象与文字的环绕效果** ✓
   - C. 在 IMG 标记符中使用 valign 属性，可以控制图象与周围内容的垂直对齐
   - D. 在 IMG 标记符中使用 valign 属性，可以控制图象与周围内容的水平对齐
   - **答案：B**。`<img>` 没有 `valign` 属性，`align` 主要控制图文环绕。

10. JavaScript 是一门（  ）语言。
    - A. 强类型编程语言
    - B. **运行在客户端弱类型编程语言** ✓
    - C. 运行在服务端
    - D. 浏览器不能运行
    - **答案：B**。

11. `<script>` 通常放在（  ）标签中。
    - A. `<body>`  B. **`<head>`**  C. `<header>`  D. `<foot>`
    - **答案：B**。但实际开发推荐放 `<body>` 底部以避免阻塞渲染（如果老师按 PPT 标准答案就选 B）。

12. 在 JavaScript 中，关于 `alert()` 和 `confirm()` 方法的说法**正确**的是？
    - A. **`alert()` 和 `confirm()` 都是 window 对象的方法** ✓
    - B. 功能相同
    - C. alert() 显示带"确定"和"取消"
    - D. confirm() 显示只有"确定"
    - **答案：A**。alert 只有"确定"，confirm 有"确定/取消"，B/C/D 描述都反了。

13. 分析下面 JavaScript 代码段：
    ```js
    a = new Array(2,3,4,5,6); sum = 0;
    for (i = 1; i < a.length; i++) sum += a[i];
    document.write(sum);
    ```
    输出结果是？
    - A. 20  B. **18**  C. 14  D. 12
    - **答案：B**。i=1 开始累加 a[1]+a[2]+a[3]+a[4] = 3+4+5+6 = **18**。

14. 如果要在不同的网页中应用相同的样式表定义，应该？
    - A. 直接在 HTML 元素中定义
    - B. 在 `<head>` 中定义
    - C. **通过一个外部样式表文件定义** ✓
    - D. 以上都可以
    - **答案：C**。外部式样式复用性最好。

15. 样式表定义 `.outer { background-color: yellow }` 表示？
    - A. 网页中某一个 id 为 outer 的元素的背景色
    - B. **网页中含有 class="outer" 元素的背景色** ✓
    - C. 网页中元素名为 outer 的元素背景色
    - D. 以上任意一个
    - **答案：B**。`.outer` 是类选择器。

## B. 前端补充复习题 1（15 题 · 含完整题干）

**1. 用 HTML 编写的网页文档在保存时应该以（  ）为扩展名。**
- A. DOC   B. WEB   C. HTML   D. PPT
- **答案：C**。HTML 文件扩展名 `.html` 或 `.htm`。

**2. 下列动态网页和静态网页的根本区别描述错误的是（  ）。**
- A. 静态网页服务器端返回的 HTML 文件是事先存储好的
- B. 动态网页服务器端返回的 HTML 文件是程序生成的
- C. 静态网页文件里只有 HTML 标记，没有程序代码
- D. 动态网页中只有程序，不能有 HTML 代码
- **答案：D**。动态网页里也有 HTML，只是由程序拼出来再返回。

**3. 下列说法错误的是（  ）。**
- A. 网站一般拥有固定的域名
- B. 通信协议包括 HTTP、FTP、Telnet 和 Mailto 等协议
- C. WWW，即万维网，是一个基于超级文本的信息查询工具
- D. HTML 是一种用来制作网络中超级文本文档的简单标记语言
- **答案：B**。Mailto 是 URL 协议方案不是通信协议；常见通信协议是 HTTP/FTP/Telnet。

**4. B/S 应用程序体系结构可分为三层，不属于这三层的是（  ）。**
- A. 表示层   B. 业务层   C. 数据访问层   D. 网络链接层
- **答案：D**。三层是表示层、业务层、数据访问层。

**5. WEB 标准的制定者是（  ）。**
- A. 微软   B. W3C（万维网联盟）   C. Netscape（网景公司）   D. IBM 公司
- **答案：B**。

**6. 下面描述错误的是（  ）。**
- A. HTML 文件必须由 `<html>` 开头，`</html>` 标记结束
- B. 文档头信息包含在 `<head>` 与 `</head>` 之间
- C. 在 `<head>` 和 `</head>` 之间可以包含 `<title>` 和 `<body>` 等信息
- D. 文档体包含在 `<body>` 和 `</body>` 标记之间
- **答案：C**。`<body>` 在 `<head>` 之外，不能塞进 head。

**7. （  ）是标题标记。**
- A. `<p>` 标记   B. `<br>` 标记   C. `<hr>` 标记   D. `<hn>`
- **答案：D**。`<hn>` 泛指 `h1`~`h6`，没有 h7。

**8. 通常网页的首页被称为（  ）。**
- A. 主页   B. 网页   C. 页面   D. 网址
- **答案：A**。首页就是主页（home page）。

**9. 下列不属于 Macromedia 公司产品的是（  ）。**
- A. Dreamweaver   B. Fireworks   C. Flash   D. Frontpage
- **答案：D**。Frontpage 是微软的，前三个是 Macromedia（后被 Adobe 收购）。

**10. 属于网页制作平台的是（  ）。**
- A. photoshop   B. flash   C. dreamweaver   D. cuteFTP
- **答案：C**。Dreamweaver 是专门做网页；Photoshop 做图、Flash 做动画、CuteFTP 是文件传输。

**11. 以下有关列表的说法中，错误的是（  ）。**
- A. 有序列表和无序列表可以互相嵌套
- B. 指定嵌套列表时，也可以具体指定项目符号或编号样式
- C. 无序列表应使用 UL 和 LI 标记符进行创建
- D. 在创建列表时，LI 标记符的结束标记符不可省略
- **答案：D**。`</li>` 在 HTML 里实际可以省略。

**12. 以下关于 FONT 标记符的说法中，错误的是（  ）。**
- A. 可以使用 color 属性指定文字颜色
- B. 可以使用 size 属性指定文字大小
- C. 指定字号时可以使用 1~7 的数字
- D. 语句 `<FONT size="+2">这里是 2 号字</FONT>` 将使文字以 2 号字显示
- **答案：D**。`size="+2"` 是相对当前字号增加 2 级，不是直接 2 号字。

**13. 以下有关表单的说明中，错误的是（  ）。**
- A. 表单通常用于搜集用户信息
- B. 在 FORM 标记符中使用 action 属性指定表单处理程序的位置
- C. 表单中只能包含表单控件，而不能包含其他诸如图片之类的内容
- D. 在 FORM 标记符中使用 method 属性指定提交表单数据的方法
- **答案：C**。表单里可以放图片、文字、任意 HTML 内容。

**14. 要创建一个左右框架，右边框架宽度是左边框架的 3 倍，以下 HTML 语句正确的是（  ）。**
- A. `<FRAMESET cols="*, 2*">`
- B. `<FRAMESET cols="*, 3*">`
- C. `<FRAMESET rows="*, 2*">`
- D. `<FRAMESET rows="*, 3*">`
- **答案：B**。左右分用 cols（列），右边是左边 3 倍写 `*, 3*`；rows 是行（上下分）。

**15. 以下说法中，正确的是（  ）。**
- A. 在 IMG 标记符中使用 align 属性，可以控制图象在页面中的对齐
- B. 在 IMG 标记符中使用 align 属性，可以控制图象与文字的环绕效果
- C. 在 IMG 标记符中使用 valign 属性，可以控制图象与周围内容的垂直对齐
- D. 在 IMG 标记符中使用 valign 属性，可以控制图象与周围内容的水平对齐
- **答案：B**。`<img>` 没有 valign 属性；align 控制图文环绕（left/right/top/bottom）。

## C. 前端补充复习题 2（10 题 · 含完整题干）

**1. JavaScript 是一门（  ）语言。**
- A. 强类型编程语言   B. 运行在客户端弱类型编程语言   C. 运行在服务端   D. 浏览器不能运行
- **答案：B**。JS 跑在浏览器端、弱类型。

**2. `<script>` 通常放在（  ）标签中。**
- A. `<body>`   B. `<head>`   C. `<header>`   D. `<foot>`
- **答案：B**。一般放 head 里；现代实践也允许放 body 末尾。

**3. 在 JavaScript 中，关于 alert() 和 confirm() 方法的说法正确的是（  ）。**
- A. alert() 和 confirm() 都是 window 对象的方法
- B. alert() 和 confirm() 方法功能相同
- C. alert() 方法的功能是显示一个带有"确定"和"取消"按钮的对话框
- D. confirm() 方法的功能是显示一个带有"确定"按钮的对话框
- **答案：A**。两者都是 window 的方法；alert 只有确定，confirm 有确定+取消。

**4. 要将页面的状态栏中显示"已经选中该文本框"，下列 JavaScript 语句正确的是（  ）。**
- A. `window.status="已经选中该文本框"`
- B. `document.status="已经选中该文本框"`
- C. `window.screen="已经选中该文本框"`
- D. `document.screen="已经选中该文本框"`
- **答案：A**。状态栏属于 window 对象的 status 属性。

**5. 分析下面的 JavaScript 代码段：**
```js
a = new Array(2,3,4,5,6);
sum = 0;
for(i=1; i<a.length; i++) sum += a[i];
document.write(sum);
```
**输出结果是（  ）。**
- A. 20   B. 18   C. 14   D. 12
- **答案：B**。i 从 1 开始（不是 0），累加 `a[1]+a[2]+a[3]+a[4]` = 3+4+5+6 = 18。

**6. CSS 是（  ）的缩写。**
- A. Colorful Style Sheets   B. Computer Style Sheets   C. Cascading Style Sheets   D. Creative Style Sheets
- **答案：C**。层叠样式表。

**7. 如果要在不同的网页中应用相同的样式表定义，应该（  ）。**
- A. 直接在 HTML 的元素中定义样式表
- B. 在 HTML 的 `<head>` 标记中定义样式表
- C. 通过一个外部样式表文件定义样式表
- D. 以上都可以
- **答案：C**。外部样式表（外联 `<link>`）才能跨页面共用。

**8. 样式表定义 `.outer {background-color:yellow}` 表示（  ）。**
- A. 网页中某一个 id 为 outer 的元素的背景色是黄色的
- B. 网页中含有 class="outer" 元素的背景色是黄色的
- C. 网页中元素名为 outer 元素的背景色是黄色的
- D. 以上任意一个都可以
- **答案：B**。`.` 是类选择器，对应 `class="outer"`。

**9. 下列选项中不属于 CSS 文本属性的是（  ）。**
- A. font-size   B. text-transform   C. text-align   D. line-height
- **答案：A**。`font-size` 是字体属性（font-*）；text-* 才是文本属性。

**10. 下面关于 CSS 的说法不正确的是（  ）。**
- A. CSS 可以控制网页背景图片
- B. margin 属性的属性值可以是百分比
- C. 字体大小的单位可以是 em
- D. 1em 等于 18 像素
- **答案：D**。1em 等于父元素当前字号，不固定；默认浏览器字号通常是 16px 而非 18px。

## D. 实践 3 Maven 选择题（15 题 · 含完整题干）

**1. 下列关于 Maven 的描述，错误的是？**
- A. Maven 是 Apache 旗下的开源项目，用于管理和构建 Java 项目
- B. Maven 提供了标准、统一的项目结构，解决了不同 IDE 创建项目结构差异的问题
- C. Maven 只能管理依赖的 JAR 包，不能完成项目的编译、测试、打包等构建操作
- D. Maven 基于项目对象模型（POM）的概念，通过 pom.xml 配置管理项目
- **答案：C**。Maven 既能管依赖也能做编译、测试、打包、部署，三大作用都有。

**2. Maven 项目中，用于存放项目源代码和资源文件的主目录是？**
- A. src/test/java   B. src/main/resources   C. src/main   D. target
- **答案：C**。`src/main` 是主目录，下面再分 `java`（代码）和 `resources`（配置）。

**3. 在 Maven 的 pom.xml 中，用于定位资源的唯一标识被称为坐标，以下哪个不属于坐标的组成部分？**
- A. groupId   B. artifactId   C. version   D. scope
- **答案：D**。坐标三要素 GAV：`groupId`、`artifactId`、`version`，scope 是依赖范围。

**4. 关于 Maven 仓库的说法，以下正确的是？**
- A. 本地仓库默认存储中央仓库的所有 jar 包，不需要配置
- B. 查找依赖的顺序为：中央仓库 → 本地仓库 → 远程仓库（私服）
- C. 若本地仓库没有对应依赖，且没有配远程仓库，则会直接从中央仓库下载到本地并引用
- D. 远程仓库（私服）必须由 Maven 官方搭建，个人无法搭建
- **答案：C**。查找顺序是本地 → 私服 → 中央，没配私服就直接走中央。

**5. 在 Maven 的 settings.xml 中，配置阿里云镜像仓库的作用是？**
- A. 修改本地仓库路径   B. 加速依赖下载，替代默认中央仓库访问   C. 设置 JDK 编译版本   D. 配置项目部署的服务器地址
- **答案：B**。中央仓库在国外，配阿里云镜像就是为了下得快。

**6. 关于 Maven 依赖传递的理解，下列说法正确的是？**
- A. 依赖传递会导致项目引入大量不必要的 jar 包，且无法排除
- B. 如果 A 依赖 B，B 依赖 C，则 A 项目中会自动包含 C 依赖（传递性）
- C. Maven 依赖传递只对 test 范围的依赖有效
- D. 排除依赖需要使用 `<exclude>` 标签并指定版本号
- **答案：B**。这就是传递依赖的定义，排除用 `<exclusions>` + `<exclusion>`。

**7. 以下哪个 Maven 生命周期阶段会执行编译、测试并且将项目打包成 JAR 包？**
- A. compile   B. test   C. package   D. install
- **答案：C**。`package` 会把前面的 compile、test 都带跑一遍再打包。

**8. 在 Maven 中执行 `mvn clean install` 命令，以下描述正确的是？**
- A. 只会执行 clean 和 install 两个阶段，中间的 compile、test 不会执行
- B. 先执行 clean 清理，再执行 install，由于 install 属于 default 生命周期，其前面的 compile、test、package 等阶段会依次执行
- C. 该命令会报错，因为 clean 和 install 属于不同的生命周期不能同时执行
- D. 只会执行 install，clean 不会生效
- **答案：B**。同一行能写多个不同生命周期套的命令，install 会触发前置阶段。

**9. 关于单元测试框架 JUnit，在 Maven 项目中配置依赖时，通常将 scope 设置为 test，其作用是什么？**
- A. 使 JUnit 依赖在主程序代码中也可以使用
- B. 让 JUnit 只在测试代码（src/test 目录）中有效，且不会打包到最终产物中
- C. 限制 JUnit 仅在打包时生效，运行时无效
- D. 使 JUnit 参与项目的部署
- **答案：B**。test 范围就是限定在测试用，不进最终 jar。

**10. 在 JUnit 中，若希望某个方法在所有测试方法执行之前只运行一次（静态初始化），应该使用哪个注解？**
- A. @BeforeEach   B. @BeforeAll   C. @AfterEach   D. @ParameterizedTest
- **答案：B**。`@BeforeAll` 只跑一次，方法必须是 `static`。

**11. Maven 中用于移除上一次构建生成文件的命令（生命周期）是？**
- A. clean   B. compile   C. test   D. package
- **答案：A**。`mvn clean` 删 `target` 目录。

**12. 当我们在 pom.xml 中引入依赖后，右侧 Maven 面板仍然报红，最有可能的原因是？**
- A. 没有配置 JDK 环境变量
- B. 由于网络原因依赖下载不完整，本地仓库中存在 .lastUpdated 文件，需要删除后重新加载
- C. 没有编写 main 方法
- D. 项目名称不符合规范
- **答案：B**。下载失败留下 `.lastUpdated`，删掉重新 reload 就好。

**13. 以下关于 Maven 依赖范围（scope）的说法，错误的是？**
- A. compile（默认）范围在主程序、测试程序中都有效，且会参与打包
- B. provided 范围表示容器已提供该依赖，不会参与打包但参与编译和测试
- C. runtime 范围只在运行时和测试运行时有效，编译主程序不需要
- D. test 范围在主程序 main 目录下可以使用该依赖
- **答案：D**。test 范围在 `src/main` 下**不能**用，只在 `src/test` 下能用。

**14. 在 Maven 中，如果需要排除传递性依赖中的某个 jar 包，正确的配置方式是？**
- A. 在 `<dependency>` 中使用 `<scope>exclude</scope>`
- B. 使用 `<exclusions>` 标签，内部嵌套 `<exclusion>` 指定 groupId 和 artifactId
- C. 直接在 pom.xml 中删除该依赖坐标
- D. 修改本地仓库，手动删除 jar 包
- **答案：B**。`<exclusions>` 复数包 `<exclusion>` 单数，里面写 groupId + artifactId。

**15. 在 IDEA 中导入已有的 Maven 项目时，推荐的方式是？**
- A. 直接复制项目文件夹到工作空间，无需额外操作
- B. 选择项目的 pom.xml 文件，通过 Maven 面板的"Add Maven Projects"或 Project Structure 导入
- C. 手动配置所有依赖 jar 包路径
- D. 先删除 pom.xml 再重新创建
- **答案：B**。认准 pom.xml 才是 Maven 项目的入口。

## E. 实践 4 Web 基础选择题（15 题 · 含完整题干）

**1. 在 HTTP 协议中，以下关于"无状态"特点的描述，正确的是？**
- A. HTTP 协议可以通过 Cookie 自动保存上一次请求的所有数据
- B. 每一次请求-响应都是独立的，服务器不会记住之前的请求信息
- C. HTTP 基于 UDP 协议，所以没有连接状态
- D. 无状态导致浏览器和服务器无法完成任何数据交互
- **答案：B**。无状态就是请求之间互不知道，要维持状态得用 Cookie/Session。

**2. 关于 SpringBoot 的起步依赖（starter）的作用，下列哪项描述最准确？**
- A. 用于代码自动生成，无需编写任何配置文件
- B. 它是一组依赖的集合，简化了项目构建，例如 spring-boot-starter-web 包含了 web 开发常用依赖
- C. 仅用于单元测试，生产环境不可用
- D. 必须手动引入所有传递依赖，不能自动管理版本
- **答案：B**。starter 就是一组依赖打包好了，引一个等于引一堆。

**3. 在 SpringBoot Web 项目中，开发一个处理浏览器请求的控制器，下列哪个注解通常用于标识该类为请求处理类并默认将返回值转为 JSON？**
- A. @Component   B. @Service   C. @RestController   D. @Configuration
- **答案：C**。`@RestController` = `@Controller` + `@ResponseBody`，返回值自动转 JSON。

**4. 在 HTTP 响应状态码中，"404"状态码属于哪一类，表示什么含义？**
- A. 1xx，表示服务器正在处理   B. 2xx，表示成功响应   C. 3xx，表示重定向   D. 4xx，表示客户端错误，资源未找到
- **答案：D**。4xx 是客户端错，404 就是路径找不到。

**5. 关于 RESTful API 设计风格，下列哪种做法符合 RESTful 规范？**
- A. 使用 GET 请求删除一个用户：/deleteUser?id=10
- B. 更新用户信息使用 POST /updateUserInfo
- C. 获取所有用户使用 GET /users
- D. 创建新用户使用 GET /users/create
- **答案：C**。RESTful 用 HTTP 动词表示动作，URL 里只放资源名。

**6. 在 SpringBoot 中，实现三层架构时，用于标识数据访问层（DAO）组件的注解是？**
- A. @Controller   B. @Service   C. @Repository   D. @ComponentScan
- **答案：C**。`@Repository` 标识 Dao 层 Bean。

**7. 关于控制反转（IoC）和依赖注入（DI）的理解，下列说法错误的是？**
- A. IoC 是指对象的创建控制权由程序自身转移到外部容器
- B. DI 是容器为应用程序提供运行时所依赖的资源
- C. 使用 @Autowired 注解可以实现依赖注入
- D. 在 SpringBoot 中，所有类都必须手动通过 new 关键字创建对象
- **答案：D**。IOC 容器接管对象创建，根本不用自己 new。

**8. 在 SpringBoot 中，@SpringBootApplication 注解默认的组件扫描范围是？**
- A. 扫描整个项目所有包及第三方 jar
- B. 仅扫描启动类所在包及其子包
- C. 只扫描 controller 包
- D. 扫描所有标注了 @Component 的类，不限包路径
- **答案：B**。所以 Controller / Service / Dao 都要放在启动类同级或子包下。

**9. 关于 HTTP 协议的请求数据格式，以下哪个部分用于存放 POST 请求的请求参数？**
- A. 请求行   B. 请求头   C. 空行之后的内容（请求体）   D. 响应体
- **答案：C**。POST 参数在请求体里，GET 参数在 URL 上。

**10. 在分层解耦中，三层架构的正确顺序（自上而下调用）通常为？**
- A. Controller → Service → Dao   B. Service → Controller → Dao   C. Dao → Service → Controller   D. Controller → Dao → Service
- **答案：A**。Controller 接请求，调 Service 处理业务，Service 调 Dao 访问数据。

**11. 以下关于 SpringBoot 内嵌 Tomcat 的说法，正确的是？**
- A. SpringBoot 必须部署到外部 Tomcat 才能运行 Web 项目
- B. 内嵌 Tomcat 需要手动下载安装插件，默认没有
- C. SpringBoot 的 spring-boot-starter-web 中包含了内嵌 Tomcat 依赖，运行 main 方法即可启动 Web 服务器
- D. 内嵌 Tomcat 只支持 HTTP/2，不支持 HTTP/1.1
- **答案：C**。一个 main 方法就跑起来了，默认 8080 端口。

**12. 关于 @ResponseBody 注解的作用，描述正确的是？**
- A. 将方法返回值直接写入 HTTP 响应体，如果是对象/集合会转为 JSON
- B. 必须与 @Controller 同时使用，不能单独存在
- C. 只能返回字符串，不能返回实体对象
- D. 该注解用于接收前端请求参数
- **答案：A**。`@ResponseBody` 让返回值直接进响应体，对象会被 Jackson 序列化为 JSON。

**13. 在 IoC 容器中，如果一个接口有多个实现类，使用 @Autowired 自动装配可能引起冲突。下列哪种解决方案不符合 Spring 推荐做法？**
- A. 使用 @Primary 注解指定首选 Bean
- B. 使用 @Qualifier 注解指定名称
- C. 使用 @Resource(name="xxx") 根据名称注入
- D. 将实现类全部排除，避免歧义
- **答案：D**。Spring 推荐前三种（@Primary、@Qualifier、@Resource），把实现类全删了等于跑不起来。

**14. 在 SpringBoot Web 案例中，我们通过 Controller 读取 user.txt 并返回用户列表，前端通过 Vue 渲染。其中 Controller 方法上未写 @ResponseBody 但能返回 JSON，原因是？**
- A. SpringBoot 自动将所有返回值转为 JSON
- B. @RestController 组合了 @Controller 和 @ResponseBody，因此默认具备响应体直接输出 JSON 的能力
- C. 由于使用了 Lombok 插件自动增强
- D. 返回类型为 List 时 SpringMVC 自动识别
- **答案：B**。`@RestController` 已经把 `@ResponseBody` 含进去了，方法上不用再写。

**15. 关于 B/S 架构与 C/S 架构的比较，根据课堂内容下列说法正确的是？**
- A. B/S 架构需要单独安装客户端，用户体验好
- B. C/S 架构维护方便，无需升级客户端
- C. B/S 架构应用程序的逻辑和数据存储在服务器端，维护方便，但体验一般
- D. C/S 架构是基于浏览器的，不需要下载任何软件
- **答案：C**。B/S 浏览器即客户端，维护方便但受网速影响；C/S 体验好但要装客户端。

## F. 实践 5 MySQL 选择题（15 题 · 含完整题干）

**1. 数据库（DB）的基本定义是（  ）。**
- A. 一种编程语言   B. 存储和管理数据的仓库   C. 网络通信协议   D. 操作系统的一部分
- **答案：B**。DB = DataBase，就是存数据的仓库。

**2. 下列软件中，属于开源免费的关系型数据库的是（  ）。**
- A. Oracle   B. SQL Server   C. MySQL   D. DB2
- **答案：C**。MySQL 是开源的，Oracle/SQL Server/DB2 都收费。

**3. MySQL 8.x 默认使用的字符集是（  ）。**
- A. GBK   B. UTF-8   C. utf8mb4   D. ASCII
- **答案：C**。utf8mb4 支持完整的 4 字节 UTF-8，能存 emoji。

**4. 在 MySQL 命令行中，用于指定登录端口的参数是（  ）。**
- A. -h   B. -P   C. -u   D. -p
- **答案：B**。**大写 P** 是端口，小写 p 是密码，-h 是主机，-u 是用户。

**5. 下列 SQL 语言分类中，用于定义数据库、表结构的是（  ）。**
- A. DDL   B. DML   C. DQL   D. DCL
- **答案：A**。DDL（Data Definition Language）建库建表改表结构。

**6. 用于实现主键字段自动增长的关键字是（  ）。**
- A. unique   B. not null   C. auto_increment   D. default
- **答案：C**。`auto_increment` 自增。

**7. 下列数据类型中，属于固定长度字符串类型的是（  ）。**
- A. VARCHAR   B. CHAR   C. TEXT   D. BLOB
- **答案：B**。`CHAR(n)` 固定 n 字节；`VARCHAR(n)` 可变长。

**8. 在 SQL 中，用于删除表中数据但保留表结构的语句是（  ）。**
- A. DROP TABLE   B. DELETE FROM   C. ALTER TABLE   D. TRUNCATE TABLE
- **答案：B**。`DELETE FROM` 删数据保留表结构、可加 WHERE 条件；`DROP` 连表都删了。

**9. DQL 语句中，用于条件过滤的关键字是（  ）。**
- A. ORDER BY   B. GROUP BY   C. WHERE   D. HAVING
- **答案：C**。`WHERE` 在分组前过滤，`HAVING` 在分组后过滤。

**10. 下列聚合函数中，用于统计记录行数的是（  ）。**
- A. SUM()   B. AVG()   C. COUNT()   D. MAX()
- **答案：C**。`COUNT(*)` 数行数。

**11. 模糊查询中，用于匹配任意单个字符的通配符是（  ）。**
- A. %   B. _   C. *   D. ?
- **答案：B**。`_` 配单个字符，`%` 配任意多个字符。

**12. 部门表与员工表之间的关系是（  ）。**
- A. 一对一   B. 一对多   C. 多对多   D. 无关系
- **答案：B**。一个部门有多个员工，一个员工只属于一个部门。

**13. 实现多对多表关系，需要使用（  ）。**
- A. 主表   B. 从表   C. 中间表   D. 视图
- **答案：C**。多对多必须建中间表，放两个外键。

**14. 内连接（INNER JOIN）查询的是（  ）。**
- A. 左表全部数据   B. 右表全部数据   C. 两张表的交集数据   D. 两张表的并集数据
- **答案：C**。内连接只要两表都匹配的数据。

**15. 下列 SQL 注释方式中，属于标准通用注释的是（  ）。**
- A. `# 注释内容`   B. `-- 注释内容`   C. `// 注释内容`   D. `<!-- 注释内容 -->`
- **答案：B**。`-- ` 是 SQL 标准注释（注意 `--` 后面要有空格），`#` 是 MySQL 特有。

## G. 实践 6 JDBC 选择题（15 题 · 含完整题干）

**1. 以下关于 JDBC 的描述，哪一项是准确的？**
- A. JDBC 是 Java 语言操作非关系型数据库的专用 API
- B. JDBC 是 Sun 公司定义的一套操作关系型数据库的规范（接口），数据库厂商提供驱动实现
- C. JDBC 只能用于 MySQL 数据库，不能用于 Oracle 或 SQL Server
- D. JDBC 的全称是 Java Database Connector，用于连接图形界面
- **答案：B**。JDBC 是规范，各家厂商给驱动 jar；全称 Java DataBase Connectivity。

**2. 在 JDBC 编程中，若使用 MySQL 8.0 及以上版本，驱动类的名称应该使用？**
- A. com.mysql.jdbc.Driver
- B. com.mysql.cj.jdbc.Driver
- C. oracle.jdbc.driver.OracleDriver
- D. com.mysql.Driver_New
- **答案：B**。MySQL 8.x 必须带 `cj`，5.x 才用不带 cj 的旧驱动。

**3. 执行 JDBC 查询操作时，用于存储查询结果集并移动光标、获取数据的对象是？**
- A. Statement   B. PreparedStatement   C. ResultSet   D. Connection
- **答案：C**。`ResultSet` 是结果集，用 `rs.next()` 移动光标。

**4. 关于 JDBC 中 PreparedStatement 预编译的优势，以下说法错误的是？**
- A. 可以有效防止 SQL 注入攻击，更加安全
- B. 由于预编译和缓存机制，执行相同 SQL 结构多次时性能更高
- C. PreparedStatement 只能执行查询操作，不能执行更新操作
- D. 使用 ? 占位符设置参数，提升代码可读性和安全性
- **答案：C**。PreparedStatement 也能执行更新（`executeUpdate`）。

**5. 已知某登录功能采用原始 Statement 拼接 SQL 字符串，攻击者在密码框输入 `' or '1'='1` 成功登录系统。该漏洞属于？**
- A. XSS 跨站脚本攻击   B. CSRF 攻击   C. SQL 注入攻击   D. 缓冲区溢出攻击
- **答案：C**。典型 SQL 注入，`or '1'='1'` 让 where 永真。

**6. 关于 MyBatis 框架的描述，下列哪个选项是正确的？**
- A. MyBatis 是一个控制层框架，用于处理前端请求
- B. MyBatis 是持久层框架，可以简化 JDBC 的开发，内置 SQL 映射和数据库交互功能
- C. MyBatis 只能通过 XML 配置文件编写 SQL，不支持注解方式
- D. MyBatis 原名 Hibernate，2013 年迁移到 Github
- **答案：B**。MyBatis 是持久层框架，注解和 XML 两种方式都支持。

**7. 在 SpringBoot 入门程序中使用 MyBatis 时，若希望将数据库连接信息配置在 application.properties 中，以下哪一项不是必需的配置？**
- A. spring.datasource.url
- B. spring.datasource.driver-class-name
- C. spring.datasource.username 和 password
- D. mybatis.config-location
- **答案：D**。前三项是连数据库必需，`mybatis.config-location` 用主配置文件时才需要。

**8. MyBatis 中用于标识 Mapper 接口，让 Spring 框架生成代理对象并交给 IOC 容器管理的注解是？**
- A. @Repository   B. @Service   C. @Mapper   D. @Component
- **答案：C**。`@Mapper` 让 MyBatis 给接口生成代理实现类。

**9. 在 MyBatis 动态 SQL 中，若需要传递多个参数到 Mapper 方法，推荐使用哪个注解为参数起名字，避免 SQL 参数绑定错误？**
- A. @RequestParam   B. @PathVariable   C. @Param   D. @ModelAttribute
- **答案：C**。`@Param("name") String name` 给参数起别名，SQL 里用 `#{name}` 引用。

**10. 执行 MyBatis 的删除（DELETE）或更新（UPDATE）操作时，如果想知道影响的行数，接口方法的返回值类型通常为？**
- A. ResultSet   B. int 或 Integer   C. boolean   D. void
- **答案：B**。`executeUpdate` 返回 int 影响行数，MyBatis 方法直接声明 `int` 或 `Integer` 接住。

**11. 关于数据库连接池的描述，哪个说法是错误？**
- A. 数据库连接池可以复用连接，减少创建和销毁的开销，提升系统响应速度
- B. SpringBoot 2.x 默认使用的数据库连接池是 HikariCP
- C. Druid 是阿里巴巴开源的连接池，功能强大，但在 SpringBoot 中无法替换默认连接池
- D. 连接池可以避免因连接未关闭导致的数据库连接遗漏
- **答案：C**。Druid 完全可以替换 HikariCP，引依赖 + 配 `spring.datasource.type=com.alibaba.druid.pool.DruidDataSource` 即可。

**12. MyBatis 中"#{}" 与 "${}" 占位符的区别，下列理解正确的是？**
- A. `${}` 采用预编译方式，可以防止 SQL 注入，性能更高
- B. `#{}` 仅仅是字符串拼接，容易引起 SQL 注入问题
- C. `#{}` 会替换为 ? 生成预编译 SQL，安全且性能好；`${}` 则是直接拼接参数值，有注入风险
- D. `#{}` 用于传递表名或列名动态场景，`${}` 用于传递值
- **答案：C**。这条要背死：`#{}` 预编译（推荐），`${}` 拼接（只在传表名/列名时才用）。

**13. 关于 MyBatis 的 XML 映射文件配置规则，不正确的是哪一项？**
- A. XML 映射文件名称需要与 Mapper 接口名称一致，且通常放在相同包下（同包同名）
- B. XML 映射文件中 namespace 属性应该为 Mapper 接口的全限定名
- C. 同一个 Mapper 接口方法可以同时在注解和 XML 中配置 SQL 语句，MyBatis 会自动合并
- D. XML 中 SQL 语句的 id 需要与 Mapper 接口中的方法名保持一致
- **答案：C**。同一方法两边都配 SQL 会**报错**，只能二选一。

**14. 在 Spring Boot 整合 MyBatis 的项目中进行单元测试时，需要在测试类上添加哪个注解，才能在测试方法中通过 @Autowired 自动注入 Mapper 接口对象？**
- A. @RunWith(SpringRunner.class)   B. @Test   C. @SpringBootTest   D. @MybatisTest
- **答案：C**。`@SpringBootTest` 启动 Spring 容器，`@Autowired` 才能生效。

**15. 关于 YAML 配置文件（application.yml）的特点，下面描述有误的是？**
- A. YAML 以数据为中心，使用缩进表示层级，不允许使用 Tab 键，只能用空格
- B. 在 YAML 中定义数组可以用 "-" 引导的列表形式
- C. YAML 文件中如果写 0 开头数字如"012"会被解析为十进制 12
- D. YAML 相比 properties 配置文件更简洁、层级清晰，支持对象和集合的表示
- **答案：C**。`012` 在 YAML 里会被当成**八进制**解析为 10，不是 12。

---


# 第六部分 · 应试技巧

## 1. 选择题套路
- **看清楚是选"对的"还是"错的"**。考题里"下列描述错误的是""不正确的是"出现频率很高。
- **绝对化表述慎选**：含"只能""必须""一定"的选项八成是错的。
- **看不懂的题目用排除法**：先排掉明显错的，剩下两个选意思更具体的那个。
- **JS 数组遍历题**：仔细看 i 从几开始、条件是 `<` 还是 `<=`、累加的是 a[i] 还是 i。

## 2. 判断题套路
- **属性归类型问题**：font-size 是字体属性，不是文本属性（这种细节最容易翻车）。
- **倒装句**：HTTP 是无状态（不是有状态）、JS 是弱类型（不是强类型）、PreparedStatement 防注入（不是 Statement）。

## 3. 简答题套路
- 开头 "答："顶格。
- 分项用 `①②③` 或 `· `，**每条一行**。
- 答案具体：① 概念定义；② 列举要素（仓库三类、生命周期五个、注解四个）；③ 举例（举一个最常见的代表 jar 或场景）。
- **禁用 AI 套话**：不要写"综上所述""值得注意的是""首先...其次...最后"。
- 涉及命令、注解、SQL 关键字、HTML 标签时**原样写**：`@Autowired`、`<exclusions>`、`mvn clean install`、`com.mysql.cj.jdbc.Driver`。

## 4. 编程大题套路

### HTML 表单
- 外层 `<form action="..." method="post">`，结尾 `</form>` 别漏。
- 每个 input、select、textarea 都要有 `name` 属性。
- 单选/多选同组 `name` 必须一致，提交按钮 `type="submit"`。

### SQL
- 每条语句末尾**加分号** `;`。
- 字符串用**单引号**：`name = '张三'`，不是 `"张三"`。
- 模糊查询 `LIKE '阮%'`，% 在哪一边对应"前/后/包含"。
- 分页 `LIMIT (page-1)*size, size`。
- 多表查询带表别名：`select e.name, d.name from emp e join dept d on e.dept_id = d.id`。

### 三层架构
- 文件结构：`controller / service / service/impl / dao / dao/impl / pojo`。
- Controller 上 `@RestController`、Service 实现类上 `@Service`、Dao 实现类上 `@Repository`。
- 跨层属性上 `@Autowired`。
- 接口和实现分离：`UserService` 接口 + `UserServiceImpl` 实现类。

### JDBC（实践 6 第三题风格 · 必考）
课件标准写法：`main` 方法直接 `throws Exception`，**不写 try-catch**。照着写五步：
```
1. Class.forName 注册驱动
2. DriverManager.getConnection 获取连接
3. conn.prepareStatement(sql) 获取预编译对象
4. ps.setXxx(i, v) 绑参 + ps.executeQuery() / executeUpdate() 执行
5. 反向关闭：rs.close() → ps.close() → conn.close()
```
- 驱动名 `com.mysql.cj.jdbc.Driver`（带 cj！）
- URL 末尾带 `?useSSL=false&serverTimezone=UTC`
- 占位符下标**从 1 开始**
- 编程题开头千万别写 `try {`，课件示例就是裸 `throws Exception`

## 5. 时间分配实操
- 拿到卷子先扫一遍编程题（最耗时），心里有个底。
- 选择 + 判断快速过，不会的标记跳过，最后回来抢分。
- 简答题按熟悉度排序：先答会的，确保拿全分；再啃难的。
- 编程题留至少 50 分钟，HTML 表单和 SQL 优先（题量大但套路固定），三层架构和 JDBC 套模板。
- 最后 10 分钟检查：SQL 分号、Java 分号、闭合标签、注解拼写。

## 6. 复习时间建议（最后一周）
- 第 1 天：CH1 HTML + CSS + 把 HTML 表单模板背一遍
- 第 2 天：CH2 JS + Vue3 + 做完前端选择题 15 题
- 第 3 天：CH3 Maven + 实践 3 选择题 15 题
- 第 4 天：CH4 Web 基础 + 三层架构代码 + 简答题 5 道
- 第 5 天：CH5 MySQL + 默写 SQL 模板 + 实践 5 选择题
- 第 6 天：CH6 JDBC + 默写 JDBC 模板 + 实践 6 选择题
- 第 7 天：全套题模拟一遍，回看错题

---

**祝考试顺利。**
