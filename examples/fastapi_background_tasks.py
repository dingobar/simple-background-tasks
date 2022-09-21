"""Run a fastapi app with recurring scheduled background tasks.

uvicorn examples.fastapi_background_tasks:app
"""

import asyncio
import logging

from fastapi import FastAPI  # type: ignore [import]

from examples import tasks as example_tasks
from simple_background_tasks import BackgroundTask

logging.basicConfig(
    format="%(asctime)s %(levelname)8s %(name)25s - %(message)s", level=logging.DEBUG
)

app = FastAPI()


@app.on_event("startup")
async def init():
    """This code runs before the API starts."""
    await init_tasks()


async def init_tasks():
    """Start backgrount tasks using simple-background-tasks."""
    tasks = [
        BackgroundTask(example_tasks.check_weather_in_bangkok),
        BackgroundTask(example_tasks.print_message, 1, message="One second passed, omg"),
        BackgroundTask(example_tasks.print_message, 3, message="All good things come in threes"),
    ]
    for task in tasks:
        asyncio.create_task(task.start())


@app.get("/")
async def read_root() -> dict:
    """Root path.

    Returns:
        dict: Dict that says "Hello World" or something idk.
    """
    return {"Hello": "World"}
