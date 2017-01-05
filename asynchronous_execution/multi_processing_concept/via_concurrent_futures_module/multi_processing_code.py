import time
import concurrent.futures


global_a = 5
global_b = 6


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')

	# CPU bound
	cpu_execution_time = time.process_time() + seconds
	while time.process_time() < cpu_execution_time:
		a = 4
		b = 3
		a, b = b, a
		global global_a
		global global_b
		global_a = a
		global_b = b

	# # IO bound
	# time.sleep(seconds)

	return f'Done sleeping {seconds} second(s)...'


print("\nApproach-1\n")

start = time.perf_counter()

max_sleep_seconds = 10

# NOTE: when we are using context manager, it will automatically join all the processes before exiting the context manager. i.e., context manager will wait for all the processes to complete their execution before exiting from the context manager.
with concurrent.futures.ProcessPoolExecutor() as executor:
	futures = [executor.submit(do_something, sleep_second) for sleep_second in range(max_sleep_seconds, 0, -1)]

	for future in concurrent.futures.as_completed(futures):

		# NOTE: If a function raises an exception, 'concurrent.futures' won't raise that exception while running the process. The exception will be raised when it's return value is retrieved.
		try:
			print(future.result())
		except Exception as e:
			print(f"Error: function thrown an exception: {e}")

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

print("\nApproach-2\n")

start = time.perf_counter()

sleep_seconds = [second for second in range(10, 0, -1)]


with concurrent.futures.ProcessPoolExecutor() as executor:
	results = executor.map(do_something, sleep_seconds)

	# NOTE: If a function raises an exception, 'concurrent.futures' won't raise that exception while running the process. The exception will be raised when it's return value is retrieved.
	try:
		for result in results:
			print(result)
	except Exception as e:
		print(f"Error: function thrown an exception: {e}")

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
