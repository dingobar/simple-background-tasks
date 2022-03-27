# Background tasks with asyncio

The idea is to inherit from `BackgroundTask` and implement `async def task(*args, **kwargs)`. Then
`await asyncio.creat_task(task.run())` will start execution.
