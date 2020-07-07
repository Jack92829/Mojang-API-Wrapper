import aiohttp
import asyncio
from .Errors import *


class Request:
    async def get(url, headers=None):
        async with aiohttp.ClientSession() as session:
            return await Response.fetch(session, url, headers)

    async def post(url, payload, headers, data=False):
        async with aiohttp.ClientSession() as session:
            return await Response.send(session, url, payload, headers, data)

    async def put(url, payload, headers):
        async with aiohttp.ClientSession() as session:
            return await Response.hit(session, url, payload, headers)

    async def delete(url, headers):
        async with aiohttp.ClientSession() as session:
            return await Response.take(session, url, headers)


class Response:
    async def fetch(session, url, headers):
        async with session.get(url, headers=headers) as response:
            try:
                response1 = await response.json()
            except:
                response1 = await response.text()
            if response.status not in [200, 204]:
                handle(response1)
            return response1
    
    async def send(session, url, payload, headers, data):
        if data:
            response = await session.post(url, data=payload, headers=headers)
        else:
            response = await session.post(url, json=payload, headers=headers)
        
        try:
            response1 = await response.json()
        except:
            response1 = await response.text()
            
        if response.status not in [200, 204]:
            handle(response1)
        return response1
    
    async def hit(session, url, payload, headers):
        async with session.put(url, json=payload, headers=headers) as response:
            if response.status != 200:
                handle(await response.json())

    async def take(session, url, headers):
        async with session.delete(url, headers=headers) as response:
            if response.status != 200:
                handle(await response.json())