@formexe.command(pass_context=True)
async def apps(ctx):
    embed = discord.Embed(
        title = 'Application',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
apply
accept
reject
""")
    helpf = (f"""
{formexep}apply
{formexep}accept [@member]
{formexep}reject [@member]
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Commands ', value=helpl)
    embed.add_field(name='Format ', value=helpf)
    embed.add_field(name='Prefix ', value=formexep, inline=False)
    embed.set_footer(text=ctx.message.guild.name)
    await ctx.send(embed=embed)
@formexe.command(pass_context=True)
async def apps(ctx):
    embed = discord.Embed(
        title = 'Application',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
apply
suggest
accept
reject
""")
    helpf = (f"""
{formexep}apply
{formexep}suggest [message]
{formexep}accept [@member]
{formexep}reject [@member]
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Commands ', value=helpl)
    embed.add_field(name='Format ', value=helpf)
    embed.add_field(name='Prefix ', value=formexep, inline=False)
    embed.set_footer(text=ctx.message.guild.name)
    msg = await ctx.send(embed=embed)
    await asyncio.sleep(60)
    await msg.delete()
    await ctx.message.delete()

@formexe.command(pass_context=True)
@commands.cooldown(1,21600, commands.BucketType.user)
async def suggest(ctx, *, arg):
    channel = discord.utils.get(ctx.message.guild.channels, name='suggestions')
    if channel == None:
        c = await ctx.message.guild.create_text_channel(name=f'suggestions', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        channel = discord.utils.get(ctx.message.guild.channels, name='suggestions')
    embed = discord.Embed(
        colour = discord.Colour(formexehex)
    )
    embed.set_author(name=ctx.message.author)
    embed.add_field(name='Suggestion', value=arg, inline=False)
    m = await channel.send(ctx.message.author.mention)
    m = await channel.send(embed=embed)
    m = await ctx.send(f"Suggestion sent")
    await ctx.message.delete()

@formexe.command()
@commands.cooldown(1,21600, commands.BucketType.user)
async def apply(ctx):
    DM = formexe.get_user(ctx.message.author.id)
    msg = await DM.send("You will be asked a few questions in order to apply")
    msg = await DM.send("If you want to cancel at any question type cancel as your answer")
    await asyncio.sleep(2)
    await ctx.send('Apply questions sent')
    await ctx.message.delete()

    qu1 = await DM.send("What are you applying for:")
    re1 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re1.content =='cancel':
        raise ValueError("Cancelled apply")

    qu2 = await DM.send("Discord username and tag:")
    re2 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re2.content =='cancel':
        raise ValueError("Cancelled apply")

    qu3 = await DM.send("State your age:")
    re3 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re3.content =='cancel':
        raise ValueError("Cancelled apply")

    qu4 = await DM.send("Please state your experience. **Be as descriptive as you can**:")
    re4 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re4.content =='cancel':
        raise ValueError("Cancelled apply")

    qu5 = await DM.send("Why do you think you are an ideal candidate for the job you're applying for? **Be as descriptive as you can**:")
    re5 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re5.content =='cancel':
        raise ValueError("Cancelled apply")

    qu6 = await DM.send("Is there anything else you wish to add:")
    re6 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re6.content =='cancel':
        raise ValueError("Cancelled apply")

    embed = discord.Embed(
        colour = discord.Colour(formexehex),
        title = 'Application',
        description = 'Your application has been sent!',
    )
    msg = await DM.send(embed=embed)
    msg1 = re1.content
    msg2 = re2.content
    msg3 = re3.content
    msg4 = re4.content
    msg5 = re5.content
    msg6 = re6.content
    if len(msg1) > 1024:
        msg1 = 'Message was too long'
    if len(msg2) > 1024:
        msg2 = 'Message was too long'
    if len(msg3) > 1024:
        msg3 = 'Message was too long'
    if len(msg4) > 1024:
        msg4 = 'Message was too long'
    if len(msg5) > 1024:
        msg5 = 'Message was too long'
    if len(msg6) > 1024:
        msg6 = 'Message was too long'

    channel = discord.utils.get(ctx.message.guild.channels, name='applications')
    if channel == None:
        c = await ctx.message.guild.create_text_channel(name=f'applications', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        channel = discord.utils.get(ctx.message.guild.channels, name='applications')
    embed = discord.Embed(
        colour = discord.Colour(formexehex)
    )

    embed.set_author(name=ctx.message.author)
    embed.add_field(name='Applying for:', value=f"{msg1}", inline=False)
    embed.add_field(name='Tag:', value=f"{msg2}", inline=False)
    embed.add_field(name='Age:', value=f"{msg3}", inline=False)
    embed.add_field(name='Previous experiences:', value=f"{msg4}", inline=False)
    embed.add_field(name='Ideal candidate:', value=f"{msg5}", inline=False)
    embed.add_field(name='Extra:', value=f"{msg6}", inline=False)
    await channel.send(ctx.message.author.mention)
    await channel.send(embed=embed)


@formexe.command()
@commands.has_permissions(manage_messages=True)
async def accept(ctx, member : discord.Member):
    embed = discord.Embed(colour=formexehex, description=f'Congratulations! Your application has been accepted!')
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.set_footer(text=ctx.message.guild.name)
    await member.send(embed=embed)

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def reject(ctx, member : discord.Member):
    embed = discord.Embed(colour=formexehex, description=f'Thank you for your application. Unfortunately we have declined your application as we are not currently looking for any support.')
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.set_footer(text=ctx.message.guild.name)
    await member.send(embed=embed)

@formexe.command()
@commands.cooldown(1,21600, commands.BucketType.user)
async def apply(ctx):
    DM = formexe.get_user(ctx.message.author.id)
    msg = await DM.send("You will be asked a few questions in order to apply")
    msg = await DM.send("If you want to cancel at any question type cancel as your answer")
    await asyncio.sleep(2)
    await ctx.send('Apply questions sent')
    await ctx.message.delete()

    qu1 = await DM.send("What are you applying for:")
    re1 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re1.content =='cancel':
        raise ValueError("Cancelled apply")

    qu2 = await DM.send("Discord username and tag:")
    re2 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re2.content =='cancel':
        raise ValueError("Cancelled apply")

    qu3 = await DM.send("State your age:")
    re3 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re3.content =='cancel':
        raise ValueError("Cancelled apply")

    qu4 = await DM.send("Please state your experience. **Be as descriptive as you can**:")
    re4 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re4.content =='cancel':
        raise ValueError("Cancelled apply")

    qu5 = await DM.send("Why do you think you are an ideal candidate for the job you're applying for? **Be as descriptive as you can**:")
    re5 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re5.content =='cancel':
        raise ValueError("Cancelled apply")

    qu6 = await DM.send("Is there anything else you wish to add:")
    re6 = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.author and message.channel.type == discord.ChannelType.private))
    if re6.content =='cancel':
        raise ValueError("Cancelled apply")

    embed = discord.Embed(
        colour = discord.Colour(formexehex),
        title = 'Application',
        description = 'Your application has been sent!',
    )
    msg = await DM.send(embed=embed)
    msg1 = re1.content
    msg2 = re2.content
    msg3 = re3.content
    msg4 = re4.content
    msg5 = re5.content
    msg6 = re6.content
    if len(msg1) > 1024:
        msg1 = 'Message was too long'
    if len(msg2) > 1024:
        msg2 = 'Message was too long'
    if len(msg3) > 1024:
        msg3 = 'Message was too long'
    if len(msg4) > 1024:
        msg4 = 'Message was too long'
    if len(msg5) > 1024:
        msg5 = 'Message was too long'
    if len(msg6) > 1024:
        msg6 = 'Message was too long'

    channel = formexe.get_channel((formexel))
    embed = discord.Embed(
        colour = discord.Colour(formexehex)
    )

    embed.set_author(name=ctx.message.author)
    embed.add_field(name='Applying for:', value=f"{msg1}", inline=False)
    embed.add_field(name='Tag:', value=f"{msg2}", inline=False)
    embed.add_field(name='Age:', value=f"{msg3}", inline=False)
    embed.add_field(name='Previous experiences:', value=f"{msg4}", inline=False)
    embed.add_field(name='Ideal candidate:', value=f"{msg5}", inline=False)
    embed.add_field(name='Extra:', value=f"{msg6}", inline=False)
    await channel.send(ctx.message.author.mention)
    await channel.send(embed=embed)


@formexe.command()
@commands.has_permissions(manage_messages=True)
async def accept(ctx, member : discord.Member):
    embed = discord.Embed(colour=formexehex, description=f'Congratulations! Your application has been accepted!')
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.set_footer(text=ctx.message.guild.name)
    await member.send(embed=embed)

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def reject(ctx, member : discord.Member):
    embed = discord.Embed(colour=formexehex, description=f'Thank you for your application. Unfortunately we have declined your application as we are not currently looking for any support.')
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.set_footer(text=ctx.message.guild.name)
    await member.send(embed=embed)
