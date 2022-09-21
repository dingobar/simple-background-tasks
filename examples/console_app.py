import asyncio
import logging
from typing import List

from examples import tasks as example_tasks
from simple_background_tasks import BackgroundTask

logging.basicConfig(
    format="%(asctime)s %(levelname)8s %(name)25s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def main():
    """Make a list of tasks with arguments to constructor, and run them with a loop."""
    tasks: List[BackgroundTask] = []
    tasks.append(BackgroundTask(example_tasks.print_message, interval=5, message="Hello!"))
    tasks.append(BackgroundTask(example_tasks.print_message, interval=2, message="Good bye."))
    tasks.append(
        BackgroundTask(
            example_tasks.check_weather_in_bangkok, interval=10, name="Check the weather in Bangkok"
        )
    )
    for task in tasks:
        asyncio.create_task(task.start())

    # Run just one task and pass arguments to .start()
    asyncio.create_task(
        BackgroundTask(example_tasks.print_message, interval=7).start("How are you?")
    )

    # This illustrates that the main app is still running, hence "background" tasks ;)
    while True:
        await asyncio.sleep(60)
        logger.info("I'm still alive running your main application!")


if __name__ == "__main__":
    asyncio.run(main())
