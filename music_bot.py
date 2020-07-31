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


@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")


@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx,*, url: str):
    

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'forcetitle': True,
        'forceurl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        infoSearched = ydl.extract_info(f"ytsearch:{url}")

    if "https" in url:
        print("Play Type: YouTube URL")

        for i in infoSearched:
            if i is 'webpage_url':
                searchURL = (infoSearched['entries'][0]['webpage_url'])
                searchTitle = (infoSearched['entries'][0]['title'])


    else:
        print("Play Type: YouTube Search")

        for i in infoSearched:
            if i is 'webpage_url_basename':
                searchURL = (infoSearched['entries'][0]['webpage_url'])
                searchTitle = (infoSearched['entries'][0]['title'])
    
    
   
    

    def check_queue():
        global q_num
        global s_num
        
       
 
        

        if q_num != 0:
            print("Song done, playing next queued\n")
            print(f"Songs still in queue: {q_num}")
            song_there = os.path.isfile("song.mp3")
            if song_there:
                os.remove("song.mp3")
            
            
                for file in os.listdir("./"):
                    if file == (f'song{s_num}.mp3'):
                        
                    
                        os.rename(file, 'song.mp3')
                        
                time.sleep(2)
                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07
                
                s_num = s_num + 1



            else:
                queues.clear()
                print("No songs were queued before the ending of the last song\n")
                q_num = 0
                s_num = 1
            
            
          

  
    
        



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return




    await ctx.send("Getting everything ready now")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([seachURL])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
   
      


    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")
            
            
    time.sleep(2)
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    




    embed = discord.Embed(
        colour = discord.Colour.purple(),
    )

    embed.add_field(name=f'Now Playing', value=f'**__[{searchTitle}]({searchURL})__**', inline=False)
    embed.add_field(name=f'Requested by', value=f'{ctx.author.mention}')

    await ctx.send(embed=embed)
    print(f"Playing: {searchTitle}\n")
    
   
    


@bot.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause")


@bot.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")


@bot.command(pass_context=True)
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()

   

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Music stopped")
        
    else:
        print("No music playing failed to stop")
        await ctx.send("No music playing failed to stop")


queues = {}

@bot.command(pass_context=True, aliases=['q', 'que'])
async def queue(ctx,*, url: str):
    global q_num
    global s_num
    


    q_num = q_num + 1
     
           
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'forcetitle': True,
        'forceurl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        infoSearched = ydl.extract_info(f"ytsearch:{url}")

    if "https" in url:
        print("Play Type: YouTube URL")

        for i in infoSearched:
            if i is 'webpage_url':
                searchURL = (infoSearched['entries'][0]['webpage_url'])
                searchTitle = (infoSearched['entries'][0]['title'])


    else:
        print("Play Type: YouTube Search")

        for i in infoSearched:
            if i is 'webpage_url_basename':
                searchURL = (infoSearched['entries'][0]['webpage_url'])
                searchTitle = (infoSearched['entries'][0]['title'])
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([searURL])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
      

        
        
    embed = discord.Embed(
        colour = discord.Colour.purple(),
    )

    embed.add_field(name=f'Added', value=f'**__[{searchTitle}]({searchURL})__**', inline=False)
    embed.add_field(name=f'To the queue', value=f'{ctx.author.mention}')

    await ctx.send(embed=embed)
    print(f"Playing: {searchTitle}\n")
     


    

    print("Song added to queue\n")
    for filename in os.listdir("./"):
        
     
        if filename.endswith(".mp3"):
            if (searchTitle) in filename:
                
                print(f"Renamed File: {filename}\n")
            
                os.rename(filename, f'song{q_num}.mp3')
            else:
                pass
            
                
        else:
            pass


@bot.command(pass_context=True, aliases=['s', 'ski'])
async def skip(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        await ctx.send("Next Song")
    else:
        print("No music playing")
        await ctx.send("No music playing failed")

@bot.command(pass_context=True, aliases=['c', 'cl'])
async def clear(ctx):
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.remove(file)

    msg = await ctx.send('Removed all songs')
    await asyncio.sleep(3)
    await msg.delete()

    
@bot.command(pass_context=True, aliases=['v', 'vol'])
async def volume(ctx, volume: int):

    if ctx.voice_client is None:
        return await ctx.send("Not connected to voice channel")

    print(volume/100)

    ctx.voice_client.source.volume = volume / 100
    await ctx.send(f"Changed volume to {volume}%")


bot.run(TOKEN)

