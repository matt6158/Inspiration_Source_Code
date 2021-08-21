@formexe.command(pass_context = True)
async def ticket(ctx):
    tauth = ctx.message.author
    msg = await ctx.send('Creating Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    category = discord.utils.get(tauth.guild.categories, id=())
    ibtc = discord.utils.get(tauth.guild.roles, id=())
    channel = await ctx.message.guild.create_text_channel('Ticket')
    msg = await channel.send(f'{tauth.mention} Someone will be with you shortly '+ibtc.mention)
    ibe = await channel.set_permissions(ctx.message.guild.default_role, read_messages=False, send_messages=False)
    ibc = await channel.set_permissions(tauth, read_messages=True, send_messages=True)
    iba = await channel.set_permissions(ibtc, read_messages=True, send_messages=True)

@formexe.command(pass_context = True)
async def report(ctx):
    tauth = ctx.message.author
    msg = await ctx.send('Creating Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    category = discord.utils.get(tauth.guild.categories, id=())
    ibtc = discord.utils.get(tauth.guild.roles, id=())
    channel = await ctx.message.guild.create_text_channel('Ticket-Report')
    msg = await channel.send(f'{tauth.mention} Someone will be with you shortly '+ibtc.mention)
    ibe = await channel.set_permissions(ctx.message.guild.default_role, read_messages=False, send_messages=False)
    ibc = await channel.set_permissions(tauth, read_messages=True, send_messages=True)
    iba = await channel.set_permissions(ibtc, read_messages=True, send_messages=True)

@formexe.command(pass_context = True)
async def vcticket(ctx):
    tauth = ctx.message.author
    msg = await ctx.send('Creating Ticket...')
    await asyncio.sleep(3)
    await msg.delete()
    category = discord.utils.get(tauth.guild.categories, id=())
    c = await guild.create_voice_channel(name='voice ticket')
    m = formexe.get_channel((c.id))
    msg = await ctx.send(f'{tauth.mention} Someone will be with you shortly')
    ibc = await m.set_permissions(tauth, view_channel=True, connect=True, speak=True)

@formexe.command(pass_context=True , aliases=['ct', 'closet'])
@commands.has_permissions(manage_messages=True)
async def close(ctx):
    channel = ctx.message.channel
    if ('ticket') in channel.name:
        await channel.delete()
    else:
        pass
