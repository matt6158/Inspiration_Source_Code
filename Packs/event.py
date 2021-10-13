@formexe.command(pass_context=True)
async def events(ctx):
    embed = discord.Embed(
        title = 'Events',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
event
giveaway
winner
poll
""")
    helpf = (f"""
{formexep}event [#channel] [message]
{formexep}giveaway [prize]
{formexep}winner [message_id]
{formexep}poll [topic]
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Commands ', value=helpl)
    embed.add_field(name='Format ', value=helpf)
    embed.add_field(name='Prefix ', value=formexep, inline=False)
    await ctx.send(embed=embed)

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, *, arg):
    qim2 = await ctx.send("End Date:")
    con = await formexe.wait_for('message', check=lambda message: message.author == ctx.author)
    qim3 = await ctx.send("Ping? [y/n]")
    con2 = await formexe.wait_for('message', check=lambda message: message.author == ctx.author)
    if con2.content == 'y':
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
        await qim3.delete()
        await con2.delete()
    else:
        embed = discord.Embed(
                colour = discord.Colour(formexehex),
                )
        embed.set_author(name="Giveaway!", icon_url=formexe.user.avatar_url)
        embed.set_thumbnail(url=formexe.user.avatar_url)
        embed.add_field(name="End Date:", value=con.content ,inline=False)
        embed.add_field(name="Prize:", value=arg ,inline=False)
        embed.add_field(name="React To The Giveaway To Join", value="-------------------------------------" ,inline=False)
        embed.set_footer(text=ctx.message.guild.name)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🎉')
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()
        await qim3.delete()
        await con2.delete()

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

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def event(ctx, channel : discord.TextChannel, *, arg):
    qim2 = await ctx.send("Ping? [y/n]")
    con = await formexe.wait_for('message', check=lambda message: message.author == ctx.author)
    if con.content == 'y':
        embed = discord.Embed(
            colour = discord.Colour(formexehex),
        )
        embed.set_author(name=ctx.message.author, icon_url=formexe.user.avatar_url)
        embed.set_thumbnail(url=formexe.user.avatar_url)
        embed.add_field(name='Event', value=(arg), inline=False)
        msg = await channel.send('@everyone')
        msg = await channel.send(embed=embed)
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()
    else:
        embed = discord.Embed(
            colour = discord.Colour(formexehex),
        )
        embed.set_author(name=ctx.message.author, icon_url=formexe.user.avatar_url)
        embed.set_thumbnail(url=formexe.user.avatar_url)
        embed.add_field(name='Event', value=(arg), inline=False)
        msg = await channel.send(embed=embed)
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()

@formexe.command(name="poll")
@commands.has_permissions(manage_messages=True)
async def poll(ctx, *, title):
    embed = discord.Embed(
        title="A new poll has been created!",
        description=f"{title}",
        color= discord.Colour(formexehex),
    )
    embed.set_footer(
        text=f"Poll created by: {ctx.message.author} • React to vote!"
    )
    embed_message = await ctx.send(embed=embed)
    await embed_message.add_reaction("👍")
    await embed_message.add_reaction("👎")
    await embed_message.add_reaction("🤷")
