@formexe.command(pass_context=True)
async def flipbook_manual(ctx, *, page: int = 1):
    await ctx.message.delete()
    pages = len(formexe.manual_pages)
    cur_page = (page - 1)
    embed = formexe.manual_pages[cur_page]
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.set_footer(text=f"📕 Prefix is {formexep} | {formexe.user.name} | Page {page}/{pages}")
    message = await ctx.send(embed=embed)
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await formexe.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "▶️" and page != pages:
                cur_page += 1
                page += 1
                newembed = formexe.manual_pages[cur_page]
                newembed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
                newembed.set_thumbnail(url=formexe.user.avatar_url)
                newembed.set_footer(text=f"📕 Prefix is {formexep} | {formexe.user.name} | Page {page}/{pages}")
                await message.edit(embed=newembed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and page > 1:
                cur_page -= 1
                page -= 1
                newembed = formexe.manual_pages[cur_page]
                newembed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
                newembed.set_thumbnail(url=formexe.user.avatar_url)
                newembed.set_footer(text=f"📕 Prefix is {formexep} | {formexe.user.name} | Page {page}/{pages}")
                await message.edit(embed=newembed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break

formexe_settingsp = discord.Embed(colour = (formexehex),title = ('⚙ Settings'))
formexe_settingsp.add_field(name='📘 Commands', value=("""
latency
username
pfp"""), inline=True)
formexe_settingsp.add_field(name='📗 Format', value=(f"""
`{formexep}latency`
`{formexep}username`
`{formexep}pfp`"""), inline=True)

formexe.manual_pages = [formexe_settingsp]


@formexe.command()
@commands.has_permissions(manage_channels=True)
async def flipbook(ctx, *, page: int = 1):
    list = []

    await ctx.message.delete()
    if len(list) == 0:
        embed = (discord.Embed(description='None'))
        return await ctx.send(embed=embed)
    items_per_page = 10
    pages = math.ceil(len(list) / items_per_page)

    start = (page - 1) * items_per_page
    end = start + items_per_page

    bmembers = ''
    for n, i in enumerate(list[start:end], start=start):
        bmembers += (f'{n+1}, <#{i}>\n')

    embed = (discord.Embed(description='**{} Channels:**\n\n{}'.format(len(list), bmembers))
             .set_footer(text='Viewing page {}/{}'.format(page, pages)))
    message = await ctx.send(embed=embed)
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await formexe.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "▶️" and page != pages:
                page += 1
                start = (page - 1) * items_per_page
                end = start + items_per_page
                bmembers = ''
                for n, i in enumerate(list[start:end], start=start):
                    bmembers += (f'{n+1}, <#{i}>\n')
                newembed = (discord.Embed(description='**{} Channels:**\n\n{}'.format(len(list), bmembers)))
                newembed.set_footer(text='Viewing page {}/{}'.format(page, pages))
                await message.edit(embed=newembed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and page > 1:
                page -= 1
                start = (page - 1) * items_per_page
                end = start + items_per_page
                bmembers = ''
                for n, i in enumerate(list[start:end], start=start):
                    bmembers += (f'{n+1}, <#{i}>\n')
                newembed = (discord.Embed(description='**{} Channels:**\n\n{}'.format(len(list), bmembers)))
                newembed.set_footer(text='Viewing page {}/{}'.format(page, pages))
                await message.edit(embed=newembed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break
