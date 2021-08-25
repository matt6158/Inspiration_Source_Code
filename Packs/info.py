def find_server(msg):
        server = None
        if msg:
            try:
                float(msg)
                server = formexe.get_guild(int(msg))
                if not server:
                    return 'Server not found.', False
            except:
                for i in formexe.guilds:
                    if i.name.lower() == msg.lower().strip():
                        server = i
                        break
                if not server:
                    return 'Could not find server. Note: You must be a member of the server you are trying to search.', False

        return server, True

@formexe.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(
        title = 'Info',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
roleinfo
userinfo
serverinfo
channelinfo
botinfo
invites
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Prefix ', value=formexep, inline=True)
    embed.add_field(name='Commands ', value=helpl, inline=False)
    await ctx.send(embed=embed)


@formexe.command()
@commands.has_permissions(manage_messages=True)
async def roleinfo(ctx, guild=None, *, msg):
    if guild:
        guild, found = find_server(guild)
        if not found:
            return await ctx.send(guild)
        guild_roles = guild.roles
    else:
        guild = ctx.message.guild
        guild_roles = ctx.message.guild.roles
    for role in guild_roles:
        if msg.lower() == role.name.lower() or msg == role.id:
            all_users = [str(x) for x in role.members]
            all_users.sort()
            all_users = ', '.join(all_users)
            em = discord.Embed(title='Role Info', color=role.color)
            em.add_field(name='Name', value=role.name)
            em.add_field(name='ID', value=role.id, inline=False)
            em.add_field(name='Users in this role', value=str(len(role.members)))
            em.add_field(name='Role color hex value', value=str(role.color))
            em.add_field(name='Role color RGB value', value=role.color.to_rgb())
            em.add_field(name='Mentionable', value=role.mentionable)
            if len(role.members) > 10:
                em.add_field(name='All users', value=(len(role.members)), inline=False)
            elif len(role.members) >= 1:
                em.add_field(name='All users', value=all_users, inline=False)
            else:
                em.add_field(name='All users', value='There are no users in this role!', inline=False)
            em.add_field(name='Created at', value=role.created_at.__format__('%x at %X'))
            em.set_thumbnail(url='http://www.colorhexa.com/{}.png'.format(str(role.color).strip("#")))
            return await ctx.send(content=None, embed=em)
    await ctx.send('Could not find role ``{}``'.format(msg))

@formexe.command(pass_context=True)
async def userinfo(ctx, member : discord.Member = None):
    member = ctx.message.author if not member else member
    roles=[role for role in member.roles]
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    voice_state = None if not member.voice else member.voice.channel

    roles = []
    for role in member.roles:
        roles.append(role)

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}", icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="User name:", value=member.display_name)
    embed.add_field(name='Nickname', value=member.nick)
    embed.add_field(name='Status', value=member.status)
    embed.add_field(name='In Voice', value=voice_state)
    embed.add_field(name='Game', value=member.activity)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p GMT"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p GMT"))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(member)+1))
    embed.add_field(name="Top role:", value=member.top_role.mention)
    embed.add_field(name="Bot?", value=member.bot)
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)

    await ctx.send(embed=embed)

@formexe.command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
async def server_info(ctx):
	embed = discord.Embed(title="Server information",
				  colour=ctx.guild.owner.colour,
                  timestamp = (ctx.message.created_at),
    )

	embed.set_thumbnail(url=ctx.guild.icon_url)

	statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

	fields = [("ID", ctx.guild.id, True),
			  ("Owner", ctx.guild.owner, True),
			  ("Region", ctx.guild.region, True),
			  ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
			  ("Members", len(ctx.guild.members), True),
			  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
			  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
			  ("Banned members", len(await ctx.guild.bans()), True),
			  ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
			  ("Text channels", len(ctx.guild.text_channels), True),
			  ("Voice channels", len(ctx.guild.voice_channels), True),
			  ("Categories", len(ctx.guild.categories), True),
			  ("Roles", len(ctx.guild.roles), True),
			  ("Invites", len(await ctx.guild.invites()), True),
			  ("\u200b", "\u200b", True)]

	for name, value, inline in fields:
		embed.add_field(name=name, value=value, inline=inline)

	await ctx.send(embed=embed)

@formexe.command()
@commands.has_permissions(manage_messages=True)
async def channelinfo(ctx, chan: Optional[discord.TextChannel]):
    channel = chan
    if channel == None:
        channel = ctx.channel
    embed = discord.Embed(
        title = f'Stats for: {channel.name}',
        description = f'List of details about: {channel.name}',
        timestamp=datetime.datetime.utcnow(),
        colour = discord.Colour(formexehex),
    )
    embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=False)
    embed.add_field(name="Channel Id", value=channel.id, inline=False)
    embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
    embed.add_field(name="Channel Position", value=channel.position, inline=False)
    embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=False)
    embed.add_field(name="Channel is NSFW?", value=channel.is_nsfw(), inline=False)
    embed.add_field(name="Channel is Announcement Channel?", value=channel.is_news(), inline=False)
    embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=False)
    embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=False)
    embed.add_field(name = 'Channel ID', value = channel.id)
    embed.add_field(name="Channel Hash", value=hash(channel), inline=False)
    embed.set_thumbnail(url= ctx.guild.icon_url)
    await ctx.send(embed = embed)

@formexe.command(pass_context=True)
async def botinfo(ctx):
    member = formexe.user
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}", icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="User name:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Running on:", value='Inspiration | Powered By Delør', inline=False)
    await ctx.send(embed=embed)

@formexe.command()
async def invites(ctx, usr : discord.Member):
    if usr == None:
       user = ctx.author
    else:
       user = usr
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    await ctx.send(f"{user.name} has invited {total_invites} member{'' if total_invites == 1 else 's'}!")
