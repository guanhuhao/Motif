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
            if contain == None or contain =='' :continue;
            break
        print(contain)
        # break


# asyncio.run(main())

loop = asyncio.get_event_loop()
print(321)
a = loop.create_task(main())
# loop.run_until_complete(a)
loop.run_forever()
print(123)
