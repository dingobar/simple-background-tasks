from backgroundtask import BackgroundTask


class PrintHello(BackgroundTask):
    async def task(*_, **__) -> None:
        print("Hello!")
