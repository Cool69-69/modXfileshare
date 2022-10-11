import aiohttp
import asyncio
import os

####################  Tnlink  ####################

async def get_shortlink(link):
    https = link.split(":")[0]
    if "http" == https:
        https = "https"
        link = link.replace("http", https)
    url = f'https://tnlink.in/api'
    params = {'api': '5cc7e548ecb43e7cd19b8c9a6d20963cd49afeb2',
              'url': link,
              }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            if data["status"] == "success":
                return data['shortenedUrl']
            else:
                return f"Error: {data['message']}"
