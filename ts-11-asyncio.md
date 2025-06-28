/ [Home](index.md) / [KactSay](kactsay.md)

# KactSay Tech: Asyncio


1. This module allows you to write concurrent,single threaded code in Python without relying on any third-party libraries

2. AsyncIO is a relatively new framework to achieve concurrency in python.

3. Multithreading is usually preferred for network I/O or disk I/O as threads need not compete hard among themselves for acquiring GIL.

4. AsyncIO is a single thread single process cooperative multitasking.

5. An asyncio task has exclusive use of CPUuntil it wishes to give it up to the coordinator or event loop.

6. Unlike a conventional function with a single point of exit,a coroutine can pause and resume its execution.

7. Using asyncio.gather to create multiple tasks in one shot.

8. An asyncio task has an exclusive right to use CPU until it volunteers to give up.

9. If by mistake a blocking call sneaks into your task, it is going to stall the progress of the program.

10. By default, the number of processes is equal to the number of processors on the machine.



#### src:
```
https://markuseliasson.se/article/introduction-to-asyncio/
https://medium.com/analytics-vidhya/asyncio-threading-and-multiprocessing-in-python-4f5ff6ca75e8
```