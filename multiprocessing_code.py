import multiprocessing
import time

start = time.perf_counter()


def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done sleeping...')


processes_count = 10
processes = []

for _ in range(processes_count):
	process = multiprocessing.Process(target=do_something)
	process.start()
	processes.append(process)

for process in processes:
	process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
