from typing import Optional

import aiohttp


async def get(url: str, headers: Optional[dict] = None):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            return await resp.json()


async def get_text(url: str, headers: Optional[dict] = None):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            return await resp.text()
