import os
import re
import random
cur_path = os.getcwd() #获取当前文件绝对路径
raw_dataDir = os.path.join(cur_path,"raw_data")

for file in os.listdir(raw_dataDir):
    data = []
    dic = {}
    tot = 0
    cnt = 0
    flag = 0
    istext = ""
    if(re.match("(.*).txt",file)) :
        print("now solve "+file)
        with open(raw_dataDir+"/"+file,"r") as f:
            for line in f :
                if line[0] == '#' :
                    if re.search(r'(.*)Directed(.*)',line) !=None :
                        flag = 1
                    continue
                edge = re.split(r'[ \n\t]',line)
                edge.pop()

                if dic.get(edge[0]) == None :
                    tot += 1
                    dic[edge[0]] =  tot

                if dic.get(edge[1]) == None :
                    tot += 1
                    dic[edge[1]] =  tot

                data += [dic[edge[0]],dic[edge[1]]]
                cnt += 1
                # if cnt%1000 == 0 : print(cnt)
            if flag == 0 : mark = "undirected"
            else : mark = "directed"
    elif(re.match(r"(.*).csv",file)):
        print("now solve "+file)
        istext = ".txt"
        with open(raw_dataDir+"/"+file,"r") as f:
            for line in f:
                edge = line.split(',')
                if edge[0].isdigit() == False : continue
                if dic.get(edge[0]) == None:
                    tot += 1
                    dic[edge[0]] = tot

                if dic.get(edge[1]) == None:
                    tot += 1
                    dic[edge[1]] = tot

                data += [dic[edge[0]], dic[edge[1]]]
                cnt += 1
                # if cnt%1000 == 0 : print(cnt)
            if flag == 0:
                mark = "undirected"
            else:
                mark = "directed"
            flag2 = 0
            with open(cur_path + "/data/" + mark + "-" + str(tot) + "-" + file+".txt", "w") as w:
                print(cur_path + "/data/" + mark + "-" + str(tot) + "-" + file+".txt")
                w.write(str(tot) + "\n")
                for item in data:
                    w.write(str(item))
                    if flag2 == 0:
                        w.write(' ')
                    else:
                        w.write('\n')
                    flag2 = (flag2 + 1) % 2
    print(data)

    # with open(cur_path+"/data/"+mark+"-"+str(tot)+"-"+file+istext,"w") as w:
    #     print(cur_path+"/data/"+mark+"-"+str(tot)+"-"+file)
    #     w.write(str(tot)+"\n")
    #     flag=0
    #     for item in data:
    #         w.write(str(item))
    #         if flag2 == 0 :
    #             w.write(' ')
    #         else :
    #             w.write('\n')
    #         flag2 = (flag2 + 1)% 2

def baseline(data):
    with open(cur_path+"/data/"+mark+"-"+str(tot)+"-"+file+istext,"w") as w:
        print(cur_path+"/data/"+mark+"-"+str(tot)+"-"+file)
        w.write(str(tot)+"\n")
        flag=0
        for item in data:
            w.write(str(item))
            if flag2 == 0 :
                w.write(' ')
            else :
                w.write('\n')
            flag2 = (flag2 + 1)% 2

def deleteEdge(data,rate):
    with open(cur_path+"/data/"+mark+"-"+str(tot)+"-"+file+istext,"w") as w:
        print(cur_path+"/data/"+mark+"-"+str(tot)+"-"+file)
        w.write(str(tot)+"\n")
        flag=0
        for i in range(len(data),step=2):
            if random.random() < rate : continue;
            w.write(str(data[i])+" "+str(data[i+1])+"\n")

def AddEdge(data,rate,mark):
    dic = {}
    for i in range(len(data), step=2):
        dic[(data[i],data[i+1])] = 1
        if mark == "undirected" :
            dic[(data[i+1], data[i])] = 1

    cnt = data.






        


        