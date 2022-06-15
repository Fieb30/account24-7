import discord, os, keep_alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(command_prefix=':', self_bot=True)



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=alse)
