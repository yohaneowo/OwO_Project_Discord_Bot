import random

from discord.ext.commands import Cog
from discord.ext import tasks, commands
import discord


class RandomTimeRandomSound(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("RandomTimeRandomSound cog ready")

    @tasks.loop(minutes=random.randint(2, 4))
    async def check_voice_connected_and_play(self, ctx):
        sound_name = ["Acho1.mp3",
                      "Acho2.mp3",
                      "Ah1.mp3",
                      "Hic1.mp3",
                      "Hic2.mp3",
                      "Hic3.mp3",
                      "Hic4.mp3"]

        random_sound = random.choice(sound_name)

        if not ctx.message.author.voice:
            await ctx.send("You are not connected to channel")
        else:
            channel = ctx.message.author.voice.channel
            if ctx.voice_client is None:
                await channel.connect()
            else:
                if not ctx.voice_client.channel == channel:
                    await ctx.voice_client.disconnect()
                    await channel.connect()
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.stop()
        voice.play(discord.FFmpegPCMAudio("./lib/RandomSoundLib//" + random_sound))

    @commands.command(name="GOGOGO")
    async def gogogo(self, ctx):
        await self.check_voice_connected_and_play.start(ctx)

    @commands.command(name="NONONO")
    async def noonono(self, ctx):
        self.check_voice_connected_and_play.cancel()
        print("stopped")


def setup(bot):
    bot.add_cog(RandomTimeRandomSound(bot))
