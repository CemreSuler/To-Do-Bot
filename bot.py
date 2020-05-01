#bot.py
#loading in the dependencies
import os
import discord
from discord.utils import get
from dotenv import load_dotenv
import createChannels

#NEED TO FIX THIS WITH A BETTER ENV FILE!!
TOKEN = 'NzA1Nzg0NDU0NzI3MzM1OTM2.Xqw56w.17hlBidfGbewgCyWOUMV4nc2mEE'
GUILD = '705112198585778186'
client = discord.Client()

@client.event
#Tells to the console the bot is ready
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    

@client.event
#Calls this event whenever a message was sent to the server
async def on_message(message):
    await createChannels.createChannels(message)
    if(message.channel.name == "to-do"):
        await message.add_reaction("\U0001F680")
        await message.add_reaction("\U0000274C")

@client.event
async def on_reaction_add(reaction,user):
    if(reaction.count == 2):
        if(reaction.emoji == "\U0000274C"):
            await reaction.message.delete()

    
client.run(TOKEN)
