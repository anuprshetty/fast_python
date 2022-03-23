import time
import threading


start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	print('Done sleeping...')


threads_count = 10
threads = []
sleep_seconds = 1.5
for _ in range(threads_count):
	thread = threading.Thread(target=do_something, args=[sleep_seconds])
	thread.start()
	threads.append(thread)

for thread in threads:
	thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
