@formexe.command(pass_context=True)
async def social(ctx):
    embed = discord.Embed(
        title = 'Social',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
youtube
spotify
twitch
""")
    helpf = (f"""
{formexep}youtube [search]
{formexep}spotify [@member]
{formexep}twitch [@member]
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Commands ', value=helpl)
    embed.add_field(name='Format ', value=helpf)
    embed.add_field(name='Prefix ', value=formexep, inline=False)
    embed.set_footer(text=ctx.message.guild.name)
    await ctx.send(embed=embed)


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
