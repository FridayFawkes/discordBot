#User Cog
# for things related with join, leave, kick, ban users, etc

import discord
from discord.ext import commands

#inherits from commands.Cog
class User_cog(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # ---/ events withing cogs /---
    @commands.Cog.listener()
    #we need self because we are in a class
    async def on_ready(self):
        print('User Management Cog Loaded')
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    @commands.Cog.listener()    
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')
    
    
    
    # ---/ Commands /---
    @ commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    async def unban(self, ctx, *, member):
        #get list of banned users
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return



def setup(client):
    client.add_cog(User_cog(client))