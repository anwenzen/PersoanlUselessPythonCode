import aiohttp
import time
import asyncio
async def job(session):
    response = await session.get('https://morvanzhou.github.io/')       # 等待并切换
    return str(response.url)


async def main(loop):
    async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        print(type(finished),type(unfinished))
        all_results = [r.result() for r in finished]    # 获取所有结果
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)

"""
['https://morvanzhou.github.io/', 'https://morvanzhou.github.io/']
Async total time: 0.11447715759277344
"""