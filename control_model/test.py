from assignment import Assignment
import os
import asyncio
import time
import subprocess
from queue import Queue

# a = Assignment("../data/undirected-5-my.txt",4)
class Manager:
    task_queue = None

    async def fun(self,sec):
        print(sec)
        print("qsize:"+str(self.task_queue.qsize()))
        test1 = self.task_queue.put(sec)
        curtime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        print(curtime+" :begin task"+str(sec))
        os.system("./haha.sh")
        curtime = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        print(curtime+" :finish task"+str(sec))
        test2 = self.task_queue.get()
        await test1
        await test2

    async def main(self):
        self.task_queue = asyncio.Queue(maxsize=4)
        task = []
        for i in range(10) :
            task.append(asyncio.create_task(self.fun(i)))
        # await self.task_queue.join()
        # await asyncio.gather(*task, return_exceptions=True)
    def __init__(self):
        asyncio.run(self.main())

que = Queue(maxsize=4)

async def test(i):
    try:
        while que.full():
            await asyncio.sleep(1)
        tmp = que.put(i)
    except :
        print("error")

    print("begin task "+str(i)+":"+time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
    p = subprocess.Popen(["sleep",str(i)+"s"])
    while True:
        await asyncio.sleep(1)
        if p.poll()!=None :
            print("finish task " + str(i) + ":" + time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))
            que.get(tmp)
            break;

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(test(i)))
        # test(i)
    for task in tasks:
        await task
# test = Manager()
# asyncio.run(main())
# # main()
# os.system("nohup sleep 10s &")

test = Assignment(path="../data/undirected-5-my.txt")

test.run_CPU()
test.run_GPU()

