import discord
from discord.ext import commands
# from discord.ext import has_permissions, CheckFailure
import logging

logging.getLogger('mainLogger')


class SettingsCog(commands.Cog, name='Settings'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='site', help='$wiki site http://site.com | enter wiki site')
    # @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def set_wiki_site(self, ctx, *args):
        logging.info("{} wrote message: $wiki site {}".format(ctx.author, ' '.join(args)))
        if ctx.message.author.guild_permissions.administrator:
            logging.info("User is a server administrator")
            await ctx.send("you CAN use this command")
        else:
            logging.info("User is not a server administrator")
            await ctx.send("You do not have permissions to use this command.")
