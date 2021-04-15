import os
import re

w = open(os.path.join(os.getcwd(),"Runtime Data.txt"),"w")
def get_file(path):
    # print(path)
    for file in os.listdir(path):
        if(os.path.isdir(os.path.join(path,file))) :
            # print("enter folder:"+file) #进入目录xxx
            get_file(os.path.join(path,file))
            # print("exit folder:"+file) #退出目录xxx
        else :
            # print(file)
            # print(path)
            if file != "log" : continue
            with open(os.path.join(path,file),"r") as r:
                content = r.read()
                # print(content)
                if re.match(r"(.*)Destroying graph",content,flags=re.MULTILINE+re.DOTALL) == None : continue
                k = re.match(r"(.*)Motif Size: ([0-9]+)(.*)",content,flags=re.MULTILINE+re.DOTALL).group(2)
                InitTime = re.match(r"(.*)Init and Load Time: ([-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+))",content,flags=re.MULTILINE+re.DOTALL).group(2)
                CPUTime = re.match(r"(.*)CPU RunTime: ([-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+))",content,flags=re.MULTILINE+re.DOTALL).group(2)
                GPUTime = re.match(r"(.*)GPU Runtime: ([-+]?([0-9]+(\.[0-9]+)?|\.[0-9]+))",content,flags=re.MULTILINE+re.DOTALL).group(2)

                EdgeNum = re.match(r"(.*)Topography of Original Network: (\d+\.\d+|\d+) nodes and (\d+\.\d+|\d+)",content,flags=re.MULTILINE+re.DOTALL).group(2)
                VertNum = re.match(r"(.*)Topography of Original Network: (\d+\.\d+|\d+) nodes and (\d+\.\d+|\d+)",content,flags=re.MULTILINE+re.DOTALL).group(3)
                w.write(k+" "+EdgeNum+" "+VertNum+" "+InitTime+" "+CPUTime+" "+GPUTime+"\n")
                print(k+" "+EdgeNum+" "+VertNum+" "+InitTime+" "+CPUTime+" "+GPUTime+"\n")
                # print(k,InitTime,CPUTime,GPUTime)
                # print(k.group(2))

get_file(os.path.abspath(os.path.join(os.getcwd(),"../../result")))