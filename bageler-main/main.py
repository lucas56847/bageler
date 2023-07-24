import os, time, asyncio, pytz
import discord,random, requests
from array import *
from datetime import datetime
from bs4 import BeautifulSoup
from invasion import *
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

#TODO implement linux compatibility with .env file loading procedure
#TODO error handling
#TODO get rid of nohup: nohup command >/dev/null 2>&1 
token = os.getenv("token")
guildname = os.getenv('discord_guild')
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
tz_LA = pytz.timezone('America/Los_Angeles') 
# Get the correct timezone for use later when bot is running
#PST for Toon time

#confirms that the bot is online
@bot.event
async def on_ready():
    channel = (bot.get_channel(1117126591370235948) or await bot.fetch_channel(1117126591370235948))
    await channel.send("The Bageler emerges!")
    
#monitor function that monitors the invasion every ~8 minutes  
@bot.command(name = 'monitor')
async def monitor(bagelresponse):
    Monitoring = 1
    print('I\'m eating glass')
    channel = (bot.get_channel(1117126591370235948) or await bot.fetch_channel(1117126591370235948))  
    while Monitoring:
        datetime_LA = datetime.now(tz_LA)
        running = 1
        if running:
            await channel.send("Monitoring already in progress! Idiot!")
            break
        
        # Format the time as a string
        ToonTime = datetime_LA.strftime("%H:%M:%S") 
        
        NewCoglist = getinvasions(Coglist)
        bagelresponse = '\n\n'.join((NewCoglist))
        
        
        #no invasions error handling
        if not bagelresponse:
            bagelresponse = "Oh god oh fuck there are no invasions"
        #formatting
        bagelresponse = "## __Invasions at: " + ToonTime + " Toon time (PST)__\n" + bagelresponse
        await channel.send(bagelresponse)
        
        #deletes list at the end 
        del bagelresponse    
        del Coglist[:]        
        #runs every 8 minutes 
        await asyncio.sleep(500)
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
                        'expensive than mine',
                        'Impressive. Very nice.',
                        'Why not, you stupid bastard?',
                        'I\'m just a happy camper! Rockin\' and a-rollin\'!',
                        'Hi, this is Paul Allen. I\'m being called away to London for a few days. Meredith, I\'ll call you when I get back. ' +
                        'Hasta la vista, baby']
    response = random.choice(am_psycho_quotes) 
    await ctx.send(response)

Coglist = []
Numlist =[]
DistrictList =[]

#invasions can be manually grabbed
@bot.command(name = 'invasions')
async def coginvasions(ctx):
    await ctx.send("Grabbing invasions...")
    NewCoglist = getinvasions(Coglist)
    bagelresponse = '\n\n'.join((NewCoglist))
    if not bagelresponse:
        bagelresponse = "Oh god oh fuck there are no invasions"
    await ctx.send(bagelresponse)
    del bagelresponse    
    del Coglist[:]
#TODO - implement message sending to users that opt in for a specific cog or suit type
#TODO add better comments
    
@bot.command(name = 'test')
async def test(channel):
    await channel.send("test")
bot.run(token)

