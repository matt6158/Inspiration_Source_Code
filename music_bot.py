import os
import shutil
from os import system
import asyncio
import time
import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get
global q_num
global s_num
q_num = 0
s_num = 1

TOKEN = ''
BOT_PREFIX = '/'

bot = commands.Bot(command_prefix=BOT_PREFIX)



@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")
    c = await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Music"))
    global q_num
    q_num = 0
    
@bot.event
async def on_message(message):
    print(q_num)
    await bot.process_commands(message)





@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")


