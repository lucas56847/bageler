import os, time, asyncio, pytz
import discord,random, requests
from array import *
from datetime import datetime,date
from bs4 import BeautifulSoup
from invasion import *
from dotenv import load_dotenv
from discord.ext import commands
from error import *
load_dotenv()

#TODO implement linux compatibility with .env file loading procedure
#TODO implement messaging capability
#todo optimize webgrab
#TODO error handling --- sorta done, USE TRY
#TODO fix blocking stuff
#TODO get rid of nohup: nohup command >/dev/null 2>&1 
#call on server with nohup python3 main.py


token = os.getenv("token")
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
intents.reactions = True
intents.guilds = True
client = discord.Client(intents=intents)

#initializes discord bot settings to allow for correct command handling
#commands can be activated with '!'

bot = commands.Bot(command_prefix='!', intents = intents)

Monitoring = 0
running = 0
tz_LA = pytz.timezone('America/Los_Angeles') 

# Get the correct timezone for use later when bot is running
#PST for Toon time

starttime = time.time()
startdate = date.today()

#confirms that the bot is online or has reconnected.
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(guild.id)
        channel = discord.utils.get(guild.channels, name='bageler')
        if (channel):
            await channel.send("The Bageler emerges!")
    print("Eat glass!")
    
#command to stop monitoring, prints to console and channel    
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command(name = 'stop')
async def stop(response):
    global Monitoring
    global running
    channel = response.channel
    if Monitoring == 0:
        response = "Already stopped. Doofus."
    else:
        running = 0
        response = "Stopping!"
    
    Monitoring = 0
    print(response)
    await channel.send(response)


#monitor function that monitors the invasion every ~8 minutes 
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command(name = 'monitor')
async def monitor(bagelresponse):
    delayFlag = 0
    global Monitoring
    global running
    Monitoring = 1
    running += 1
    longest = 0
    loops = 0;
    totalTime = 0
    
    print('I\'m eating glass')
    channel = (bagelresponse.channel)  
    while Monitoring:
        datetime_LA = datetime.now(tz_LA)
        newtime = time.time()
        loops += 1

        if (delayFlag != 0):
            await channel.send("Delay between invasion commands:\n" + str(newtime - timeBetweenInstances))
        
        if running > 1:
            await channel.send("Monitoring already in progress! Idiot!")
            break
        
        # Format the time as a string
        ToonTime = datetime_LA.strftime("%H:%M:%S") 
        
        NewCoglist = getinvasions(Coglist)
        
        if isinstance(Coglist, str) == False:
            if isinstance(Coglist, int) == False:
                return error[2]
            return error[Coglist]
            
        
        bagelresponse = '\n\n'.join((NewCoglist))
        
        #no invasions error handling
        if not bagelresponse:
            bagelresponse = "Oh god oh fuck there are no invasions"
            
        #formatting
        bagelresponse = "## __Invasions at: " + ToonTime + " Toon time (PST)__\n" + bagelresponse
        await channel.send(bagelresponse)
     
        finishtime = time.time()
        timeTaken = (finishtime - newtime)

        totalTime += timeTaken
        
        avgTime = totalTime/loops
        avgStr = ("Average time: " + str(round(avgTime,2)) + "\n")
        
        timeTakeStr = ("Time taken: " + str(round(timeTaken,2)) + "\n")
        
        if (longest < timeTaken):
            longest = timeTaken
        longTimeStr = ("Longest time taken: "+ str(round(longest,2)) + "\n")

        await channel.send(avgStr + timeTakeStr + longTimeStr)           
        
        #deletes list at the end 
        del bagelresponse    
        del Coglist[:]        
        delayFlag += 1
        timeBetweenInstances = time.time()
        #runs every 8 minutes 
        await asyncio.sleep(500)
    running = 1
    
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command(name = 'Bateman')
#TODO more movies?
#silly function to test message functionality. left in as it tests bot's simple commands
async def bateman(ctx):
   
    am_psycho_quotes = ['Feed me a stray cat.',
                        'I have to return some videotapes.',
                        'Do you like Huey Lewis and The News?',
                        'Yes it is! In \'87, Huey released this, Fore, their most accomplished album. ' +
                        'I think their undisputed masterpiece is "Hip to be Square", a song so catchy, most people probably don\'t ' +
                        'listen to the lyrics. But they should, because it\'s not just about the pleasures of conformity, and the ' +
                        'importance of trends, it\'s also a personal statement about the band itself.',
                        'Hey Paul!',
                        'Try getting a reservation at Dorsia now, you fucking stupid bastard!',
                        'Let\'s see Paul Allen\'s card.',
                        'Just cool it with the anti-Semitic remarks.',
                        'There are no more barriers to cross. All I have in common with the uncontrollable and the insane, the vicious ' +
                        'and the evil, all the mayhem I have caused and my utter indifference toward it I have now surpassed. '+
                        'My pain is constant and sharp, and I do not hope for a better world for anyone. In fact, I want my '+
                        'pain to be inflicted on others. I want no one to escape. But even after admitting this, there is no catharsis; '+
                        'my punishment continues to elude me, and I gain no deeper knowledge of myself. No new knowledge can be extracted '+
                        'from my telling. This confession has meant nothing.',
                        'There is a moment of sheer panic when I realize that Paul\'s apartment overlooks the park... and is obviously more '+
                        'expensive than mine.',
                        'Impressive. Very nice.',
                        'Why not, you stupid bastard?',
                        'I\'m just a happy camper! Rockin\' and a-rollin\'!',
                        'Hi, this is Paul Allen. I\'m being called away to London for a few days. Meredith, I\'ll call you when I get back. ' +
                        'Hasta la vista, baby']
    response = random.choice(am_psycho_quotes) 
    await ctx.send(response)

Coglist = []
Numlist =[]
DistrictList =[] #do i need this?

#invasions can be manually grabbed
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command(name = 'invasions')
async def coginvasions(ctx):
    channel = (ctx.channel)
    newtime = time.time()
    
    await ctx.send("Grabbing invasions...")
    
    NewCoglist = getinvasions(Coglist)
    
    if isinstance(NewCoglist, list) == False:
        bagelresponse = error[NewCoglist]
    else: 
        bagelresponse = '\n\n'.join((NewCoglist))
    
    if not bagelresponse:
        bagelresponse = "Oh god oh fuck there are no invasions"
        
    await ctx.send(bagelresponse)
    finishtime = time.time()
    timetaken = (finishtime - newtime)
    await channel.send("Time taken:\n" + str(round(timetaken,2)))
       
    del bagelresponse    
    del Coglist[:]
    
#TODO - implement message sending to users that opt in for a specific cog or suit type
#TODO add better comments
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command(name = 'whatsnew')    
async def whatsnew(ctx):
   
    response = 'Bagelbot 1.4\nChangelog: Added better error handling and increased efficiency of message sending. ' \
               'Time and stop function slightly improved. More: https://github.com/lucas56847/bageler'
    await ctx.send(response)
    
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command(name = 'time')
async def timer(ctx):
    bageltime = round((time.time() - starttime)/3600,1)
    await ctx.send("Bageler has been running since: " + str(startdate) +  " \t" + str(bageltime) + " hours")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("You are on cooldown for another %.2fs." %error.retry_after)
    #raise error
#async def on_message(self, message):
#    if message.author.id == self.user.id:
#        return
 #   if message.content.startswith('!') and len(message.content) > 1:
 #       channel = client.get_user(message.author.id)
 #      await asyncio.sleep(10)
        
bot.run(token)

