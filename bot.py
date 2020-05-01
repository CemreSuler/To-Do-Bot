#bot.py
#loading in the dependencies
import os
import discord
from discord.utils import get
from dotenv import load_dotenv
import createChannels
import todo
import inprogress
import finished
import deleted

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
    await todo.addReactions(message)
    await inprogress.addReactions(message)
    await finished.addReactions(message)
    await deleted.addReactions(message)

@client.event
#Calls this event whenever the user reacts to a message with an emoji
async def on_reaction_add(reaction,user):
    todoID = discord.utils.get(reaction.message.guild.text_channels, name="to-do")
    inProgressID = discord.utils.get(reaction.message.guild.text_channels, name="in-progress")
    finishedID = discord.utils.get(reaction.message.guild.text_channels, name="finished")
    deletedID = discord.utils.get(reaction.message.guild.text_channels, name="deleted")
    if(reaction.message.channel == todoID):
        await todo.todo(reaction)
    if(reaction.message.channel == inProgressID):
        await inprogress.inprogress(reaction)
    if(reaction.message.channel == finishedID):
        await finished.finished(reaction)
    if(reaction.message.channel == deletedID):
        await deleted.deleted(reaction)

    
client.run(TOKEN)
