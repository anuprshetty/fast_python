import asyncio


async def print_text(text):
	print(text)
	await asyncio.sleep(5)
	print('print_text finished')

	return "text is printed"


# async method
async def main():
	print("Anup")

	# task is a future in Python
	task = asyncio.create_task(print_text("Shetty"))
	print(f"type of task: {type(task)}")  # <class '_asyncio.Task'>
	await asyncio.sleep(2)
	print('main sleep completed')
	task_return_value = await task
	print('main finished')
	print(f"task_return_value: {task_return_value}")


# async method when called returns a coroutine. i.e., main() --> <class 'coroutine'>
# coroutine --> cooperative routine
asyncio.run(main())
