## docsify

[docsify](https://docsify.js.org/#/zh-cn/) 可以根据 markdown 文档生成好看的博客站点,而[docsify-cli](https://github.com/docsifyjs/docsify-cli) 是它的命令行工具;

常用的命令有以下三个,更多的使用方法可以到官网中查看

```bash
# 安装命令行工具
npm i docsify-cli -g
# 构建模版
docsify init ./docs
# 启动服务
docsify serve docs
```

docsify-cli 可以方便的生成 sidebar ,自动读取文件内容生成侧边栏;但是有一些问题,比如不会忽略 REAMDE,子路径生成存在 bug 等

```bash
docsify generate . --sidebar _sidebar.md
```

## 图片

`_media` 可以放图片等相关信息,其中路径是相对路径,比如以下结构

```
tools
 |- docsify.md
 |- _media
    |- simple.jpeg
```

当我们在文件中写入`![simple](_media/simple.jpeg)`时,系统会自动生成以下样式的 html 文件

```html
<img
  src="/tools/_media/simple.jpeg"
  data-origin="_media/simple.jpeg"
  alt="simple"
/>
```

下面是一个图片示例:

![simple](_media/simple.jpeg)

### 下载文件

下载文件需要借助 html 代码实现

```html
<a href="tools/_media/clashX.dmg" target="_blank">ClashX</a>
```

## github page

我们可以将博客发布到 [github page](https://pages.github.com/) 上,以供他人访问;在仓库 - Settings - Pages 可以将你的仓库设置为 github page

需要注意的是,如果你的仓库名为 gaianote.github.io ,那么发布地址为 gaianote.github.io,如果你的仓库名为 myblog 等名称,那么发布地址为 gaianote.github.io/myblog.请根据需要自己选择
