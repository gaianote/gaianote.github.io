## flask 上下文

注意,get 请求时,需要特殊字符前端需要 encode 后传入,否则会有问题

```python
request.args # 获取get请求的参数
request.get_json()
```

python url decode

```python
from urllib.parse import unquote
unquote("a%2BM0bNSZVRWTKVb6OtprBw%3D%3D")
```

## 让 jsonify()结果返回中文

```python
app.config['JSON_AS_ASCII'] = False
```
