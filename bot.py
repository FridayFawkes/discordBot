"""
discord bot in python
Provisional Name: Tom BOTbadil
"""
#import libraries
import discord
from discord.ext import commands
import json

#get token from config.json
with open('config.json') as json_file:
    config = json.load(json_file)
    bot_token = config['token']

#create bot instance
client = commands.Bot(command_prefix='.')

#create event
@client.event
async def on_ready():
    print('Bot is ready.')

#copy pasted token as parameter (from dev page of the bot)
client.run(bot_token)