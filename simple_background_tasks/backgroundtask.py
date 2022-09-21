import asyncio
import logging
from time import time
from typing import Any, Awaitable, Callable

logger = logging.getLogger(__name__)


class BackgroundTask:
    """Takes a coroutine task as an input, call with asyncio.create_task(task.start())."""

    task: Callable[..., None]
    interval: int | float
    name: str
    task_kwargs: dict[str, Any]

    def __init__(
        self,
        task: Callable[..., Awaitable],
        interval: int | float = 5,
        name: str | None = None,
        **task_kwargs: Any
    ) -> None:
        """Initialize task instance.

        Args:
            task (Callable[..., None]): Callable that is run in the background. Can be any callable
                object like functions or class methods. Required.
            interval (int | float, optional): Passed to await asyncio.sleep()
                between task invocations. Defaults to 5.
            name (str, optional): Name of the task for logging purposes. Defaults to the class name.
            task_kwargs: kwargs passed to the task when it is invoked. Can also be passed to start()
                or run_once().
        """
        self.task = task  # type: ignore [assignment]
        self.interval = interval
        self.name = name if name else str(self.__class__.__name__)
        self.task_kwargs = task_kwargs
        self.task

    async def run_once(self, *args, **kwargs):
        """Run the task once.

        Args:
            args: Arguments to pass to the task.
            kwargs: Keyword arguments to pass to the task.
        """
        logger.debug('Running task "%s"', self.name)
        t0 = time()
        try:
            await self.task(*args, **kwargs, **self.task_kwargs)
            logger.debug('Finished task "%s" in %4fs', self.name, time() - t0)
        except Exception as e:
            logger.exception('Task "%s" failed with error %s', self.name, repr(e))

    async def start(self, *args, **kwargs) -> None:
        """Run the task with the configured interval for the task.

        Args:
            args: Arguments to pass to the task.
            kwargs: Keyword arguments to pass to the task.
        """
        while True:
            await self.run_once(*args, **kwargs)
            await asyncio.sleep(self.interval)
