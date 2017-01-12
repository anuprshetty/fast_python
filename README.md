# Fast Python

Multi threading, multi processing and event loop in Python.

## asyncio

- Python framework enabling asynchronous single threaded concurrent code using coroutines.
- Goal of asyncio: maximize the usage of a single thread by handling I/O asynchronously, and by enabling concurrent code using coroutines.
- asyncio enables single threaded programs to be more productive by filling the gaps that would otherwise be wasted on waiting on I/O. To do this efficiently asyncio avoids blocking functions. And instead uses coroutines which can be executed in small chunks concurrently.
- concurrency is dealing with many things at the same time while being able to do only one thing at a time.
- On very I/O heavy workloads, asyncio can be orders of magnitude faster than blocking I/O. This is why so many important web technologies are built using asyncio like nginx, redis, node.js, browser, etc.

### event loop

- what an event loop is doing? It's calling callbacks in some order one by one.
