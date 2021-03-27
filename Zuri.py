import discord
from discord.ext import commands 
import asyncio 
import datetime 
import sys
import os
from discord.ext.commands import (CommandOnCooldown)

zuri = commands.Bot(command_prefix='', case_insensitive=True)
zuri.remove_command("help")

@zuri.event
async def on_ready():
    await zuri.change_presence(status=discord.Status.online, activity=discord.Game('with Shadow'))
    print('I am Online')
'''
@zuri.event
async def on_message(msg):
    if ":" == msg.content[0] and ":" == msg.content[-1]:
        emoji_name = msg.content[1:-1]
        for emoji in msg.guild.emojis:
            if emoji_name == emoji.name:
                await msg.delete()
                await msg.channel.send(str(emoji))
                break

    await zuri.process_commands(msg)
'''
@zuri.command()
async def eh(ctx):
    await ctx.send('Eh ~')

'''
@zuri.command()
async def ily(ctx,):
    await ctx.author.send('I Love you too ❤ ~')
'''
@zuri.command()
async def chillbus(ctx):
    await ctx.send('Alright, board the bus 🚌! ~')

@zuri.command()
async def ily(ctx, user: discord.Member):
    await ctx.author.send('I am taken ;3')



#CUSTOM COMMANDS
'''
@zuri.command()
async def create(self, ctx, name, *, output):
    # First check if there's a custom command with that name already
    existing_command = self._custom_commands.get(name)
    # Check if there's a built in command, we don't want to override that
    if existing_command is None and ctx.bot.get_command(name):
        return await ctx.send(f"A built in command with the name {name} is already registered")

    # Now, if the command already exists then we just need to add/override the message for this guild
    if existing_command:
        self._custom_commands[name][679671356593274881] = output
    # Otherwise, we need to create the command object
    else:
        @zuri.command(name=name, help=f"Custom command: Outputs your custom provided output")
        @guild_check(self._custom_commands)
        async def cmd(self, ctx):
            await ctx.send(self._custom_commands[ctx.invoked_with][679671356593274881])
    await ctx.send(f"Added a command called {name}")

@zuri.command()
async def remove_command(self, ctx, name):
    # Make sure it's actually a custom command, to avoid removing a real command
    if name not in self._custom_commands or ctx.guild.id not in self._custom_commands[name]:
        return await ctx.send(f"There is no custom command called {name}")
    # All that technically has to be removed, is our guild from the dict for the command
    del self._custom_commands[name][ctx.guild.id]
    await ctx.send(f"Removed a command called {name}")
'''
'''
@zuri.command(pass_context=True)
@commands.has_role("Greeting Squad 🥇") 
async def welcome(ctx, member: discord.Member = None, role: discord.Role = None):
    await ctx.add_roles(member, role)
'''

zuri.run("...")
