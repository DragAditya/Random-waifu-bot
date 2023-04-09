import aiohttp

async def fetch_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data['url']

async def waifu_sfw():
    return await fetch_image('https://api.waifu.pics/sfw/waifu')

async def waifu_nsfw():
    return await fetch_image('https://api.waifu.pics/nsfw/waifu')