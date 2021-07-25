# 多进程 multiprocess

Python 中的 `multiprocess` 提供了 `Process` 类，实现进程相关的功能。但是它基于 fork 机制，因此不被 windows 平台支持。想要在 windows 中运行，必须使用 `if __name__ == '__main__':`的方式，显然这只能用于调试和学习，不能用于实际环境。

另外，在 multiprocess 中你既可以 import 大写的 Process，也可以 import 小写的 process，这两者是完全不同的东西。这种情况在 Python 中很多，请一定要小心和注意。

下面是一个简单的多进程例子，Process 类的用法和 Thread 类几乎一模一样。

```python
import os
import multiprocessing

def foo(i):
    # 同样的参数传递方法
    print("这里是 ", multiprocessing.current_process().name)
    print('模块名称:', __name__)
    print('父进程 id:', os.getppid())  # 获取父进程id
    print('当前子进程 id:', os.getpid())  # 获取自己的进程id
    print('------------------------')

if __name__ == '__main__':

    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
```

运行结果：

```
这里是  Process-2
模块名称: __mp_main__
父进程 id: 880
当前子进程 id: 5260
--------------
这里是  Process-3
模块名称: __mp_main__
父进程 id: 880
当前子进程 id: 4912
--------------
这里是  Process-4
模块名称: __mp_main__
父进程 id: 880
当前子进程 id: 5176
--------------
这里是  Process-1
模块名称: __mp_main__
父进程 id: 880
当前子进程 id: 5380
--------------
这里是  Process-5
模块名称: __mp_main__
父进程 id: 880
当前子进程 id: 3520
--------------
```

## 1. 进程间的数据共享


在 Linux 中，每个子进程的数据都是由父进程提供的，每启动一个子进程就从父进程克隆一份数据。

创建一个进程需要非常大的开销，每个进程都有自己独立的数据空间，不同进程之间通常是不能共享数据的，要想共享数据，一般通过中间件来实现。

下面我们尝试用一个全局列表来实现进程间的数据共享：

```python
from multiprocessing import Process

lis = []

def foo(i):
    lis.append(i)
    print("This is Process ", i," and lis is ", lis, " and lis.address is  ", id(lis))

if __name__ == '__main__':
    for i in range(5):
        p = Process(target=foo, args=(i,))
        p.start()
    print("The end of list_1:", lis)
```

运行结果：

```
The end of list_1: []
This is Process  2  and lis is  [2]  and lis.address is   40356744
This is Process  1  and lis is  [1]  and lis.address is   40291208
This is Process  0  and lis is  [0]  and lis.address is   40291208
This is Process  3  and lis is  [3]  and lis.address is   40225672
This is Process  4  and lis is  [4]  and lis.address is   40291208
```

可以看到，全局列表 lis 没有起到任何作用，在主进程和子进程中，lis 指向内存中不同的列表。

想要在进程之间进行数据共享可以使用`Queues`、`Array`和`Manager`这三个 multiprocess 模块提供的类。

### 1.1 使用 Array 共享数据

对于 Array 数组类，括号内的“i”表示它内部的元素全部是 int 类型，而不是指字符“i”，数组内的元素可以预先指定，也可以只指定数组的长度。Array 类在实例化的时候必须指定数组的数据类型和数组的大小，类似 temp = Array('i', 5)。对于数据类型有下面的对应关系：

```
'c': ctypes.c_char, 'u': ctypes.c_wchar,
'b': ctypes.c_byte, 'B': ctypes.c_ubyte,
'h': ctypes.c_short, 'H': ctypes.c_ushort,
'i': ctypes.c_int, 'I': ctypes.c_uint,
'l': ctypes.c_long, 'L': ctypes.c_ulong,
'f': ctypes.c_float, 'd': ctypes.c_double
```

看下面的例子：

运行结果：

```
进程2   修改数组第一个元素后-----> 101
进程4   修改数组第一个元素后-----> 201
进程5   修改数组第一个元素后-----> 301
进程3   修改数组第一个元素后-----> 401
进程1   修改数组第一个元素后-----> 501
进程6   修改数组第一个元素后-----> 601
进程9   修改数组第一个元素后-----> 701
进程8   修改数组第一个元素后-----> 801
进程0   修改数组第一个元素后-----> 901
进程7   修改数组第一个元素后-----> 1001
```

### 1.2 使用 Manager 共享数据

通过 Manager 类也可以实现进程间数据的共享。Manager()返回的 manager 对象提供一个服务进程，使得其他进程可以通过代理的方式操作 Python 对象。manager 对象支持 list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value ,Array 等多种格式。

```python
from multiprocessing import Process
from multiprocessing import Manager

def func(i, dic):
dic["num"] = 100+i
print(dic.items())

if **name** == '**main**':
dic = Manager().dict()
for i in range(10):
    p = Process(target=func, args=(i, dic))
    p.start()
    p.join()
```

运行结果：

```
[('num', 100)]
[('num', 101)]
[('num', 102)]
[('num', 103)]
[('num', 104)]
[('num', 105)]
[('num', 106)]
[('num', 107)]
[('num', 108)]
[('num', 109)]
```

### 1.3 使用 queues 的 Queue 类共享数据

multiprocessing 是一个包，它内部又一个 queues 模块，提供了一个 Queue 队列类，可以实现进程间的数据共享，如下例所示：

```python
import multiprocessing
from multiprocessing import Process
from multiprocessing import queues

def func(i, q):
    ret = q.get()
    print("进程%s 从队列里获取了一个%s，然后又向队列里放入了一个%s" % (i, ret, i))
    q.put(i)

if __name__ == "__main__":
    lis = queues.Queue(20, ctx=multiprocessing)
    lis.put(0)
    for i in range(10):
        p = Process(target=func, args=(i, lis,))
        p.start()
```

运行结果：

```
进程 1 从队列里获取了一个 0，然后又向队列里放入了一个 1
进程 4 从队列里获取了一个 1，然后又向队列里放入了一个 4
进程 2 从队列里获取了一个 4，然后又向队列里放入了一个 2
进程 6 从队列里获取了一个 2，然后又向队列里放入了一个 6
进程 0 从队列里获取了一个 6，然后又向队列里放入了一个 0
进程 5 从队列里获取了一个 0，然后又向队列里放入了一个 5
进程 9 从队列里获取了一个 5，然后又向队列里放入了一个 9
进程 7 从队列里获取了一个 9，然后又向队列里放入了一个 7
进程 3 从队列里获取了一个 7，然后又向队列里放入了一个 3
进程 8 从队列里获取了一个 3，然后又向队列里放入了一个 8
```

关于 queue 和 Queue，在 Python 库中非常频繁的出现，很容易就搞混淆了。甚至是 multiprocessing 自己还有一个 Queue 类(大写的 Q)，一样能实现 queues.Queue 的功能，导入方式是 from multiprocessing import Queue。

## 2. 进程锁

为了防止和多线程一样的出现数据抢夺和脏数据的问题，同样需要设置进程锁。与 threading 类似，在 multiprocessing 里也有同名的锁类 RLock，Lock，Event，Condition 和 Semaphore，连用法都是一样样的，这一点非常友好！

```python
from multiprocessing import Process
from multiprocessing import Array
from multiprocessing import RLock, Lock, Event, Condition, Semaphore
import time

def func(i,lis,lc):
    lc.acquire()
    lis[0] = lis[0] - 1
    time.sleep(1)
    print('say hi', lis[0])
    lc.release()

if __name__ == "__main__":
    array = Array('i', 1)
    array[0] = 10
    lock = RLock()
    for i in range(10):
        p = Process(target=func, args=(i, array, lock))
        p.start()
```
运行结果：

```
say hi 9
say hi 8
say hi 7
say hi 6
say hi 5
say hi 4
say hi 3
say hi 2
say hi 1
say hi 0 
```

## 3. 进程池 Pool 类

进程启动的开销比较大，过多的创建新进程会消耗大量的内存空间。仿照线程池的做法，我们可以使用进程池控制内存开销。

比较幸运的是，Python 给我们内置了一个进程池，不需要像线程池那样要自己写，你只需要简单的 from multiprocessing import Pool 导入就行。进程池内部维护了一个进程序列，需要时就去进程池中拿取一个进程，如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。

进程池中常用的方法：

apply() 同步执行（串行）
apply_async() 异步执行（并行）
terminate() 立刻关闭进程池
join() 主进程等待所有子进程执行完毕。必须在 close 或 terminate()之后。
close() 等待所有进程结束后，才关闭进程池。

```python
from multiprocessing import Pool
import time

def func(args):
    time.sleep(1)
    print("正在执行进程 ", args)

if __name__ == '__main__':

    p = Pool(5)     # 创建一个包含5个进程的进程池

    for i in range(30):
        p.apply_async(func=func, args=(i,))

    p.close()           # 等子进程执行完毕后关闭进程池
    # time.sleep(2)
    # p.terminate()     # 立刻关闭进程池
    p.join()
```