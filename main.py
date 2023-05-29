import os
import discord,random, requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents = intents)


@client.event
async def on_ready():
    print(f'{client.user} has ARRIVED')
    print(f'list: {client.guilds}')
   # print(f'listmembers: {guild.members}')


    for guild in client.guilds:
        if guild.name == guildname:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

   # members = '\n - '.join([member.name for member in guild.members])
    for members in guild.members:
      print(f'Guild Member:\n - {members.name}')    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content =='hello':
        await message.channel.send("I'm eating glass.")
        return
    if message.content =='Julia':
        await message.channel.send(file=discord.File('agony.png'))
        return
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
    if message.content == 'Bateman':
        response = random.choice(am_psycho_quotes) 
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
        return
 
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
Coglist = []
@bot.command(name = 'invasions')
async def coginvasions(ctx):
    await ctx.send("Grabbing invasions...")
    NewCoglist = getinvasions(Coglist)
    bagelresponse = '\n'.join((NewCoglist))
    await ctx.send(bagelresponse)

bot.run(token)
#client.run(token)
