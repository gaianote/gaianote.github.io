# python 执行外部命令

```python
import subprocess

cmd = "mitmdump --set upstream-cert=false --no-http2 -q -s mitm.py -p 9090"
p = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, shell=True)
print(p.pid)
# p.kill()

```

## p.communicate()

## python 关闭进程
