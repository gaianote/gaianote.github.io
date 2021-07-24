# 并发操作

## ThreadPoolExecutor 线程池

ThreadPoolExecutor可以控制最大的并发数量,下述脚本的含义是:

task是任务进程
通过线程池实现,执行10个总任务,且最大并发数为3
当10个任务都完成后,进行执行主线程其它任务

```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time
# 1. 任务进程
def task(i):
    time.sleep(1)
    print(str(i) + '...end')
# 2. 线程池
with ThreadPoolExecutor(3) as pool:
    for i in range(10):
        pool.submit(task,i)
# 3. 主线程
print('main_1 thread end...')
```

### 要点 

1. task任务报错不会被抛出
2. 无法读取变量


[](https://www.jianshu.com/p/b9b3d66aa0be)

