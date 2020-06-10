#Another Cog Example

import discord
from discord.ext import commands

#inherits from commands.Cog
class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ---/ events withing cogs /---
    @commands.Cog.listener()
    #we need self because we are in a class
    async def on_ready(self):
        print('Test Cog Loaded')

    # ---/ Commands /---
    @commands.command()
    async def test(self, ctx):
        await ctx.send('Test!')

def setup(client):
    client.add_cog(Test(client))