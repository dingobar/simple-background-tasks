from backgroundtask import BackgroundTask


class PrintMessage(BackgroundTask):
    async def task(self, message) -> None:
        print(message)
