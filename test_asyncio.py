
import asyncio

async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    return 1

async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    print("worker_3 start")
    await asyncio.sleep(3)
    return 3

async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    print("task 123 created")
    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)
    print("end")

if __name__ == "__main__":
    asyncio.run(main())

# ########## 输出 ##########

# [1, ZeroDivisionError('division by zero'), CancelledError()]
# Wall time: 2 s