import discord
import aiohttp
import calendar
from discord.ext import commands
from datetime import datetime
from io import BytesIO
from PIL import Image

channel_id = ''
token = ''
file_path = ''


bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if len(message.attachments) == 1 and message.channel.id == channel_id:
        img_url = message.attachments[0]['url']
        async with aiohttp.ClientSession() as ses:
            async with ses.get(img_url) as r:
                img = await r.read()

        image = Image.open(BytesIO(img))

        d = datetime.utcnow()
        unixtime = calendar.timegm(d.utctimetuple())

        image.save(f'{file_path}raidscreen_{unixtime}_9999_9999_99.png')


bot.run(token)