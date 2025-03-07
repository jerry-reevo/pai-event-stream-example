import asyncio
from typing import Any

class AsyncIteratorProxy:
    def __init__(self, queue: asyncio.Queue):
        self._queue = queue

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        try:
            value = await self._queue.get()
            if value is None:
                raise StopAsyncIteration
            return value
        except asyncio.CancelledError:
            raise StopAsyncIteration
        except Exception:
            raise

    async def emit(self, event: Any):
        await self._queue.put(event)

    async def close(self):
        await self._queue.put(None)
