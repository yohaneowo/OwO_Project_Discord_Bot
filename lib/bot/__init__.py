#birthday 25/02/2021
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from glob import glob
from discord.ext import commands, tasks
from discord import Intents
from discord.ext.commands import CommandNotFound

PREFIX = ">"
OWNER_IDS =[814363262677418025]
COGS = [path.split("/")[-1][:-3] for path in glob("lib/cogs/*.py")]

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
        self.cogs_ready = Ready()
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all()
        )




    def setup(self):
        for cog in COGS:
            
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")

        print("setup complete")

    def run(self, version):
        self.VERSION = version

        print("running setup...")
        self.setup()
      

        self.Token = os.getenv('TOKEN')
        print("Running bot...Cheking Token")
        super().run(self.Token, reconnect=True)
        

        


    async def on_connect(self):
        print("Bot Connected")

    async def on_disconnect(self):
        print("Bot disconnected")

    # command error
    async def on_error(self, error, *args, **kwargs):
        if error == "on_command_error":
            await args[0].send("Something went Wrong...F")


        else:
            channel = self.get_channel(806692318185914418)
            await self.stdout.send("an error occured ")
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.send("Wrong Commnands")
            pass

        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc




    # ready
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(650357594447413276)
            self.stdout = self.get_channel(806692318185914418)
            print("Bot is Online")

            await self.stdout.send("<3")

        else:
            print("Bot Reconnect?")





    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


        # difference
        if message.author == bot.user:
            return

        if message.content.startswith('$hello' ):
            await message.channel.send('hello')






bot = Bot()