import os
import re
import time
import psutil
dataDir_path = os.path.join(os.getcwd(),"data")
print(dataDir_path)
dic = {0:0,1:0,2:0,3:0}
for filename in os.listdir(dataDir_path):
    while(1) :
        flag = 0
        for i in range(1):
            if psutil.pid_exists(int(dic[i])) == False:
                GPUid = i
                flag = 1
                break
        if flag==1 : break
        time.sleep(5)

    exe_path = "./gpuNemo"
    data_path = os.path.join(dataDir_path,filename)
    motif_k = 4
    repeat = 100
    # GPUid = 0
    result_path = re.search(r'(.*)\.txt',filename)
    isDirected = " -u"
    if(re.search(r'undirected',filename)==None) : isDirected = ""
    if(result_path == None) : continue
    else : result_path = "result/"+result_path.group(1)

    if os.system("mkdir "+result_path) == 1 : continue
    print("nohup nvprof "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+" >"+result_path+"/log"+isDirected+" 2>&1 &")
    os.system("nohup nvprof "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+" >"+result_path+"/log"+isDirected+" 2>&1 &")
    # os.system("nohup "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+" >"+result_path+"/log"+isDirected+" 2>&1 &")
    time.sleep(1)
    with open(result_path+"/log","r") as r:
        line = r.readline();
        pid = re.search(r'==(.*)==(.*)',line).group(1)
        print(pid)
        dic[GPUid] = pid

