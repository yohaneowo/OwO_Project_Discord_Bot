from lib.bot import bot
from keep_alive import keep_alive

VERSION = "0.0.1"

keep_alive()
bot.run(VERSION)