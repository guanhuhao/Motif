import asyncio
r = open("./test.txt","r")
async def read():
    while(True) :
        await  asyncio.sleep(1)
        contain = r.read()
        # print(contain)
        if contain == None : continue
        return contain
async def main():
    while (True):
        while(True):
            await  asyncio.sleep(1)
            contain = r.read()
            if contain == None :continue;
            break
        if int(contain) == 10:
            print("haha")

asyncio.run(main())

