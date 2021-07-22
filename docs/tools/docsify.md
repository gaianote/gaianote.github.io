# docsify

[docsify](https://docsify.js.org/#/zh-cn/) 可以根据 markdown 文档生成好看的博客站点,而[docsify-cli](https://github.com/docsifyjs/docsify-cli) 是它的命令行工具;我们可以轻易的开始使用它:

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
Successfully generated the sidebar file '_sidebar.md'.
```
