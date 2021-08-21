@formexe.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, *, arg):
    qim2 = await ctx.send("End Date:")
    con = await formexe.wait_for('message', check=lambda message: message.author == ctx.author)
    embed = discord.Embed(
            colour = discord.Colour(formexehex),
            )
    embed.set_author(name="Giveaway!", icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name="End Date:", value=con.content ,inline=False)
    embed.add_field(name="Prize:", value=arg ,inline=False)
    embed.add_field(name="React To The Giveaway To Join", value="-------------------------------------" ,inline=False)
    embed.set_footer(text=ctx.message.guild.name)
    msg = await ctx.send('@everyone')
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🎉')
    await ctx.message.delete()
    await qim2.delete()
    await con.delete()

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def winner(ctx, id_ : int):
    channel = ctx.message.channel
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(formexe.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations to: {winner.mention}. You won!")
    await ctx.message.delete()

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def selfbot(ctx, *, arg):
    await ctx.message.delete()
    webhook = await ctx.message.channel.create_webhook(name='selfbot')
    await webhook.send(content=arg, username=ctx.message.author.name, avatar_url=ctx.message.author.avatar_url)
    await webhook.delete()

@formexe.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    await ctx.send('https://www.youtube.com' + search_results[0])

@formexe.command()
async def spotify(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title = f"{user.name}'s Spotify",
                    description = "Listening to {}".format(activity.title),
                    color = 0x1DB954)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                await ctx.send(embed=embed)
                await ctx.message.delete()

@formexe.command()
async def twitch(ctx, user: discord.Member = None):
    for activity in user.activities:
        if isinstance(activity, discord.Streaming):
            url = activity.url
            await ctx.send(f'{user} is streaming on twitch: {url}')
            await ctx.message.delete()
