import os
import logging
import logging.config
import discord
from discord.ext import commands
from sys import exc_info

from EasterEggCog import EasterEggCog
from SettingsCog import SettingsCog

logging.config.fileConfig('logging.conf')
logging.getLogger('mainLogger')

token = os.getenv('DISCORD_BOT_TOKEN')
client_user = os.getenv('CLIENT_USER')
client_id = os.getenv('CLIENT_ID')
bot = commands.Bot(command_prefix='$ ', pm_help=False)
bot.add_cog(EasterEggCog(bot))
# EVENTS

@bot.event
async def on_connect():
    logging.info("----------------------")
    logging.info("Bot is connected to discord")
    logging.info("----------------------")


@bot.event
async def on_ready():
    logging.info("----------------------")
    logging.info("Logged in as: {}".format(bot.user.name))
    logging.info("----------------------")


@bot.event
async def on_error(event, *args, **kwargs):
    logging.error("---- ERROR ----")
    logging.error("Error from:", event)
    logging.error("Error context:", args, kwargs)

    exc_type, value, traceback = exc_info()
    logging.error("Exception type:", exc_type)
    logging.error("Exception value:", value)
    logging.error("Exception traceback object:", traceback)


# UTILITY


# RUN BOT

bot.run(token)
