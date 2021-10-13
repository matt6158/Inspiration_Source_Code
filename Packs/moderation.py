@formexe.command(pass_context=True)
async def mod(ctx):
    embed = discord.Embed(
        title = 'Moderation ',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
warn
mute
kick
ban
hackban
purge
lock
unlock
dm
unmute
unban
""")
    helpf = (f"""
{formexep}warn [@member] [reason]
{formexep}mute [@member]
{formexep}kick [@member] [reason]
{formexep}ban [@member] [reason]
{formexep}hackban [member_id]
{formexep}purge [@member] [number]
{formexep}lock - optional [@role]
{formexep}unlock - optional [@role]
{formexep}dm [@members] [message]
{formexep}unmute [@member]
{formexep}unban [member_name]
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Commands ', value=helpl)
    embed.add_field(name='Format ', value=helpf)
    embed.add_field(name='Prefix ', value=formexep, inline=False)
    embed.set_footer(text=ctx.message.guild.name)
    await ctx.send(embed=embed)

@formexe.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f'You have been warned! {member.mention}')
    await member.send(f'You have be warned for {reason}')
    await ctx.message.delete()

@formexe.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
    await ctx.message.delete()


@formexe.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def hackban(ctx, *, member):
    try:
        await ctx.guild.ban(discord.Object(id=member))
        await ctx.send(f'Banned {member}')
        await ctx.message.delete()
    except:
        await ctx.send("Couldn't find member")

@formexe.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    await ctx.message.delete()

@formexe.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, member: discord.Member=None, limit=50):
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        return await ctx.send("Please pass in an integer as limit")
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"Purged {limit} messages", delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
    guild = ctx.guild
    if discord.utils.get(guild.roles, name="Muted"):
        pass
    else:
        await guild.create_role(name="Muted", colour=discord.Colour(0x939995))
        print('role made mute')

    role = discord.utils.get(ctx.message.author.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f'{member.mention} has been muted')

@formexe.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} was unmuted')

@formexe.command(pass_context=True, aliases=['ld'])
@commands.has_permissions(manage_messages=True)
async def lock(ctx, role : discord.Role = None):
    role = ctx.guild.default_role if not role else role
    await ctx.channel.set_permissions(role, send_messages=False)
    lm = await ctx.send(f'This channel has been locked')
    await asyncio.sleep(10)
    await lm.delete()

@formexe.command(pass_context=True, aliases=['ul'])
@commands.has_permissions(manage_messages=True)
async def unlock(ctx, role : discord.Role = None):
    role = ctx.guild.default_role if not role else role
    await ctx.channel.set_permissions(role, send_messages=True)
    lm = await ctx.send(f'This channel is now unlocked')
    await asyncio.sleep(10)

@formexe.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def dm(ctx, users: Greedy[User], *, arg):
    for user in users:
        await user.send(arg)
    await ctx.message.delete()
    await ctx.send('DMs sent')
