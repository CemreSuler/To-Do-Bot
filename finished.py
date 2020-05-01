import os
import discord
from discord.utils import get
from dotenv import load_dotenv

client = discord.Client()

async def addReactions(message):
    #Reacts the checkmark, go-back and X emoji to messages sent in the to-do channel
    if(message.channel.name == "finished"):
        await message.add_reaction("\U000021A9") #go-back
        await message.add_reaction("\U0000274C") #delete

async def finished(reaction):
    todoID = discord.utils.get(reaction.message.guild.text_channels, name="to-do")
    deletedID = discord.utils.get(reaction.message.guild.text_channels, name="deleted")
    #This is important so that it doesn't use the bot's reactions for actions
    if(reaction.count >= 2):
        #If the reaction emoji is a go-back emoji, send the to-do-list item back to the to-do channel and delete it from the in-progress channel
        if(reaction.emoji ==  "\U0001F680"):
            await todoID.send(reaction.message.content)
            await reaction.message.channel.send("Sent '" + str(reaction.message.content) + "' to the to-do channel! (Removing this in 3 seconds)", delete_after=3)
            await reaction.message.delete()

        #If the reaction emoji is a cross, delete the to-do-list item
        if(reaction.emoji == "\U0000274C"):
            await deletedID.send(reaction.message.content)
            await reaction.message.channel.send("Deleted '" + str(reaction.message.content) + "'  (Removing this in 3 seconds)", delete_after=3)
            await reaction.message.delete()

           