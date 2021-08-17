remote-debugging-port

https://zhuanlan.zhihu.com/p/60852696

```python
from selenium import webdriver
option = webdriver.ChromeOptions()

# 添加启动参数
option.add_argument()

# 添加扩展应用 
option.add_extension()
option.add_encoded_extension()

# 添加实验性质的设置参数 
option.add_experimental_option()

# 设置调试器地址
option.debugger_address = "127.0.0.1:9222"
```

## 浏览器地址栏参数

在浏览器地址栏输入下列命令得到相应的信息

* about:version - 显示当前版本
* about:memory - 显示本机浏览器内存使用状况
* about:plugins - 显示已安装插件
* about:histograms - 显示历史记录
* about:dns - 显示 DNS 状态
* about:cache - 显示缓存页面
* about:gpu -是否有硬件加速
* chrome://extensions/ - 查看已经安装的扩展
