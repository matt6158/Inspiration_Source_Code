@formexe.command(pass_context=True)
async def utility(ctx):
    embed = discord.Embed(
        title = 'Utility',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
createchannel
deletechannel
slomode
announce
quote
say
nickname
avatar
jumbo
react
selfbot
colour
""")
    helpf = (f"""
{formexep}createchannel [channel_type] [name]
{formexep}deletechannel [channel_name]
{formexep}slomode [#channel] [seconds]
{formexep}announce [#channel] [message]
{formexep}quote [title]
{formexep}say [message]
{formexep}nickname [@member] [name]
{formexep}avatar [@member]
{formexep}jumbo [emoji]
{formexep}react [message_id] [emoji]
{formexep}selfbot [message]
{formexep}colour [hex]
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

@formexe.command(pass_context=True , aliases=['cc'])
@commands.has_permissions(manage_channels=True)
async def createchannel(ctx, type : str, *, arg):
    if type == 'text':
        await ctx.message.guild.create_text_channel(name=arg, category=ctx.message.channel.category)
    elif type == 'voice':
        await ctx.message.guild.create_voice_channel(name=arg, category=ctx.message.channel.category)
    elif type == 'category':
        await ctx.message.guild.create_category(name=arg)


@formexe.command(pass_context=True , aliases=['deletec'])
@commands.has_permissions(manage_channels=True)
async def deletechannel(ctx, channel_name):
    await ctx.message.delete()
    existing_channel = discord.utils.get(ctx.message.guild.channels, name=channel_name)
    if existing_channel is not None:
       await existing_channel.delete()
       await ctx.send(f'Channel deleted')

    else:
       await ctx.send(f'No channel named, "{channel_name}", was found')

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, channel : discord.TextChannel, num : int):
    await channel.edit(slowmode_delay = num)
    await asyncio.sleep(2)
    await ctx.message.delete()

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def announce(ctx, channel : discord.TextChannel, *, arg):
    qim2 = await ctx.send("Ping? [y/n]")
    con = await formexe.wait_for('message', check=lambda message: message.author == ctx.author)
    if con.content == 'y':
        embed = discord.Embed(
            colour = discord.Colour(formexehex),
        )
        embed.set_author(name=ctx.message.author, icon_url=formexe.user.avatar_url)
        embed.set_thumbnail(url=formexe.user.avatar_url)
        embed.add_field(name='Announcement', value=(arg), inline=False)
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
        embed.add_field(name='Announcement', value=(arg), inline=False)
        msg = await channel.send(embed=embed)
        await ctx.message.delete()
        await qim2.delete()
        await con.delete()

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, arg):
    await ctx.send(arg)

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def quote(ctx, *, arg):
    qim2 = await ctx.send("What do you want to say:")
    con = await formexe.wait_for('message', check=lambda message: message.author == ctx.author)
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour(formexehex),


        )
    embed.set_author(name=ctx.message.author, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name=arg, value=(con.content), inline=False)
    msg = await channel.send(embed=embed)
    await ctx.message.delete()
    await con.delete()
    await qim2.delete()

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def nickname(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

@formexe.command()
async def avatar(ctx, member : discord.Member = None):
    member = ctx.message.author if not member else member
    embed = discord.Embed(colour=member.color, title='Avatar')
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@formexe.command()
async def jumbo(ctx, emoji: Union[discord.Emoji, discord.PartialEmoji]):
    await ctx.message.delete()
    webhook = await ctx.message.channel.create_webhook(name='Jumbo')
    await webhook.send(content=emoji.url, username=ctx.message.author.name, avatar_url=ctx.message.author.avatar_url)
    await webhook.delete()

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def react(ctx, message : discord.Message, *, arg):
    await message.add_reaction(arg)
    await ctx.message.delete()

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def selfbot(ctx, *, arg):
    await ctx.message.delete()
    webhook = await ctx.message.channel.create_webhook(name='selfbot')
    await webhook.send(content=arg, username=ctx.message.author.name, avatar_url=ctx.message.author.avatar_url)
    await webhook.delete()

@formexe.command()
async def colour(ctx, value : str):
    embed = discord.Embed(colour=formexehex, title='Colour')
    embed.set_image(url='http://www.colorhexa.com/{}.png'.format(str(value).strip("#")))
    await ctx.send(embed=embed)
