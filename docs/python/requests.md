# requests

对于 content-type 为 `Content-Type: application/json` 的请求

```python
def query_data_from_hbase():

    cookies = {"ticket": "someticket",}
    headers = {}
    data = {"sql": "some sql"}
    response = requests.post(
        "http://url",
        headers=headers,
        cookies=cookies,
        json=data,
        verify=False,
    )
    return response
```

下载图片

```python
img_data = session.get("https://cas.sysu.edu.cn/cas/captcha.jsp").content
with open("./captcha.jpg", "wb") as fp:
    fp.write(img_data)
```

## cookie与持久化

处理cookie

```python
session = requests.session()

cookies = response.cookies.get_dict()
```