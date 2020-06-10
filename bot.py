"""
discord bot in python
Provisional Name: Tom BOTbadil
"""
#import libraries
import discord
from discord.ext import commands, tasks
from itertools import cycle
import json
import os

#get token from config.json
with open('config.json') as json_file:
    config = json.load(json_file)
    bot_token = config['token']

#create bot instance
client = commands.Bot(command_prefix='.')
status = cycle(['Status 1', 'Status 2'])

# ---/ Events /---
@client.event
async def on_ready():
    # set bot status
    # await client.change_presence(status=discord.Status.dnd, activity=discord.Game("I am afraid I can't do that Dave."))
    # start the task
    # change_status.start()
    print('Bot is ready.')


# ---/ Commands /---

#Note: function is named the same as the command

# ---/ Tasks /---
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#  ---/ Cogs / ---
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


#before running client, load all cogs
for filename in os.listdir('./cogs'):
    #check for .py extension
    if filename.endswith('.py'):
        #note: extension does not include .py
        client.load_extension(f'cogs.{filename[:-3]}')



client.run(bot_token)