# 异步编程 aiohttp 库

[官方文档](https://docs.aiohttp.org/en/stable/)

安装 aiohttp 以及其依赖的网络加速库

```bash
pip3 install "aiohttp[speedups]"
```

客户端示例

```python
import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```