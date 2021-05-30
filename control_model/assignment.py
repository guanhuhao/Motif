from keras import models
import asyncio
import os
from queue import Queue,PriorityQueue
import subprocess
import re
import random
import time
import copy

exec_CPU = os.path.abspath(os.path.join(os.getcwd(),"./CPU"))
exec_GPU = os.path.abspath(os.path.join(os.getcwd(),"./GPU"))
print(exec_GPU)

class Assignment:
    CPU_time = 0
    GPU_time = 0
    Ini_time = 0
    repeat = 100
    k = 0
    path = ""
    is_directed = True
    filename = ""

    _CPU_finished = False
    _GPU_finished = False
    dic = {}

    priority = 0


    def get_info(self):
        dic = {}
        with open(self.path) as file:
            dic["vexNum"]=int(file.readline());
            dic["edgeNum"] = 0;
            for line in file: dic["edgeNum"] += 1

        if (re.search(r'undirected',self.filename) != None): self.is_directed = False
        return dic

    def _predict_run_time(self):
        self.dic = self.get_info()
        model = models.load_model("./control_model/prediction/IniTime.h5")
        self.Ini_time = model.predict([[self.k,self.dic["vexNum"],self.dic["edgeNum"]]])
        model = models.load_model("./control_model/prediction/CPUTime.h5")
        self.CPU_time = model.predict([[self.k,self.dic["vexNum"],self.dic["edgeNum"]]])
        model = models.load_model("./control_model/prediction/GPUTime.h5")
        self.GPU_time = model.predict([[self.k,self.dic["vexNum"],self.dic["edgeNum"]]])

    async def run_CPU(self,id,que_CPU_res,que_GPU_task,is_test = 0,cnt_CPU=0):
        # print("haha")
        if(is_test == 1):
            cmd = "python ./control_model/sleep.py"
            p = subprocess.Popen(cmd, shell=True)
            while True:
                await asyncio.sleep(1)
                if p.poll() != None:
                    que_CPU_res.put(id)
                    self.write_log("000004","no." + str(cnt_CPU) + " CPU task is finished and recycle CPU resource ...")
                    que_GPU_task.put(self)
                    break
            return p

        if(self.is_directed) :
            isDirect = ""
        else :
            isDirect = " -u"

        result_path = os.path.abspath(os.path.join(os.getcwd(),"./result"))
        os.system("mkdir "+result_path+"/"+self.filename)
        result_path = os.path.join(result_path,self.filename)

        cmd = exec_CPU+" -i " + self.path+" -s " + str(self.k) + " -r " + str(self.repeat)+" -o "+ \
            result_path + " -g " + str(0) + isDirect +" >"+result_path+"/CPUlog"
        # print("run CPU:"+cmd)
        p = subprocess.Popen(cmd,shell=True)
        while True:
            await asyncio.sleep(1)
            if p.poll() != None:
                que_CPU_res.put(id)
                self.write_log("000004", "no." + str(cnt_CPU) + " CPU task is finished and recycle CPU resource ...")
                que_GPU_task.put(self)
                break
        return p

    async def run_GPU(self,GPUID,que,is_test = 0,cnt_GPU=0):
        if(is_test == 1):
            cmd = "python ./control_model/sleep.py"
            p = subprocess.Popen(cmd, shell=True)
            while True:
                await asyncio.sleep(1)
                if p.poll() != None:
                    que.put(GPUID)
                    self.write_log("000014","no." + str(cnt_GPU) + " GPU task is finished and recycle GPU resource ...")
                    break;
            return p

        if (self.is_directed):
            isDirect = ""
        else:
            isDirect = " -u"

        result_path = os.path.abspath(os.path.join(os.getcwd(), "./result"))
        # os.system("mkdir " + result_path + "/" + self.filename)  #because run_CPU has mkdir
        result_path = os.path.join(result_path, self.filename)

        cmd = exec_GPU + " -i " + self.path + " -s " + str(self.k) + " -r " + str(self.repeat) + " -o " + \
              result_path + " -g " + str(GPUID) + isDirect + " >>" + result_path + "/GPUlog"
        print("run GPU:"+cmd)
        p = subprocess.Popen(cmd, shell=True)
        while True:
            await asyncio.sleep(1)
            if p.poll() != None:
                que.put(GPUID)
                self.write_log("000014", "no." + str(cnt_GPU) + " GPU task is finished and recycle GPU resource ...")
                break;
        return p

    def __init__(self,path,k=4,repeat=100,priority_method = 0):
        self.k = k
        self.repeat = repeat
        self.path = os.path.abspath(os.path.join(os.getcwd(),path))
        self.filename = self.path.split('/')[-1]
        # self._predict_run_time()

        # self.cal_priority(priority_method)

    def __lt__(self, other):
        return self.priority < other.priority;


    def cal_priority(self,method = 0):
        if method == 0 :
            self.priority = 0;
        elif method == 1:
            maxi = 0;
            pos = 0;
            for i in range(len(self.CPU_time)):
                if self.CPU_time[i] > maxi :
                    maxi =self.CPU_time
                    pos = i;
            self.priority = pos
        # elif method == 2:

    def write_log(self,typeid,contain):
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pipe = open("./pipe.txt","a")
        pipe.write(curtime+"|"+typeid+"|"+contain+"\n")
        print(curtime+"|"+typeid+"|"+contain)
        pipe.close()
        # self.info_que.put([curtime,typeid,contain])



class Manager:
    GPU_Num = 3
    CPU_Num = 4
    is_test = 0

    waitlist_CPU = PriorityQueue()
    waitlist_GPU = PriorityQueue()

    resource_CPU = Queue(maxsize=CPU_Num)
    resource_GPU = Queue(maxsize=GPU_Num)

    info_que = Queue(10)

    cnt_CPU = 0
    cnt_GPU = 0

    async def _get_CPU(self):
        while(self.resource_CPU.empty()):
            await asyncio.sleep(1)
        tmp = self.resource_CPU.get()
        return tmp

    def _free_CPU(self,id = 0):
        self.resource_CPU.put(id)

    async def _get_GPU(self):
        while(self.resource_GPU.empty()):
            await asyncio.sleep(1)
        return self.resource_GPU.get()

    def _free_GPU(self,id):
        self.resource_GPU.put(id)

    def add_CPU_task(self,task):
        # self.write_log("0000",task.path)
        self.waitlist_CPU.put(task)

    def add_GPU_task(self,task):
        self.waitlist_GPU.put(task)

    async def _get_CPU_task(self):
        while(self.waitlist_CPU.empty()):
            await asyncio.sleep(1)
        return self.waitlist_CPU.get()

    async def _get_GPU_task(self):
        while(self.waitlist_GPU.empty()):
            await asyncio.sleep(1)
        return self.waitlist_GPU.get()

    def _init_task(self):
        # self.waitlist_CPU.p
        with open("./task/task1.txt", "r") as r:
            for line in r:
                line = line[0:-1]
                line = line.split(" ")
                item = Assignment(path=line[0], k=int(line[1]), repeat=int(line[2]))
                # print(line[0])
                self.add_CPU_task(item)

    def _init_thread(self):
        for i in range(self.CPU_Num):
            self.resource_CPU.put(i)
        for i in range(self.GPU_Num):
            self.resource_GPU.put(i)

    def __init__(self,GPU_Num = 1,CPU_Num = 4,is_test = 0):
        pipe = open("./pipe.txt","w")
        pipe.close()

        self.is_test = is_test;
        self.CPU_Num=CPU_Num;
        self.GPU_Num=GPU_Num;

        self._init_thread()
        self._init_task()
        #
        # self.write_log("123","321")

    async def run_CPU(self):
        while(True):
            self.write_log("000001", "no."+str(self.cnt_CPU)+" CPU task is wating assignment...")
            task = await self._get_CPU_task()
            self.write_log("000002", "no."+str(self.cnt_CPU) + " CPU task got assignment and wating for rest CPU resource...")
            id = await self._get_CPU()
            self.write_log("000003", "no."+str(self.cnt_CPU) + " CPU task got CPU resource, now begin solve...")
            asyncio.create_task(task.run_CPU(id,self.resource_CPU,self.waitlist_GPU,is_test=self.is_test,cnt_CPU=copy.deepcopy(self.cnt_CPU)))
            self.cnt_CPU += 1

    async def run_GPU(self):
        while(True):
            self.write_log("000011", "no."+str(self.cnt_GPU) + " GPU task is wating assignment...")
            task = await self._get_GPU_task()
            self.write_log("000012", "no."+str(self.cnt_GPU) + " GPU task got assignment and wating for rest CPU resource...")
            id = await self._get_GPU()
            self.write_log("000013", "no."+str(self.cnt_GPU) + " GPU task got CPU resource, now begin solve...")
            asyncio.create_task(task.run_GPU(id,self.resource_GPU,is_test=self.is_test,cnt_GPU=copy.deepcopy(self.cnt_GPU)))
            self.cnt_GPU += 1

    def write_log(self,typeid,contain):
        curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pipe = open("./pipe.txt","a")
        pipe.write(curtime+"|"+typeid+"|"+contain+"\n")
        print(curtime+"|"+typeid+"|"+contain)
        pipe.close()
        # self.info_que.put([curtime,typeid,contain])
        # print(self.info_que.qsize())


    async def main(self):
        CPU = asyncio.create_task(self.run_CPU())
        GPU = asyncio.create_task(self.run_GPU())
        await CPU
        await GPU











