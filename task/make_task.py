import os

w = open("task1.txt","w")
data_path =os.path.abspath(os.path.join(os.getcwd(),"../tmp"))
for file in os.listdir(data_path):
    file_path = os.path.join(data_path,file)
    k = 4
    repeat = 100
    w.write(file_path+" "+str(k)+" "+str(repeat)+"\n")
