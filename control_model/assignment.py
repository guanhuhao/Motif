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

    def run_CPU(self):
        if(self.is_directed) : isDirect = " -u"
        else : isDirect = ""

        result_path = os.path.abspath(os.path.join(os.getcwd(),"../result"))
        os.system("mkdir "+result_path+"/"+self.filename)
        result_path = os.path.join(result_path,self.filename)

        cmd = exec_CPU+" -i " + self.path+" -s " + str(self.k) + " -r " + str(self.repeat)+" -o "+ \
            result_path + " -g " + str(0) + isDirect +" >"+result_path+"/CPUlog"
        print(cmd)
        p = subprocess.Popen(cmd,shell=True)

    def run_GPU(self):
        if (self.is_directed):
            isDirect = " -u"
        else:
            isDirect = ""

        result_path = os.path.abspath(os.path.join(os.getcwd(), "../result"))
        # os.system("mkdir " + result_path + "/" + self.filename)  #because run_CPU has mkdir
        result_path = os.path.join(result_path, self.filename)

        cmd = exec_GPU + " -i " + self.path + " -s " + str(self.k) + " -r " + str(self.repeat) + " -o " + \
              result_path + " -g " + str(0) + isDirect + " >>" + result_path + "/GPUlog"
        print(cmd)
        p = subprocess.Popen(cmd, shell=True)

    def __init__(self,path,k=4,repeat=100):
        self.k = k
        self.repeat = repeat
        self.path = os.path.abspath(os.path.join(os.getcwd(),path))
        self.filename = self.path.split('/')[-1]
        print(self.path)
        print (self.filename)

        self._predict_run_time()


class Manager:
    THREAD_POOL_SIZE = 4

    def _init_thread(self):
        self.thread_queue = Queue(maxsize=self.THREAD_POOL_SIZE)

    def _init_task(self):
        self.task_queue = Queue()

    def __init__(self):
        self._init_thread()
        self._init_task()








