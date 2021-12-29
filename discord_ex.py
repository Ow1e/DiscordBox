import os, sys

from driver import send

import discord
from discord.ext import commands
import properties

client = commands.Bot(command_prefix="box!")

# Checks for key

print("Looking for Key in enviroments")

if os.getenv("DISCORD_KEY") == None:
    sys.exit("Key not found in enviroments")
else:
    discord_key = os.getenv("DISCORD_KEY")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(properties.playing))
    print("Bot is ready for input")

@client.event
async def on_message(message):
    if message.author.nick == None:
        nick = message.author.name
    else:
        nick = message.author.nick
    to_print = (f"[#{message.channel.name} | {message.guild.name}] {nick}: {message.content}")
    send(to_print)

client.run(discord_key)