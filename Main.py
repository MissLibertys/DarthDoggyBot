import discord
from discord.ext import commands
import asyncio
import time
from itertools import cycle
import os

client = commands.Bot(command_prefix=("/"))
status = ["testing the bot", "/help"]

async def change_status():
  await client.wait_until_ready()
  msgs = cycle(status)
  
  while not client.is_closed:
    current_status = next(msgs)
    await client.change_presence(game=discord.Game(name=current_status))
    await asyncio.sleep(5)
    
player = {}	

@client.event
async def on_ready():
	print('Logged in as')
	print("User name:", client.user.name)
	print("User id:", client.user.id)
	print('---------------')
    
@client.command(pass_context=True)
async def ping(ctx):
    """Pings the bot and gets a response time."""
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = (time.time() - pingtime) * 1000
    await client.edit_message(pingms, "Pong! :ping_pong: ping time is `%dms`" % ping)
	
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])
