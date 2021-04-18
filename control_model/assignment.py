from keras import models
import asyncio
import os
from queue import Queue
import subprocess
import re

exec_CPU = os.path.abspath(os.path.join(os.getcwd(),"../CPU"))
exec_GPU = os.path.abspath(os.path.join(os.getcwd(),"../GPU"))

class Assignment:
    CPU_time = 0
    GPU_time = 0
    Init_ime = 0
    repeat = 100
    k = 0
    path = ""
    is_directed = False
    filename = ""

    _CPU_finished = False
    _GPU_finished = False


    def get_info(self):
        dic = {}
        with open(self.path) as file:
            dic["vexNum"]=int(file.readline());
            dic["edgeNum"] = 0;
            for line in file: dic["edgeNum"] += 1

        if (re.search(r'undirected',self.filename) == None): isDirected = ""
        print()
        return dic

    def _predict_run_time(self):
        dic = self.get_info()
        model = models.load_model("./prediction/IniTime.h5")
        self.Ini_time = model.predict([[self.k,dic["vexNum"],dic["edgeNum"]]])
        model = models.load_model("./prediction/CPUTime.h5")
        self.CPU_time = model.predict([[self.k,dic["vexNum"],dic["edgeNum"]]])
        model = models.load_model("./prediction/GPUTime.h5")
        self.GPU_time = model.predict([[self.k,dic["vexNum"],dic["edgeNum"]]])

    async def run_CPU(self,id,que):
        print("task begin:")
        print("CPUid: "+str(id)+" que_size:"+str(que.qsize()))
        if(self.is_directed) : isDirect = " -u"
        else : isDirect = ""

        result_path = os.path.abspath(os.path.join(os.getcwd(),"../result"))
        os.system("mkdir "+result_path+"/"+self.filename)
        result_path = os.path.join(result_path,self.filename)

        cmd = exec_CPU+" -i " + self.path+" -s " + str(self.k) + " -r " + str(self.repeat)+" -o "+ \
            result_path + " -g " + str(0) + isDirect +" >"+result_path+"/CPUlog"
        print(cmd)
        p = subprocess.Popen(cmd,shell=True)
        while True:
            await asyncio.sleep(1)
            # print(p.poll())
            if p.poll() != None:
                que.put(id)
                break
        return p

    async def run_GPU(self,GPUID,que):
        if (self.is_directed):
            isDirect = " -u"
        else:
            isDirect = ""

        result_path = os.path.abspath(os.path.join(os.getcwd(), "../result"))
        # os.system("mkdir " + result_path + "/" + self.filename)  #because run_CPU has mkdir
        result_path = os.path.join(result_path, self.filename)

        cmd = exec_GPU + " -i " + self.path + " -s " + str(self.k) + " -r " + str(self.repeat) + " -o " + \
              result_path + " -g " + str(GPUID) + isDirect + " >>" + result_path + "/GPUlog"
        print(cmd)
        p = subprocess.Popen(cmd, shell=True)
        while True:
            await asyncio.sleep(1)
            if p.poll() != None:
                que.put(GPUID)
                break;
        return p

    def __init__(self,path,k=4,repeat=100):
        self.k = k
        self.repeat = repeat
        self.path = os.path.abspath(os.path.join(os.getcwd(),path))
        self.filename = self.path.split('/')[-1]
        # print(self.path)
        # print (self.filename)

        self._predict_run_time()


class Manager:
    GPU_Num = 4
    CPU_Num = 4

    async def get_CPU(self):
        while(self.resource_CPU.empty()):
            # print("rest CPU:"+str(self.resource_CPU.qsize()))
            await asyncio.sleep(1)
        tmp = self.resource_CPU.get()
        # print(tmp)
        return tmp

    def free_CPU(self,id = 0):
        self.resource_CPU.put(id)

    async def get_GPU(self):
        while(self.resource_GPU.empty()):
            await asyncio.sleep(1)
        return self.resource_GPU.get()

    def free_GPU(self,id):
        self.resource_GPU.put(id)

    # def wait_CPU(self0):

    def _init_task(self):
        self.waitlist_CPU = Queue()
        self.waitlist_GPU = Queue()

        with open("../task/task1.txt", "r") as r:
            for line in r:
                line = line[0:-1]
                line = line.split(" ")
                item = Assignment(path=line[0], k=int(line[1]), repeat=int(line[2]))
                self.waitlist_CPU.put(item)
        print("waitlist len:"+str(self.waitlist_CPU.qsize()))

    def _init_thread(self):
        self.resource_CPU = Queue(maxsize=self.CPU_Num)
        self.resource_GPU = Queue(maxsize=self.GPU_Num)
        # self.resource_CPU.

        for i in range(self.CPU_Num):
            self.resource_CPU.put(i)
        for i in range(self.GPU_Num):
            self.resource_GPU.put(i)

    def __init__(self):
        self._init_thread()
        self._init_task()

    async def run_CPU(self):
        while(True):
            id = await self.get_CPU()
            if(self.waitlist_CPU.empty()) : continue
            # id = self.get_CPU()
            print("get CPU:"+str(id))
            task = self.waitlist_CPU.get();
            print("get task:");
            print(task)
            asyncio.create_task(task.run_CPU(id,self.resource_CPU))










