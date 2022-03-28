# Incomplete code. Exploration needed.
import asyncio


async def print_text(text):
	print(text)
	await asyncio.sleep(5)
	print('print_text finished')


async def main():
	print("Anup")
	# await foo("Shetty")
	task = asyncio.create_task(print_text("Shetty"))
	await asyncio.sleep(2)
	print('main sleep completed')
	await task
	print('main finished')


asyncio.run(main())
