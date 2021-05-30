import random

from control_model.assignment import Assignment,Manager
import os
import asyncio
import time
import subprocess
from queue import Queue

# a = Assignment("../data/undirected-5-my.txt",4)

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

# test = Assignment(path="../data/undirected-5-my.txt")
#
# test.run_CPU()
# test.run_GPU()

manager = Manager(is_test=0)

#asyncio.run(manager.main())
loop = asyncio.get_event_loop()
result = loop.run_until_complete(manager.main())
# cmd = "python ./sleep.py"
# print (cmd)
# p = subprocess.Popen(cmd, shell=True)
# while True:
#     if p.poll() != None:
#         print("finished!")
#         break
# print("管胡昊")
# asyncio.run(manager.run_GPU())

