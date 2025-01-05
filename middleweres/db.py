from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message

class CounterMiddlewere(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call_(
        self,
        handler: callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        self.counter += 1
        data['counter'] == self.counter
        return await handler(event, data)