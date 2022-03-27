from abc import ABC, abstractmethod
import asyncio
import logging
from time import time

logger = logging.getLogger()


class BackgroundTask(ABC):
    """Abstract class for a background task

    Implement the async method task(*args, **kwargs).
    """

    interval: int
    name: str

    def __init__(self, interval=None, name=None) -> None:
        """Initialize background task

        Parameters
        ----------
        interval : int, optional
            Seconds between executions, if None runs only once
        name : str, optional
            Name of the task, by default instance.__class__.__name__
        """
        self.interval = interval if interval else 5
        self.name = name if name else str(self.__class__.__name__)

    async def run_task(self, *args, **kwargs):
        logger.debug('Running task "%s"', self.name)
        t0 = time()
        try:
            await self.task(*args, **kwargs)
            logger.debug('Finished task "%s" in %4fs', self.name, time() - t0)
        except Exception as e:
            logger.exception('Task "%s" failed with error %s', self.name, repr(e))

    async def run_scheduled(self, *args, **kwargs) -> None:
        while True:
            await self.run_task(*args, **kwargs)
            await asyncio.sleep(self.interval)

    async def run(self, *args, **kwargs) -> None:
        if self.interval:
            await self.run_scheduled(*args, **kwargs)
        else:
            await self.run_task(*args, **kwargs)

    @abstractmethod
    async def task(*args, **kwargs) -> None:
        pass
