import multiprocessing
import time


global_a = 5
global_b = 6

start = time.perf_counter()


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

	print(f'Done sleeping {seconds} second(s)...')


processes_count = 32
processes = []
sleep_seconds = 5

for _ in range(processes_count):
	process = multiprocessing.Process(target=do_something, args=(sleep_seconds,))
	process.start()
	processes.append(process)

# There is no straight forward way to get the return value of the function via 'multiprocessing' module.
# Use 'concurrent.futures' module instead.
for process in processes:
	process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
