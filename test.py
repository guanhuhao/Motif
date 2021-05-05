import time

cnt = 0;
w = open("test.txt", "w")
w.close()
while(True):
    time.sleep(1)
    w = open("test.txt", "a")
    w.write(str(cnt+1)+"\n")
    w.close()
    print(str(cnt+1))
    cnt += 1
w.close()
