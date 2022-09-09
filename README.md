# Background tasks with asyncio

The idea is to inherit from `BackgroundTask` and implement `async def task(*args, **kwargs)`. Then
`await asyncio.create_task(task.start())` will start execution.
