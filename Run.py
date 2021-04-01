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
        for i in range(4):
            if psutil.pid_exists(int(dic[i])) == False:
                GPUid = i
                flag = 1
                break
        if flag==1 : break
        time.sleep(10)
    exe_path = "./gpuNemo"
    data_path = os.path.join(dataDir_path,filename)
    motif_k = 4
    repeat = 100
    # GPUid = 0
    result_path = re.search(r'(.*)\.txt',filename)
    isDirected = " -u"
    if(re.search(r'undirected',filename)==None) : isDirected = ""
    if(result_path == None) : continue
    else : result_path = "result/"+str(motif_k)+"-"+result_path.group(1)

    if os.system("mkdir "+result_path) == 1 : continue

    # print("nohup /home/guan/cuda/bin/nvprof "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+isDirected+" > "+result_path+"/log 2>&1 &\n")
    # os.system("nohup /home/guan/cuda/bin/nvprof "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+isDirected+" > "+result_path+"/log 2>&1 &")

    # print("nohup "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+" >"+result_path+"/log"+isDirected+" 2>&1 &\n")
    os.system("nohup "+exe_path+" -i "+data_path+" -s "+str(motif_k)+" -r "+str(repeat)+" -o "+result_path+" -g "+str(GPUid)+" >"+result_path+"/log"+isDirected+" 2>&1 &")
    time.sleep(10)
    path_tmp = os.path.join(os.getcwd(),result_path)
    path_tmp = os.path.join(path_tmp,"log")
    with open("./"+result_path+"/log","r") as r:
        line = r.read()
        pid = re.search(r'==(.*)==(.*)',line).group(1)
        dic[GPUid] = pid
    print("now assign "+result_path+" to GPU:"+str(GPUid)+" Pid:"+pid+"\n")

print("\nfinished\n")
