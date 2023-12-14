import time
import asyncio
import requests

async def function1():
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fimages%2Fstock%2Fhigh-resolution&psig=AOvVaw3f9bTiKtI5ryqPJ_kfTesV&ust=1699448579869000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiQlLr5sYIDFQAAAAAdAAAAABAE"
    response = requests.get(url) 
    open("img1","wb").write(response.content)
    print("function1")
    return "abhi"
    
async def function2():
    url = "https://images.unsplash.com/photo-1693834794043-99bb76f267d0?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fHw%3D"
    response = requests.get(url) 
    open("img2","wb").write(response.content)
    
    print("function2")
    
async def function3():
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbig%2520size%2F&psig=AOvVaw3f9bTiKtI5ryqPJ_kfTesV&ust=1699448579869000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiQlLr5sYIDFQAAAAAdAAAAABAZ"
    response = requests.get(url) 
    open("img3","wb").write(response.content)
    print("function3")
    
async def main():   
    L = await asyncio.gather(
            function1(),
            function2(),
            function3(),
)
    print(L)
async def main(): 
    task = asyncio.create_task(function1())   
    # await function1()
    await function2()
    await function3()
    
asyncio.run(main())