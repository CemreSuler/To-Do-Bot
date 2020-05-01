# bot.py
import os

import discord
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'NzA1Nzg0NDU0NzI3MzM1OTM2.Xqw56w.17hlBidfGbewgCyWOUMV4nc2mEE'
GUILD = '705112198585778186'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    rightChannel = discord.get_channel("705825738850435072")
    if message.author == client.user:
        return
    if len(message.content) > 0:
        if (message.channel == rightChannel):
            await message.channel.send("Er zou nu een emoji moeten worden toegevoegd.")
            await message.add_reaction("\U0001F680")
            await message.add_reaction("\U0000274C")

client.run(TOKEN)
