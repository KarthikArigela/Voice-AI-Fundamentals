import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

## Example 1 ##

# def fetch_data(param):
#     print(f"Do something with {param}...")
#     time.sleep(param)
#     print(f"Done with {param}")
#     return f"Result of {param}"


# def main():
#     result1 = fetch_data(1) # Sync function
#     print("Fetch 1 fully completed")
#     result2 = fetch_data(2) # Sync function
#     print("Fetch 2 fully completed")
#     return [result1, result2]

# t1 = time.perf_counter()

# results = main()
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")

## Example 2 ##

# async def fetch_data(param):
#     print(f"Do something with {param}...")
#     await asyncio.sleep(param)
#     print(f"Done with {param}")
#     return f"Result of {param}"

# async def main():
#     task1 = fetch_data(1)  # Sync function only. No prior scheduling
#     task2 = fetch_data(2)  # Sync function only. No prior scheduling
#     result1 = await task1  # Scheduled and Executed at the same time
#     print("Task 1 fully completed")
#     result2 = await task2  # Scheduled and Executed at the same time
#     print("Task 2 fully completed")
#     return [result1, result2]

# t1 = time.perf_counter()

# results = asyncio.run(main())
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")

## Example 3 ##

# async def fetch_data(param):
#     print(f"Do something with {param}...")
#     await asyncio.sleep(param)
#     print(f"Done with {param}")
#     return f"Result of {param}"


# async def main():
#     task1 = asyncio.create_task(fetch_data(1)) # task1 Scheduled 
#     task2 = asyncio.create_task(fetch_data(2)) # task2 Scheduled
#     result1 = await task1                      # task1 executed
#     print("Task 1 fully completed")
#     result2 = await task2                      # task2 continued execution
#     print("Task 2 fully completed")
#     return [result1, result2]


# t1 = time.perf_counter()

# results = asyncio.run(main())
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")

## Example 4 ##

# async def fetch_data(param):
#     print(f"Do something with {param}...")
#     await asyncio.sleep(param)
#     print(f"Done with {param}")
#     return f"Result of {param}"


# async def main():
#     task1 = asyncio.create_task(fetch_data(1)) # task1 Scheduled
#     task2 = asyncio.create_task(fetch_data(2)) # task2 Scheduled
#     result2 = await task2                      # task1 execute first because task1 is first in fifo sequence and will not stop until task2 is done
#     print("Task 2 fully completed")
#     result1 = await task1                      # Just returns the result from task1 already executed
#     print("Task 1 fully completed")            
#     return [result1, result2]


# t1 = time.perf_counter()

# results = asyncio.run(main())
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")

## Example 5 ##

# async def fetch_data(param):
#     print(f"Do something with {param}...")
#     time.sleep(param)
#     print(f"Done with {param}")
#     return f"Result of {param}"


# async def main():
#     task1 = asyncio.create_task(fetch_data(1)) # task1 Scheduled
#     task2 = asyncio.create_task(fetch_data(2)) # task2 Scheduled
#     result1 = await task1                      # task1 starts executing and as sleep is sync function, blocking happens and task1 is fully completed
#     print("Task 1 fully completed")            # But since task2 is in fifo sequence before the main function again in the queue, task2 gets triggered with blocking sleep sync function before this print statement/returning to main
#     result2 = await task2                      # Just returns the result from task2 already executed
#     print("Task 2 fully completed")
#     return [result1, result2]

# t1 = time.perf_counter()

# results = asyncio.run(main())
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")

## Example 6 ##

# def fetch_data(param):
#     print(f"Do something with {param}...", flush=True)
#     time.sleep(param)
#     print(f"Done with {param}", flush=True)
#     return f"Result of {param}"


# async def main():
#     # Run in Threads
#     task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1)) # task1 Scheduled
#     task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2)) # task2 Scheduled
#     result1 = await task1                                         # task1 triggers a thread inside the async task and the thread works on its own as a seperate async task (Like nested async task)
#     print("Thread 1 fully completed")
#     result2 = await task2                                         # By the time task2 is triggered, task1 internal thread is running and task2 internal thread triggers a nested async task to complete the fetchdata function
#     print("Thread 2 fully completed")

#     # Run in Process Pool
#     loop = asyncio.get_running_loop()

#     with ProcessPoolExecutor() as executor:
#         task1 = loop.run_in_executor(executor, fetch_data, 1) # the same nested async task runs in processpool executor as well for task1
#         task2 = loop.run_in_executor(executor, fetch_data, 2) # and for task2 as well

#         result1 = await task1
#         print("Process 1 fully completed")
#         result2 = await task2
#         print("Process 2 fully completed")

#     return [result1, result2]


# if __name__ == "__main__":
#     t1 = time.perf_counter()

#     results = asyncio.run(main())
#     print(results)

#     t2 = time.perf_counter()
#     print(f"Finished in {t2 - t1:.2f} seconds")

## Example 7 ##

# async def fetch_data(param):
#     await asyncio.sleep(param)
#     return f"Result of {param}"


# async def main():
#     # Create Tasks Manually
#     task1 = asyncio.create_task(fetch_data(1))
#     task2 = asyncio.create_task(fetch_data(2))
#     result1 = await task1
#     result2 = await task2
#     print(f"Task 1 and 2 awaited results: {[result1, result2]}")

#     # Gather Coroutines
#     coroutines = [fetch_data(i) for i in range(1, 3)]
#     results = await asyncio.gather(*coroutines, return_exceptions=True) # triggers async tasks in loop one after the other without prior scheduling 
#     print(f"Coroutine Results: {results}")

#     # Gather Tasks
#     tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]
#     results = await asyncio.gather(*tasks) # triggers async tasks in loop one after the other with prior scheduling
#     print(f"Task Results: {results}")

#     # Task Group
#     async with asyncio.TaskGroup() as tg:
#         results = [tg.create_task(fetch_data(i)) for i in range(1, 3)] # triggers async tasks automatically after the loop ends with prior scheduling
#         # All tasks are awaited when the context manager exits.
#     print(f"Task Group Results: {[result.result() for result in results]}")

#     return "Main Coroutine Done"


# t1 = time.perf_counter()

# results = asyncio.run(main())
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")


# For More clarifications: https://youtu.be/oAkLSJNr5zY?si=WXiqWMZ2w3rj9WNW