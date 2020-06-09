"""
discord bot in python
Provisional Name: Tom BOTbadil
"""
#import libraries
import discord
from discord.ext import commands
import json
import random

#get token from config.json
with open('config.json') as json_file:
    config = json.load(json_file)
    bot_token = config['token']

#create bot instance
client = commands.Bot(command_prefix='.')

# ---/ Events /---
@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# ---/ Commands /---

#Note: function is named the same as the command
@client.command()
async def ping(ctx): #ctx = context
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command(aliases=['8ball'])
#Note: python does not allow functions starting by numbers
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes – definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    #delete also the clear command itself
    await ctx.channel.purge(limit=amount+1)

client.run(bot_token)