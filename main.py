# py -3 main.py

import os
import discord
from discord.ext import commands

token = os.getenv('DISCORD_BOT_TOKEN')
client_user = os.getenv('CLIENT_USER')
client_id = os.getenv('CLIENT_ID')
bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: {0}".format(client_user))
    print("----------------------")


@bot.command(name='test', help='this is a test command')
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(name='pikachu', help='this is a surprise pikachu response, custom for users')
async def pikachu(ctx, *arg):
    # str(ctx.author) == 'ctrl-vee#8271' or 
    if str(ctx.author) == 'sirdragonkitty#2093':
        await ctx.send("{0} is surprised".format(ctx.author.display_name))
        await ctx.send(file=discord.File('images/shocked_pikachu.png'))
    else:
        await ctx.send('The family has not authorized you to use this command.')


@bot.command(name='pikachuadmin')
async def pikachu_admin(ctx, *arg):
    if str(ctx.author) == 'ctrl-vee#8271':
        await ctx.send("{0} is surprised".format(ctx.author.display_name))
        await ctx.send(file=discord.File('images/shocked_pikachu.png'))
    else:
        await ctx.send('only Vee can use this command.')


bot.run(token)
