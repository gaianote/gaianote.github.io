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
