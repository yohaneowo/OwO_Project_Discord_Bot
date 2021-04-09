import discord
from discord.ext.commands import Bot as BotBase
from glob import glob
from discord import Intents
import os

PREFIX="<"
OWNER_IDS=[824589815130357760]
COGS=[path.split("\\")[-1][:-3]for path in glob ("./Cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self,cog ,False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog ready")

    def all_ready(self):

        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
    def __init__(self):
      self.PREFIX = PREFIX 
      
      super().__init__(
        command_prefix=PREFIX,
        owner_ids=OWNER_IDS,
        intents=Intents.all()
      )

    def setup(self):
      for cog in COGS:
        self.load_extention(f"lib.cogs.{cog}")
        print(f"{cog}Cog Loaded")
      
      print("setup done")


    async def on_connect(self):
        print("Bot Connected")

    async def on_disconnect(self):
        print("Bot disconnected")


client = discord.Client()

def setupBot(self):
    for cog in COGS:
      client.load_extention(f"lib.cogs.{cog}")
      print(f"{cog}Cog Loaded")

    print("setup done")


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))
  setupBot()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  

client.run(os.getenv('TOKEN'))