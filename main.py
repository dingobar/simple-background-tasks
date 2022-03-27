import asyncio
from typing import List
from backgroundtask import BackgroundTask
from tasks.check_weather import CheckWeather

from tasks.print_hello import PrintHello

import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)8s %(name)25s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger()


async def main():
    tasks: List[BackgroundTask] = []
    tasks.append(PrintHello(interval=5))
    tasks.append(CheckWeather(interval=10, name="Check the weather in Bangkok"))

    for task in tasks:
        asyncio.create_task(task.run())

    while True:
        await asyncio.sleep(60)
        logger.info("I'm still alive")


if __name__ == "__main__":
    asyncio.run(main())
