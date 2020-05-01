import os
import discord
from discord.utils import get
from dotenv import load_dotenv

client = discord.Client()

async def addReactions(message):
    #Reacts the X and Rocket emoji to  messages sent in the to-do channel
    if(message.channel.name == "to-do"):
        await message.add_reaction("\U0001F680") #rocket
        await message.add_reaction("\U0000274C") #cross

async def todo(reaction):
    inProgressID = discord.utils.get(reaction.message.guild.text_channels, name="in-progress")
    #This is important so that it doesn't use the bot's reactions for actions
    if(reaction.count >= 2):
        #If the reaction emoji is a cross, delete the to-do-list item
        if(reaction.emoji == "\U0000274C"):
            await reaction.message.delete()
        #If the reaction emoji is a rocket, forward the to-do-list item to the in-progress channel and delete it from the to-do channel
        if(reaction.emoji ==  "\U0001F680"):
            await inProgressID.send(str(reaction.message.author) + ": " + str(reaction.message.content))
            await reaction.message.delete()