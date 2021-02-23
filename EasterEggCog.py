import discord
from discord.ext import commands


class EasterEggCog(commands.Cog, name='Secret'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pikachu', help='this is a surprise pikachu response, custom for users')
    async def pikachu(self, ctx, *arg):
        # str(ctx.author) == 'ctrl-vee#8271' or
        if str(ctx.author) == 'sirdragonkitty#2093':
            await ctx.send("{0} is surprised".format(ctx.author.display_name))
            await ctx.send(file=discord.File('images/shocked_pikachu.png'))
        else:
            await ctx.send('The family has not authorized you to use this command.')

    @commands.command(name='pikachuadmin')
    async def pikachu_admin(self, ctx, *arg):
        if str(ctx.author) == 'ctrl-vee#8271':
            await ctx.send("{0} is surprised".format(ctx.author.display_name))
            await ctx.send(file=discord.File('images/shocked_pikachu.png'))
        else:
            await ctx.send('only Vee can use this command.')

    @commands.command(name='imshocked')
    async def pikachu_custom(self, ctx):
        await ctx.send("{0} is surprised".format(ctx.author.display_name))
        await ctx.send(file=discord.File('images/shocked_pikachu.png'))
