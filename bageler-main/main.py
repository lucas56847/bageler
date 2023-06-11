import os
import discord,random, requests
from array import *
from bs4 import BeautifulSoup
from invasion import *
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

token = os.getenv("token")
guildname = os.getenv('discord_guild')
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
intents.reactions = True
intents.guilds = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents = intents)


@bot.listen()
async def on_ready():
    print('I\'m eating glass')
    channel = (bot.get_channel(1117126591370235948) or await bot.fetch_channel(1117126591370235948))  
    while True:
        NewCoglist = getinvasions(Coglist)
        bagelresponse = '\n\n'.join((NewCoglist))
        if not bagelresponse:
            bagelresponse = "Oh god oh fuck there are no invasions"
        bagelresponse = "Invasions Currently:\n" + bagelresponse
        await channel.send(bagelresponse)
        del bagelresponse    
        del Coglist[:]        
        #await channel.send("test")
        time.sleep(500)
@bot.command(name = 'Bateman')
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


@bot.event
async def on_update(update):
    await update.send("among us")
    
@bot.command(name = 'test')
async def test(channel):
    await channel.send("test")
bot.run(token)
client.run(token)

