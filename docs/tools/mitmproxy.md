# 常用脚本

## 1. 实现mapRemote功能

```python
# 1. 编写mitm.py脚本如下

import mitmproxy.http
from mitmproxy import ctx

class Counter:
    def request(self, flow):
        if flow.request.host.endswith("thor.pre.weidian.com"):
            flow.request.scheme = "http"
            flow.request.port = 80
            flow.request.host = "houtu.pre.vdian.net"
            flow.request.path = "/thorRemote" + flow.request.path
            flow.request.headers["Host"] = "houtu.pre.vdian.net"
    def response(self, flow):
        if flow.request.host.endswith("houtu.pre.vdian.net"):
            print(flow.response.text)
addons = [
    Counter()
]


# 2. 启动脚本,并关闭验证上游服务器SSL

mitmdump -s mitm.py -p 9090 --ssl-insecure --no-http2 -q
```

## 2. mock reponse

```python
import json,copy
import mitmproxy.http
from mitmproxy import ctx

class LiveCounter(object):
    """
    直播频道页数据mock
    """

    def response(self, flow):

        if flow.request.url.find("live/live.listPubLivings/1.0") != -1:
            print(flow.request.url)
            print(flow.request.query)
            print(flow.response.text)
            result = json.loads(flow.response.text)
            putongLive = copy.deepcopy(result["result"]["liveList"][0])
            putongLive["isAdvertPit"] = 0
            result["result"]["liveList"].insert(0,putongLive)
            flow.response.text =  json.dumps(result)

addons = [
    LiveCounter()
]

```
正常情况下,我们是不能直接使用https重定向到http的,但是可以添加此参数来解决这个问题

```
mitmdump --set upstream-cert=false --no-http2 -q -s mitm.py
```