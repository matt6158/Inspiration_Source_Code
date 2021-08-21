@formexe.command(pass_context=True)
async def fun(ctx):
    embed = discord.Embed(
        title = 'Fun',
        colour = discord.Colour(formexehex),
    )
    helpl = ("""
8ball
rate
roll
flip
topic
gif
choose
echo
ascii
l2g
calculate
rpc
""")
    embed.set_author(name=formexe.user.name, icon_url=formexe.user.avatar_url)
    embed.set_thumbnail(url=formexe.user.avatar_url)
    embed.add_field(name='Prefix ', value=formexep, inline=True)
    embed.add_field(name='Commands ', value=helpl, inline=False)
    await ctx.send(embed=embed)

@formexe.command(name='8ball',
            pass_context = True)
async def eight_ball(ctx):
    possible_responses = [
        'Yes ',
        'No ',
        'Too hard to tell ',
        'Without a doubt ',
        'It is quite possible ',
        'Uncertain ',
        'Definitely ',
    ]
    await ctx.send(random.choice(possible_responses)+ctx.message.author.mention)

@formexe.command(pass_context = True)
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@formexe.command(pass_context = True)
async def flip(ctx):
    flip = ['Heads','Tails']
    await ctx.send(ctx.message.author.mention +random.choice(flip))

@formexe.command(pass_context=True)
async def rate(ctx, *, arg):
    await ctx.send(f"I rate {arg} a {random.randint(1,11)} out of 10")

@formexe.command()
async def echo(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@formexe.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@formexe.group(pass_context=True, invoke_without_command=True)
async def ascii(ctx, *, msg):
    if ctx.invoked_subcommand is None:
        if msg:
            msg = str(figlet_format(msg.strip()))
            if len(msg) > 2000:
                await ctx.send('Message too long, RIP.')
            else:
                await ctx.send('```\n{}\n```'.format(msg))
        else:
            await ctx.send(
                           'Please input text to convert to ascii art. Ex: ``>ascii stuff``')

@formexe.command(pass_context=True)
async def l2g(ctx, *, msg: str, aliases=['lmgtfy']):
    lmgtfy = 'http://lmgtfy.com/?q='
    await ctx.send(lmgtfy + urllib.parse.quote_plus(msg.lower().strip()))

@formexe.command(pass_context=True)
async def calc(ctx, *, msg):
    equation = msg.strip().replace('^', '**').replace('x', '*')
    try:
        if '=' in equation:
            left = eval(equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
            right = eval(equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
            answer = str(left == right)
        else:
            answer = str(eval(equation, {"__builtins__": None}, {"sqrt": sqrt}))
    except TypeError:
        return await ctx.send("Invalid calculation query.")

    em = discord.Embed(color=0xD3D3D3, title='Calculator')
    em.add_field(name='Input:', value=msg.replace('**', '^').replace('x', '*'), inline=False)
    em.add_field(name='Output:', value=answer, inline=False)
    await ctx.send(content=None, embed=em)
    await ctx.message.delete()

@formexe.command()
async def gif(ctx, search=None):
    if search == None:
        q='hello'
    else:
        q=seach

    api_key="VbVWF4MAVFl03GXzHF9twGIDvNL1x7Za"
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=f'Woof!')
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@formexe.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await formexe.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")


@formexe.command(pass_context = True)
async def topic(ctx):
    possible_responses = [
     '1. What weird food combinations do you really enjoy? ',
     '2. What social stigma does society need to get over? ',
     '3. What food have you never eaten but would really like to try? ',
     '4. What’s something you really resent paying for? ',
     '5. What would a world populated by clones of you be like? ',
     '6. Do you think that aliens exist? ',
     '7. What are you currently worried about? ',
     '8. Where are some unusual places you’ve been? ',
     '9. Where do you get your news? ',
     '10. What are some red flags to watch out for in daily life? ',
     '11. What movie can you watch over and over without ever getting tired of? ',
     '12. When you are old, what do you think children will ask you to tell stories about? ',
     '13. If you could switch two movie characters, what switch would lead to the most inappropriate movies? ',
     '14. What inanimate object would be the most annoying if it played loud upbeat music while being used? ',
     '15. When did something start out badly for you but in the end, it was great? ',
     '16. How would your country change if everyone, regardless of age, could vote? ',
     '17. What animal would be cutest if scaled down to the size of a cat? ',
     '18. If your job gave you a surprise three day paid break to rest and recuperate, what would you do with those three days? ',
     '19. What’s wrong but sounds right? ',
     '20. What’s the most epic way you’ve seen someone quit or be fired? ',
     '21. If you couldn’t be convicted of any one type of crime, what criminal charge would you like to be immune to? ',
     '22. What’s something that will always be in fashion, no matter how much time passes? ',
     '23. What actors or actresses play the same character in almost every movie or show they do? ',
     '24. In the past people were buried with the items they would need in the afterlife, what would you want buried with you so you could use it in the afterlife? ',
     '25. What’s the best / worst practical joke that you’ve played on someone or that was played on you? ',
     '26. Who do you go out of your way to be nice to? ',
     '27. Where do you get most of the decorations for your home? ',
     '28. What food is delicious but a pain to eat? ',
     '29. Who was your craziest / most interesting teacher ',
     '30. What “old person” things do you do? ',
     '31. What was the last photo you took? ',
     '32. What is the most amazing slow motion video you’ve seen? ',
     '33. Which celebrity do you think is the most down to earth? ',
     '34. What would be the worst thing to hear as you are going under anesthesia before heart surgery? ',
     '35. What’s the spiciest thing you’ve ever eaten? ',
     '36. What’s the most expensive thing you’ve broken? ',
     '37. What obstacles would be included in the World’s most amazing obstacle course? ',
     '38. What makes you roll your eyes every time you hear it? ',
     '39. What do you think you are much better at than you actually are? ',
     '40. Should kidneys be able to be bought and sold? ',
     '41. What’s the most creative use of emojis you’ve ever seen? ',
     '42. When was the last time you got to tell someone “I told you so.”? ',
     '43. What riddles do you know? ',
     '44. What’s your cure for hiccups? ',
     '45. What invention doesn’t get a lot of love, but has greatly improved the world? ',
     '46. What’s the most interesting building you’ve ever seen or been in? ',
     '47. What mythical creature do you wish actually existed? ',
     '48. What are your most important rules when going on a date? ',
     '49. How do you judge a person? ',
     '50. If someone narrated your life, who would you want to be the narrator? ',
     '51. What was the most unsettling film you’ve seen? ',
     '52. What unethical experiment would have the biggest positive impact on society as a whole? ',
     '53. When was the last time you were snooping, and found something you wish you hadn’t? ',
     '54. Which celebrity or band has the worst fan base? ',
     '55. What are you interested in that most people aren’t? ',
     '56. If you were given a PhD degree, but had no more knowledge of the subject of the degree besides what you have now, what degree would you want to be given to you? ',
     '57. What smartphone feature would you actually be excited for a company to implement? ',
     '58. What’s something people don’t worry about but really should? ',
     '59. What movie quotes do you use on a regular basis? ',
     '60. Do you think that children born today will have better or worse lives than their parents? ',
     '61. What’s the funniest joke you know by heart? ',
     '62. When was the last time you felt you had a new lease on life? ',
     '63. What’s the funniest actual name you’ve heard of someone having? ',
     '64. Which charity or charitable cause is most deserving of money? ',
     '65. What TV show character would it be the most fun to change places with for a week? ',
     '66. What was cool when you were young but isn’t cool now? ',
     '67. If you were moving to another country, but could only pack one carry-on sized bag, what would you pack? ',
     '68. What’s the most ironic thing you’ve seen happen? ',
     '69. If magic was real, what spell would you try to learn first? ',
     '70. If you were a ghost and could possess people, what would you make them do? ',
     '71. What goal do you think humanity is not focused enough on achieving? ',
     '72. What problem are you currently grappling with? ',
     '73. What character in a movie could have been great, but the actor they cast didn’t fit the role? ',
     '74. What game have you spent the most hours playing? ',
     '75. What’s the most comfortable bed or chair you’ve ever been in? ',
     '76. What’s the craziest conversation you’ve overheard? ',
     '77. What’s the hardest you’ve ever worked? ',
     '78. What movie, picture, or video always makes you laugh no matter how often you watch it? ',
     '79. What artist or band do you always recommend when someone asks for a music recommendation? ',
     '80. If you could have an all-expenses paid trip to see any famous world monument, which monument would you choose? ',
     '81. If animals could talk, which animal would be the most annoying? ',
     '82. What’s the most addicted to a game you’ve ever been? ',
     '83. What’s the coldest you’ve ever been? ',
     '84. Which protagonist from a book or movie would make the worst roommate? ',
     '85. Do you eat food that’s past its expiration date if it still smells and looks fine? ',
     '86. What’s the most ridiculous thing you have bought? ',
     '87. What’s the funniest comedy skit you’ve seen? ',
     '88. What’s the most depressing meal you’ve eaten? ',
     '89. What tips or tricks have you picked up from your job / jobs? ',
     '90. What outdoor activity haven’t you tried, but would like to? ',
     '91. What songs hit you with a wave of nostalgia every time you hear them? ',
     '92. What’s the worst backhanded compliment you could give someone? ',
     '93. What’s the most interesting documentary you’ve ever watched? ',
     '94. What was the last song you sang along to? ',
     '95. What’s the funniest thing you’ve done or had happen while your mind was wandering? ',
     '96. What app can you not believe someone hasn’t made yet? ',
     '97. When was the last time you face palmed? ',
     '98. If you were given five million dollars to open a small museum, what kind of museum would you create? ',
     '99. Which of your vices or bad habits would be the hardest to give up? ',
     '100. What really needs to be modernized? ',
     '101. When was the last time you slept more than nine hours? ',
     '102. How comfortable are you speaking in front of large groups of people? ',
     '103. What’s your worst example of procrastination? ',
     '104. Who has zero filter between their brain and mouth? ',
     '105. What was your most recent lie? ',
     '106. When was the last time you immediately regretted something you said? ',
     '107. What would be the best thing you could reasonably expect to find in a cave? ',
     '108. What did you think was going to be amazing but turned out to be horrible? ',
     '109. What bit of trivia do you know that is very interesting but also very useless? ',
     '110. What’s the silliest thing you’ve seen someone get upset about? ',
     '111. What animal or plant do you think should be renamed? ',
     '112. What was the best thing that happened to you today? ',
     '113. As a child, what did you think would be awesome about being an adult, but isn’t as awesome as you thought it would be? ',
     '114. When’s censorship warranted? ',
     '115. What’s the most boring super hero you can come up with? ',
     '116. What would be some of the downsides of certain superpowers? ',
     '117. What word is a lot of fun to say? ',
     '118. What current trend do you hope will go on for a long time? ',
     '119. What actors or actresses can’t play a different character because they played their most famous character too well? ',
     '120. Where’s your go to restaurant for amazing food? ',
     '121. What’s something that all your friends agree on? ',
     '122. What’s your best story from a wedding? ',
     '123. What languages do you wish you could speak? ',
     '124. What’s the most pleasant sounding accent? ',
     '125. What’s something that everyone, absolutely everyone, in the entire world can agree on? ',
     '126. What country is the strangest? ',
     '127. What’s the funniest word in the English language? ',
     '128. What’s some insider knowledge that only people in your line of work have? ',
     '129. Who do you wish you could get back into contact with? ',
     '130. How do you make yourself sleep when you can’t seem to get to sleep? ',
     '131. If people receive a purple heart for bravery, what would other color hearts represent? ',
     '132. What are some of the best vacations you’ve had? ',
     '133. If there was a book of commandments for the modern world, what would some of the rules be? ',
     '134. What’s the craziest video you’ve ever seen? ',
     '135. What’s your “Back in my day, we…”? ',
     '136. If you could know the truth behind every conspiracy, but you would instantly die if you hinted that you knew the truth, would you want to know? ',
     '137. What animal would be the most terrifying if it could speak? ',
     '138. What’s the worst hairstyle you’ve ever had? ',
     '139. What habit do you have now that you wish you started much earlier? ',
     '140. If you were given one thousand acres of land that you didn’t need to pay taxes on but couldn’t sell, what would you do with it? ',
     '141. What about the opposite sex confuses you the most? ',
     '142. When was the last time you yelled at someone? ',
     '143. What’s the opposite of a koala? ',
     '144. What kinds of things do you like to cook or are good at cooking? ',
     '145. What life skills are rarely taught but extremely useful? ',
     '146. What movie universe would be the worst to live out your life in? ',
     '147. If you could hack into any one computer, which computer would you choose? ',
     '148. Who do you feel like you know even though you’ve never met them? ',
     '149. What’s the most ridiculous animal on the planet? ',
     '150. What’s the worst thing you’ve eaten out of politeness? ',
     '151. What’s the most historic thing that has happened in your lifetime? ',
     '152. What happens in your country regularly that people in most countries would find strange or bizarre? ',
     '153. What has been blown way out of proportion? ',
     '154. When was a time you acted nonchalant but were going crazy inside? ',
     '155. What’s about to get much better? ',
     '156. What are some clever examples of misdirection you’ve seen? ',
     '157. What’s your funniest story involving a car? ',
     '158. What would be the click-bait titles of some popular movies? ',
     '159. If you built a themed hotel, what would the theme be and what would the rooms look like? ',
     '160. What scientific discovery would change the course of humanity overnight if it was discovered? ',
     '161. Do you think that humans will ever be able to live together in harmony? ',
     '162. What would your perfect bar look like? ',
     '163. What’s the scariest non-horror movie? ',
     '164. What’s the most amazing true story you’ve heard? ',
     '165. What’s the grossest food that you just can’t get enough of? ',
     '166. What brand are you most loyal to? ',
     '167. What’s the most awkward thing that happens to you on a regular basis? ',
     '168. If you had to disappear and start a whole new life, what would you want your new life to look like? ',
     '169. What movie or book do you know the most quotes from? ',
     '170. What was one of the most interesting concerts you’ve been to? ',
     '171. Where are you not welcome anymore? ',
     '172. What do you think could be done to improve the media? ',
     '173. What’s the most recent show you’ve binge watched? ',
     '174. What’s the worst movie trope? ',
     '175. What’s a common experience for many people that you’ve never experienced? ',
     '176. What are some misconceptions about your hobby? ',
     '177. What’s the smartest thing you’ve seen an animal do? ',
     '178. What’s the most annoying noise? ',
     '179. What’s your haunted house story? ',
     '180. What did you Google last? ',
     '181. What’s the dumbest thing someone has argued with you about? ',
     '182. If money and practicality weren’t a problem, what would be the most interesting way to get around town? ',
     '183. What’s the longest rabbit hole you’ve been down? ',
     '184. What’s the saddest scene in a movie or TV series? ',
     '185. What’s the most frustrating product you own? ',
     '186. What inconsequential super power would you like to have? ',
     '187. What qualities do all your friends have in common? ',
     '188. What odd smell do you really enjoy? ',
     '189. What’s the coolest animal you’ve seen in the wild? ',
     '190. What’s the best lesson you’ve learned from a work of fiction? ',
     '191. What food do you crave most often? ',
     '192. Who in your life has the best / worst luck? ',
     '193. What fashion trend makes you cringe or laugh every time you see it? ',
     '194. What’s your best story of you or someone else trying to be sneaky and failing miserably? ',
     '195. Which apocalyptic dystopia do you think is most likely? ',
     '196. If you had a HUD that showed three stats about any person you looked at, what three stats would you want it to show? ',
     '197. What’s the funniest thing you’ve seen a kid do? ',
     '198. What’s your secret talent? ',
     '199. What’s the best way you or someone you know has gotten out of a ticket / trouble with the law? ',
     '200. Tear gas makes people cry and laughing gas makes people giggle, what other kinds of gases do you wish existed? ',
     'Bermuda Warwick Long Bay Beach ',
     '201. What’s the most beautiful beach you’ve been to? ',
     '202. What’s the most anxiety inducing thing you do on a regular basis? ',
     '203. What’s something that everyone agrees we should change, but somehow it never changes? ',
     '204. What trend are you tired of? ',
     '205. What’s incredibly cheap and you would pay way more for? ',
     '206. What’s your grossest bug story? ',
     '207. What would the adult version of an ice-cream truck sell and what song would it play? ',
     '208. What company do you despise? ',
     '209. When was the most inappropriate time you busted out in laughter? ',
     '210. What would be an accurate tag line for each month? ',
     '211. What’s the most overrated product out on the market? ',
     '212. What word do you always misspell? ',
     '213. What naps are the most satisfying? ',
     '214. What’s the weirdest thing you’ve found lying on the ground / side of the road? ',
     '215. What’s the funniest TV show you’ve ever seen? ',
     '216. What’s the most embarrassing story from your childhood? ',
     '217. What animal is the most majestic? ',
     '218. What’s something that everyone knows is true, but we don’t like to admit it? ',
     '219. What’s the weirdest text or email you’ve gotten? ',
     '220. What always cheers you up when you think about it? ',
     '221. What sport could you play the longest in a televised game, without anyone discovering you aren’t a professional athlete? ',
     '222. If you could talk to animals and they would understand you, but you couldn’t understand them, what would you do with that power? ',
     '223. What’s the most boring sport, and what would you do to make it more exciting? ',
     '224. What’s the creepiest tech out there? ',
     '225. Who did you use to look up to, but they screwed up and you lost faith in them? ',
     '226. What’s fine in small numbers but terrifying in large numbers? ',
     '227. Do you like things to be carefully planned or do you prefer to just go with the flow? ',
     '228. What animal would you most like to eat? ',
     '229. What fictional characters have you had a crush on over the years? ',
     '230. What would the box with all your hopes and dreams inside look like? ',
     '231. What was the worst shopping experience you’ve ever had? ',
     '232. What story you’ve heard has stayed with you and always disturbs you every time you think about it? ',
     '233. What was the most important appointment or deadline you missed? ',
     '234. If you were a clown themed super hero, what powers would you have? ',
     '235. If you could airdrop anything you want, worth two million dollars or less, anywhere you want, what would you airdrop and where would you airdrop it? ',
     '236. If you lived in a virtual reality world of your own creation, what would it look like? ',
     '237. What escalated very quickly? ',
     '238. What two things are terrible when separate but great when you put them together? ',
     '239. What did you believe for way too long as a child? ',
     '240. What big event do you think will happen soon that most people aren’t expecting? ',
     '241. What still makes you cringe when you think back on it? ',
     '242. What current trend makes no sense to you? ',
     '243. If you owned a restaurant, what kind of food would it serve? ',
     '244. Which celebrity is the most likely to have a collection of canes that are just for show? ',
     '245. What’s the weirdest crush you’ve had? ',
     '246. What do a lot of people have very strong opinions about, even though they know very little about it? ',
     '247. What’s your go to casino game? ',
     '248. An epic feast is held in your honor, what’s on the table? ',
     '249. What’s your favorite holiday movie? ',
     '250. Who is the most manipulative person you’ve ever met? ',
     '251. Who is the most creative person you know? ',
     '252. What’s the funniest pick up line you’ve heard? ',
     '253. What seemingly innocent question makes you think “It’s a trap!”? ',
     '254. How ambitious are you? ',
     '255. What did you like / dislike about where you grew up? ',
     '256. What elements of pop culture will be forever tied in your mind to your childhood? ',
     '257. What’s your good luck charm? ',
     '258. What’s legal now, but probably won’t be in 25 years? ',
     '259. Would you want the ability to hear the thoughts of people near you if you couldn’t turn the ability off? ',
     '260. When was the last time you stayed up through the entire night? ',
     '261. What’s something that people think makes them look cool, but actually has the opposite effect? ',
     '262. What’s the oldest thing you own? ',
     '263. What has someone borrowed but never given back? ',
     '264. Where is the best place you’ve been for taking walks? ',
     '265. If cartoon physics suddenly replaced real physics, what are some things you would want to try? ',
     '266. What from the present will withstand the test of time? ',
     '267. Who in your life is the worst at using technology? ',
     '268. What’s the weirdest conversation you’ve eavesdropped on? ',
     '269. What just around the corner tech are you eager to get your hands on? ',
     '270. What was the darkest movie you’ve ever seen? ',
     '271. What do you do when you hear something fall in the middle of the night while you are in bed? ',
     '272. What outfit could you put together from clothes you own to get the most laughs? ',
     '273. What’s the most disgusting sounding word in the English language? ',
     '274. What was ruined because it became popular? ',
     '275. What outdated slang do you use on a regular basis? ',
     '276. What was the biggest realization you had about yourself? ',
     '277. What’s your best example of easy come, easy go? ',
     '278. What small change greatly improves a person’s appearance? ',
     '279. What topic could you spend hours talking about? ',
     '280. What happens regularly that would horrify a person from 100 years ago? ',
     '281. What do a lot of people hope will happen but is just not going to happen? ',
     '282. What’s the weirdest thing that has happened to you while working at your job? ',
     '283. What questions would you like to ask a time traveler from 200 years in the future? ',
     '284. Which way should toilet paper hang, over or under? ',
     '285. What’s the most physically painful thing you’ve ever experienced? ',
     '286. What horror story do you have from a job you’ve had? ',
     '287. What’s the most rage inducing game you’ve ever played? ',
     '288. What’s the biggest overreaction you’ve ever seen? ',
     '289. What are some of the most common misconceptions? ',
     '290. What job doesn’t exist now but will exist in the future? ',
     '291. What awful movie do you love? ',
     '292. What normally delicious food gets ruined when you wrap it in a tortilla? ',
     '293. What’s your best example of fake it till you make it? ',
     '294. What were you completely certain of until you found out you were wrong? ',
     '295. What’s something commonly done that gets progressively weirder the more you think about it? ',
     '296. What’s the cutest thing you can imagine? Something so cute it’s almost painful. ',
     '297. If you were given unlimited resources, how would you lure the worst of humanity into one stadium at the same time? ',
     '298. What do you think about when you hear the word “classy”? ',
     '299. What near future predictions do you have? ',
     '300. What do you need help with most often? ',
     '301. What piece of “art” would you create if you had to pretend to be an artist and submit something to a gallery? ',
     '302. What do you do to make the world a better place? ',
     '303. What’s the best and worst thing about the country you are from? ',
     '304. If you were in charge renaming things so that their names would be more accurate, what names would you come up with? ',
     '305. What’s better broken than whole? ',
     '306. What values are most important to you? ',
     '307. What’s the best sandwich you’ve ever had? ',
     '308. What’s the worst thing you ate from a fast food restaurant? ',
     '309. What’s something that I don’t know? ',
     '310. What profession doesn’t get enough credit or respect? ',
     '311. What memory of yours feels real but is most likely false? ',
     '312. What’s your “and then it got worse” story? ',
     '313. What was the most amazing physical feat you’ve managed to pull off? ',
     '314. What’s the most annoying thing about the social media platform you use most often? ',
     '315. If you were hired to show tourists what life is really like where you live, what would you show them / have them do? ',
     '316. What would be the most unsettling thing to keep occasionally finding around your house? ',
     '317. What nicknames do you have for people in your life? ',
     '318. What does the opposite sex do that you wish that you could do, but it’s not anatomically feasible or it’s socially frowned upon? ',
     '319. How much do you plan / prepare for the future? ',
     '320. What do you hate most and love most about your car? ',
     '321. What weird potato chip flavor that doesn’t exist would you like to try? ',
     '322. What’s the silliest thing you’ve convinced someone of? ',
     '323. How much do you think names affect the outcomes of people’s lives? ',
     '324. What product or service is way more expensive than it needs to be? ',
     '325. What’s the shadiest thing you’ve seen someone do? ',
     '326. What was the last situation where some weird stuff went down and everyone acted like it was normal, and you weren’t sure if you were crazy or everyone around you was crazy? ',
     '327. What did you eat so much of that now you hate it? ',
     '328. What are some of the dumbest lyrics you’ve heard in a song? ',
     '329. Where’s the line between soup and cereal? ',
     '330. What word do you always mispronounce? ',
     '331. What do you think you do better than 90% of people? ',
     '332. What would be the worst food to be liquefied and drunk through a straw? ',
     '333. What’s the weirdest thing about modern life that people just accept as normal? ',
     '334. How much of your body would you cybernetically enhance if you could? ',
     '335. If you wanted to slowly drive a roommate insane using only notes, what kind of notes would you leave around the house? ',
     '336. If you had a giraffe that you needed to hide, where would you hide it? ',
     '337. What’s the clumsiest thing you’ve done? ',
     '338. What songs do you only know the chorus to? ',
     '339. Think of a brand, now what would an honest slogan for that brand be? ',
     '340. What’s something common from your childhood that will seem strange to future generations? ',
     'Green forest canopy ',
     '341. What’s the most amazing place in nature you’ve been? ',
     '342. What’s quickly becoming obsolete? ',
     '343. Where is the most uncomfortable place you have ever slept? ',
     '344. What’s the most annoying animal you’ve encountered? ',
     '345. What’s your best example of correlation not equaling causation? ',
     '346. In what situations, do you wish you could throw down a smoke bomb and disappear? ',
     '347. When was the last time you were hopelessly lost? ',
     '348. What songs do you feel compelled to sing along with when you hear them, even if you don’t totally know all the words? ',
     '349. What product do you wish a company would make a “smart” version of? ',
     '350. What two films would you like to combine into one? ',
     '351. What’s are some of your Pavlovian responses? ',
    ]
    await ctx.send(random.choice(possible_responses)+ctx.message.author.mention)
