import os
import discord
from discord.utils import get
import json

client = discord.Client()

async def setup(message):
    #Checks if it was a human that sent the message
    if message.author == client.user:
        return
    #Setup command that you can run everywhere
    if message.content == "td!setup":
        #Checks if there is a tasks category and creates it if there isn't
        if (discord.utils.get(message.guild.categories, name="tasks")):
            await message.channel.send("There is already a category with the name 'tasks', so I won't create a new one")
        else:
            await message.channel.send("There is no category with the name 'tasks', I'll create one for you now!")
            await message.guild.create_category_channel('tasks')

        #Gets the ID of the 'tasks' category so it can get passed through to the text-channel creator
        categoryID = discord.utils.get(message.guild.categories, name="tasks")

        #Checks if there is a to-do channel and creates it if there isn't
        if (discord.utils.get(message.guild.text_channels, name="to-do")):
            await message.channel.send("There is already a text-channel with the name 'to-do', so I won't create a new one")
        else:
            await message.channel.send("There is no text-channel with the name 'to-do', I'll create one for you now!")
            await message.guild.create_text_channel('to-do',category=categoryID)
        
        #Checks if there is an in-progress channel and creates it if there isn't
        if (discord.utils.get(message.guild.text_channels, name="in-progress")):
            await message.channel.send("There is already a text-channel with the name 'in-progress', so I won't create a new one")
        else:
            await message.channel.send("There is no text-channel with the name 'in-progress', I'll create one for you now!")
            await message.guild.create_text_channel('in-progress',category=categoryID)
        
        #Checks if there is a finished channel and creates it if there isn't
        if (discord.utils.get(message.guild.text_channels, name="finished")):
            await message.channel.send("There is already a text-channel with the name 'finished', so I won't create a new one")
        else:
            await message.channel.send("There is no text-channel with the name 'finished', I'll create one for you now!")
            await message.guild.create_text_channel('finished',category=categoryID)

        #Checks if there is a deleted channel and creates it if there isn't
        if (discord.utils.get(message.guild.text_channels, name="deleted")):
            await message.channel.send("There is already a text-channel with the name 'deleted', so I won't create a new one")
        else:
            await message.channel.send("There is no text-channel with the name 'deleted', I'll create one for you now!")
            await message.guild.create_text_channel('deleted',category=categoryID)

    guildID = message.guild.id
    todoID = discord.utils.get(message.guild.text_channels, name="to-do")
    inProgressID = discord.utils.get(message.guild.text_channels, name="in-progress")
    finishedID = discord.utils.get(message.guild.text_channels, name="finished")
    deletedID = discord.utils.get(message.guild.text_channels, name="deleted")
    

    guildData = {
        guildID: {
            "todoID":todoID.id,
            "inProgressID":inProgressID.id,
            "finishedID":finishedID.id,
            "deletedID":deletedID.id
        }
    }
    
    with open("database.json", "w") as write_file:
        json.dump(guildData, write_file)
