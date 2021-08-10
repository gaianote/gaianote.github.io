## 如何启动多个独立的 Google Chrome 实例

在日常工作中通常需要使用多个用户登录到系统中，事实上，如果在同一个 Google Chrome 实例中登录多个用户，这几乎是不可能的，（虽然使用隐身方式可以打开两个独立的 Google Chrome 实例，但是如何才能打开两个以上的实例呢？）因为同一个 Google Chrome 实例中，后登录的用户的 Cookie 等信息会覆盖前一登录用户的信息。

解决方法

Google Chrome 默认的 working directory 是“\${user.dir}/Library/Application Support/Google/Chrome/Default”(For windows: “C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default”)里面记录了 session，cookie 等诸多信息。

了解到 Google Chrome 保存 Cookie 等信息是在一个 working directory 这一点，解决上述问题就不在困难。

实际操作
通过指定工作目录来确保用户状态不会被替换，通过参数“--user-data-dir="/path/to/real/directory/"”

类 UNIX 系统

可以使用如下命令：
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --user-data-dir="/Users/CentLui/temp/Google/Chrome/SystemA/dev
```

Windows 系统
可以使用如下的命令：

```bash
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\Users\Administrator\Google\SystemA\dev"
```
