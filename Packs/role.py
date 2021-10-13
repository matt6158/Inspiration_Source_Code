@formexe.command(pass_context=True)
async def role(ctx):
    embed = discord.Embed(
        title = 'Role',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
addrole
removerole
createrole
rolecolour
rolecount
deleterole
""")
    helpf = (f"""
{formexep}addrole [@member] [role]
{formexep}removerole [@member] [role]
{formexep}createrole [name]
{formexep}rolecolour [role]
{formexep}rolecount [role]
{formexep}deleterole [role]
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Commands ', value=helpl)
    embed.add_field(name='Format ', value=helpf)
    embed.add_field(name='Prefix ', value=formexep, inline=False)
    embed.set_footer(text=ctx.message.guild.name)
    await ctx.send(embed=embed)

@formexe.command(pass_context=True, aliases=['ar'])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(user.mention+f" You have been given the role {role.name}")

@formexe.command(pass_context=True, aliases=['rr'])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(ctx.message.author.mention+f" {user.name} has has {role.name} removed")

@formexe.command(pass_context=True, aliases=['cr'])
@commands.has_permissions(manage_roles=True)
async def createrole(ctx, *, arg):
    guild = ctx.guild
    author = ctx.message.author
    await guild.create_role(name=arg)
    await ctx.send(ctx.message.author.mention+f' {arg} has been added to roles ')

@formexe.command(pass_context=True, aliases=['rc'])
@commands.has_permissions(manage_roles=True)
async def rolecolour(ctx, *, arg):
    role = discord.utils.get(ctx.guild.roles, name=arg)
    qul = await ctx.send("Please enter a hex colour:")
    rel = await formexe.wait_for('message' ,check=(lambda message: message.author == ctx.message.author))
    if '#' in rel.content:
        colour = rel.content.split('#')
        nc = (colour[1])
        nnc = discord.Colour(int(f"0x{nc}", 16))
        await role.edit(color=discord.Colour(int(f"0x{nc}", 16)))

@formexe.command()
@commands.has_permissions(manage_roles=True)
async def rolecount(ctx, *, arg):
    guild = formexe.get_guild(int(ctx.message.guild.id))
    role = discord.utils.get(guild.roles, name=arg)
    user_count = len(role.members)
    msg = await ctx.send(f'There are {user_count} members with the role {role}')

@formexe.command(pass_context=True, aliases=['dr'])
@commands.has_permissions(manage_roles=True)
async def deleterole(ctx, role_name):
    role = discord.utils.get(ctx.message.guild.roles, name=role_name)
    await role.delete()
    await ctx.send('Role deleted')
