import discord
from discord.ext import commands, tasks
from random import choice
from itertools import cycle


# 0.0
status =cycle(['我是谁？','我在哪？','我在干嘛？','Prefix = ]'])

class VoiceError(Exception):
    pass

class VoiceState:
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        self.bot = bot
        self._ctx = ctx
        self.voice = None


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ready = False
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.bot, ctx)
            self.voice_states[ctx.guild.id] = state
        return state

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)



    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.change_status.start()
            await self.bot.stdout.send("**-Misc Cog Ready**")
            await self.bot.stdout.send("`Status Loop On`")


            print("Misc online")



    # Status Loop,Fucking YES i did it
    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.Game(next(status)))


    # Commands
    @commands.command(name='ping', aliases=["p"])
    async def ping(self, ctx):
        await ctx.send(f'延迟...{round(self.bot.latency * 1000)}ms')



    @commands.command(name='summon')
    @commands.has_permissions(manage_guild=True)


    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):

        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel!")
            return
        else:
            channel = ctx.message.author.voice.channel
            if ctx.voice_client is None:
                await channel.connect()
            else:
                if not ctx.voice_client.channel == channel:
                    await ctx.voice_client.disconnect()
                    await channel.connect()
                else:
                    await ctx.send(f'Already Connected La')

    @commands.command(name="leave")
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()

        else:
            await ctx.send("The bot is not connected to a voice channel.")






def setup(bot):
    bot.add_cog(Misc(bot))