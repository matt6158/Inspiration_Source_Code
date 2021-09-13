@formexe.command(pass_context=True)
async def tick(ctx):
    embed = discord.Embed(
        title = 'Tickets',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
ticket
report
vcticket
close
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Prefix ', value=formexep, inline=True)
    embed.add_field(name='Commands ', value=helpl, inline=False)
    await ctx.send(embed=embed)

@formexe.command(pass_context = True)
async def ticket(ctx):
    await ctx.message.delete()
    tauth = ctx.message.author
    msg = await ctx.send('Creating Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    guild = formexe.get_guild(formemg)
    logs = discord.utils.get(guild.channels, name='ticket-logs')
    if logs == None:
        cat = await guild.create_category(name='Tickets')
        c = await cat.create_text_channel(name=f'ticket-logs', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        logs = discord.utils.get(guild.channels, name='ticket-logs')
    category = logs.category
    ulist = []
    for channel in category.channels:
        if (channel.topic) == None:
            await channel.edit(topic=formexe.user.id)
            ulist.append(int(channel.topic))
        else:
            try:
                if int(channel.topic) == (tauth.id):
                    current = formexe.get_channel(channel.id)
                    ulist.append(int(channel.topic))
            except:
                pass
    i = (tauth.id)
    if i not in ulist:
        channel = await ctx.message.guild.create_text_channel(name=f'{tauth.name} ticket', topic=(tauth.id), category=category)
        msg = await channel.send(f'{tauth.mention} Someone will be with you shortly')
        ibc = await channel.set_permissions(tauth, read_messages=True, send_messages=True)
    else:
        await current.send(f'{tauth.mention} You already have a ticket')

@formexe.command(pass_context = True)
async def report(ctx):
    await ctx.message.delete()
    tauth = ctx.message.author
    msg = await ctx.send('Creating Report Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    guild = formexe.get_guild(formemg)
    logs = discord.utils.get(guild.channels, name='ticket-logs')
    if logs == None:
        cat = await guild.create_category(name='Tickets')
        c = await cat.create_text_channel(name=f'ticket-logs', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        logs = discord.utils.get(guild.channels, name='ticket-logs')
    category = logs.category
    ulist = []
    for channel in category.channels:
        if (channel.topic) == None:
            await channel.edit(topic=formexe.user.id)
            ulist.append(int(channel.topic))
        else:
            try:
                if int(channel.topic) == (tauth.id):
                    current = formexe.get_channel(channel.id)
                    ulist.append(int(channel.topic))
            except:
                pass
    i = (tauth.id)
    if i not in ulist:
        channel = await ctx.message.guild.create_text_channel(name=f'{tauth.name} report', topic=(tauth.id), category=category)
        msg = await channel.send(f'{tauth.mention} Someone will be with you shortly')
        msg = await channel.send('If you can send the users name or id and the evidence that would help us out. Thanks')
        ibc = await channel.set_permissions(tauth, read_messages=True, send_messages=True)
    else:
        await current.send(f'{tauth.mention} You already have a ticket')

@formexe.command(pass_context = True)
async def vcticket(ctx):
    await ctx.message.delete()
    tauth = ctx.message.author
    msg = await ctx.send('Creating Vc Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    guild = formexe.get_guild(formemg)
    logs = discord.utils.get(guild.channels, name='ticket-logs')
    if logs == None:
        cat = await guild.create_category(name='Tickets')
        c = await cat.create_text_channel(name=f'ticket-logs', topic=('DO NOT EDIT THE NAME OF THIS CHANNEL'))
        await c.send('DO NOT EDIT THE NAME OF THIS CHANNEL, if you want it changed contact support')
        logs = discord.utils.get(guild.channels, name='ticket-logs')
    category = logs.category
    channel = await guild.create_voice_channel(name=f'{tauth.name} ticket', category=category)
    msg = await ctx.send(f'{tauth.mention} Someone will be with you shortly')
    msg2 = await ctx.send('The channel will delete when you leave')
    await asyncio.sleep(10)
    await msg.delete()
    await msg2.delete()

@formexe.command(pass_context=True , aliases=['ct', 'closet'])
@commands.has_permissions(manage_messages=True)
async def close(ctx, channel : discord.TextChannel = None):
    channel = ctx.message.channel if not channel else channel
    if ('ticket-logs') in channel.name:
        pass
    elif ('ticket') in channel.name:
        await channel.delete()
    elif ('report') in channel.name:
        await channel.delete()
    else:
        pass

@formexe.event
async def on_voice_state_update(member, before, after):
    if before.channel is None:
        pass
    elif before.channel.name == (f'{member.name} ticket') and after.channel is None:
            channel = formexe.get_channel(before.channel.id)
            await channel.delete()
