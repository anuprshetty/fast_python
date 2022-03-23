import time
import concurrent.futures


start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	return f'Done sleeping {seconds} second(s)...'


print("Approach-1")
max_sleep_seconds = 10

with concurrent.futures.ThreadPoolExecutor() as executor:
	futures = [executor.submit(do_something, sleep_second) for sleep_second in range(max_sleep_seconds, 0, -1)]

	for future in concurrent.futures.as_completed(futures):
		print(future.result())

print("Approach-2")
sleep_seconds = [second for second in range(10, 0, -1)]

with concurrent.futures.ThreadPoolExecutor() as executor:
	results = executor.map(do_something, sleep_seconds)

	for result in results:
		print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
