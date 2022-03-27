import asyncio
from typing import List
from backgroundtask import BackgroundTask
from tasks.check_weather import CheckWeather

from tasks.print_hello import PrintMessage

import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)8s %(name)25s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger()


async def main():

    # Make a list of tasks with arguments to constructor, and run them with a loop

    tasks: List[BackgroundTask] = []
    tasks.append(PrintMessage(interval=5, message="Hello!"))
    tasks.append(PrintMessage(interval=2, message="Good bye."))
    tasks.append(CheckWeather(interval=10, name="Check the weather in Bangkok"))

    for task in tasks:
        asyncio.create_task(task.run())

    # Run just one task and pass arguments to .run()

    asyncio.create_task(PrintMessage(interval=7).run("How are you?"))

    while True:
        await asyncio.sleep(60)
        logger.info("I'm still alive")


if __name__ == "__main__":
    asyncio.run(main())
