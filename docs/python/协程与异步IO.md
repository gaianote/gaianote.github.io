# 协程与异步 IO

通常在 Python 中我们进行并发编程一般都是使用多线程或者多进程来实现的，对于 CPU 计算密集型任务由于 GIL 的存在通常使用多进程来实现，而对于 IO 密集型任务可以通过线程调度来让线程在执行 IO 任务时让出 GIL，从而实现表面上的并发。

其实对于 IO 密集型任务我们还有一种选择就是协程。协程，又称微线程，英文名 Coroutine，是运行在单线程中的“并发”，协程相比多线程的一大优势就是省去了多线程之间的切换开销，获得了更高的运行效率。Python 中的异步 IO 模块 asyncio 就是基本的协程模块。

Python 中的协程经历了很长的一段发展历程。最初的生成器 yield 和 send()语法，然后在 Python3.4 中加入了 asyncio 模块，引入@asyncio.coroutine 装饰器和 yield from 语法，在 Python3.5 上又提供了 async/await 语法，目前正式发布的 Python3.6 中 asynico 也由临时版改为了稳定版。

## 1. 协程

- **进程/线程**：操作系统提供的一种并发处理任务的能力。
- **协程**：程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧。

## 2. async 和 await

`async` 关键字申明了该函数是一个异步函数，我们关注到的作用就只有这些。

`await` 关键字只能在使用了 async 申明过的协程函数中使用，该关键字后面加一个可等待对象（什么是可等待对象？能被暂停的对象，像生成器那样可以被暂停）。可等待 对象有三种主要类型: **协程**、 **任务** 和 **Future**.

协程的发展经过了多个版本的迭代,个人推荐的协程写法如下:

```python
import asyncio
import time

async def func_1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "函数一的返回值"

async def func_2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return "函数二的返回值"

async def main():
    tasks1 = (func_1(), func_2())  # 分组1
    tasks2 = [func_2(), func_1()]  # 分组2
    result_1 = await asyncio.gather(*tasks1)
    result_2 = await asyncio.gather(*tasks2)
    print(result_1, result_2)

if __name__ == "__main__":
    start_time = time.time()  # 始运行的时间
    asyncio.run(main())
    print(time.time() - start_time)  # 结束的时间减去开始时间，可以发现总时间4秒
# result_1的返回值：['函数一的返回值', '函数二的返回值']
# result_2的返回值：['函数二的返回值', '函数一的返回值']
```

- `asyncio.gather()` 方法在基础上和 `asyncio.wait()` 方法一致，但它还提供了分组、具体的返回值和任务的取消。**一组内的运行是异步的，但不同分组的之间是同步的**,所以运行上面的代码时间是 4 秒。
- `asyncio.gather()` 返回的结果不是一个对象，而**是具体的返回值**，不管分组是列表、元组和集合，它的返回值都放在列表中。
- `gather` 方法原型为 def gather(\*coros_or_futures, loop=None, return_exceptions=False)，return_exceptions 参数默认为 False，代表当运行异步任务时，**某一个任务出现了错误，就会立刻将异常返回给等待它的任务**，就等于该任务被取消了，但其它的任务不会被影响而继续运行；当参数设置为 True，一个任务出现了错误，**返回的异常信息作为运行结果**，其它的任务同样不会受影响；没有说参数设置为哪个好，一切都要看需求。

## 参考资料

- [Python 异步 asyncio 库学习总结](https://blog.csdn.net/qq_43279457/article/details/110906565)
