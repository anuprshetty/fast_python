import os
import time
import concurrent.futures


global_a = 5
global_b = 6


def do_something(seconds):
	print(f'Task({seconds}) ... started')

	# # CPU bound
	# cpu_execution_time = time.process_time() + seconds
	# while time.process_time() < cpu_execution_time:
	# 	a = 4
	# 	b = 3
	# 	a, b = b, a
	# 	global global_a
	# 	global global_b
	# 	global_a = a
	# 	global_b = b

	# IO bound
	time.sleep(0.1)

	return f'Task({seconds}) ... DONE'


def create_threads(thread_sleep_seconds):
	with concurrent.futures.ThreadPoolExecutor() as thread_executor:
		thread_results = thread_executor.map(do_something, thread_sleep_seconds)

		# NOTE: If a function raises an exception, 'concurrent.futures' won't raise that exception while running the thread. The exception will be raised when it's return value is retrieved.
		try:
			return list(thread_results)
		except Exception as e:
			print(f"Error: function thrown an exception: {e}")


cpu_count = os.cpu_count()
process_count = cpu_count
thread_count = process_count * 5
task_count = 10
process_list = []
for process_index in range(process_count):
	thread_list = []
	for thread_index in range(thread_count):
		for task_index in range(task_count):
			task = (process_index * thread_count * task_count) + (thread_index * task_count) + task_index
			thread_list.append(task)
	process_list.append(thread_list)

print(process_list)

with concurrent.futures.ProcessPoolExecutor() as process_executor:
	process_results = process_executor.map(create_threads, process_list)

	# NOTE: If a function raises an exception, 'concurrent.futures' won't raise that exception while running the process. The exception will be raised when it's return value is retrieved.
	try:
		for thread_results in process_results:
			for thread_result in thread_results:
				print(thread_result)
	except Exception as e:
		print(f"Error: function thrown an exception: {e}")
