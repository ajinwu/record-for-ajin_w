import asyncio
import time
async def get_html(url):
    print("start get html")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://www.imooc.com") for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)