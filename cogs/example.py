#Cog Example

import discord
from discord.ext import commands
import random
import traceback
import sys

#inherits from commands.Cog
class Example(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ---/ events withing cogs /---
    @commands.Cog.listener()
    #we need self because we are in a class
    async def on_ready(self):
        print('Example Cog Loaded')

    # error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Note: if have this handler, you need to have a default error handling case
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command used')
        #if isinstance(error, commands.MissingRequiredArgument):
        #    await ctx.send('Please pass in all required arguments')
        
        # print traceback of not handled errors
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        print(error)

    # ---/ Commands /---
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(client.latency*1000)}ms')

    @commands.command(aliases=['8ball'])
    #Note: python does not allow functions starting by numbers
    async def _8ball(self, ctx, *, question):
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

    @commands.command()
    @commands.has_permissions(manage_messages=True) #permission check for a command
    async def clear(self, ctx, amount : int):
        #delete also the clear command itself
        await ctx.channel.purge(limit=amount+1)

    # command specific error handler
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to delete')


    def is_it_me(ctx):
        # test user id
        return ctx.author.id == 720331170289549452

    @commands.command()
    @commands.check(is_it_me)
    async def hello(self, ctx):
        await ctx.send(f"Hi, I'm {ctx.author}")
def setup(client):
    client.add_cog(Example(client))