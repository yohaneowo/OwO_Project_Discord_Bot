from discord.ext.commands import Cog
from discord.ext import commands
import discord




class SoundBoard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def CheckVoiceConnectedAndPlay(self, ctx, SoundLocation):
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
        voice.play(discord.FFmpegPCMAudio("./lib/SoundLib/"+SoundLocation))

    @Cog.listener()
    async def on_ready(self):
        print("SoundBoard_cog ready")
        await self.bot.stdout.send("**-SoundBoard Cog Ready**")

    # Rick And Morty

    @commands.command(name="cando")
    async def cando(self, ctx):
        await self.CheckVoiceConnectedAndPlay(ctx, "can-do.mp3")


    @commands.command(name="genius")
    async def genius(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "genius.mp3")

    @commands.command(name="wgn")
    async def wgn(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "going.mp3")

    @commands.command(name="ctnm")
    async def ctnm(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "i-cant-take-it-anymore.mp3")


    @commands.command(name="impress")
    async def impress(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "impress.mp3")

    @commands.command(name="ohnice")
    async def ohnice(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ohh-nice.mp3")


    @commands.command(name="ohokay")
    async def ohokay(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ohh-okay.mp3")

    @commands.command(name="ohyeah")
    async def ohyeah(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ooah-yeah.mp3")

    @commands.command(name="failure")
    async def failure(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "your-failures-are-your-own-old-man.mp3")

    @commands.command(name="tax")
    async def tax(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "tax.mp3")

    @commands.command(name="yes")
    async def yes(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "yes.mp3")


    @commands.command(name="watchtv")
    async def watchtv(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nobody-exists-on-purpose.mp3")

    @commands.command(name="dis")
    async def disqualified(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "disqualified.mp3")

    @commands.command(name="show")
    async def show(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "show.mp3")

    @commands.command(name="got")
    async def got(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "got.mp3")





    # Memes
    @commands.command(name="listen")
    async def dis(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "hey_listen.mp3")


    @commands.command(name="mine")
    async def mine(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "mine.mp3")

    @commands.command(name="ohhhh")
    async def ohhhh(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ohhhh.mp3")

    @commands.command(name="fbi")
    async def fbi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "fbi.mp3")

    @commands.command(name="illu")
    async def illu(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "illuminati.mp3")

    @commands.command(name="nani")
    async def nani(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nanii.mp3")

    @commands.command(name="st")
    async def st(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "sadtrombone.mp3")

    @commands.command(name="fail")
    async def fail(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "fail.mp3")

    @commands.command(name="haiya")
    async def haiya(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "haiya.mp3")

    @commands.command(name="nanilong")
    async def nanilong(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nanilong.mp3")

    @commands.command(name="ok")
    async def ok(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ok.mp3")

    @commands.command(name="boi")
    async def boi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "boi.mp3")

    @commands.command(name="ohno")
    async def ohno(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "oh-no-no-no-no-laugh.mp3")

    @commands.command(name="ara")
    async def ara_akeno(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ara-ara.mp3")

    @commands.command(name="bruh")
    async def bruh(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "bruh.mp3")

    @commands.command(name="nope")
    async def nope(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nope.mp3")

    @commands.command(name="fuckup")
    async def fuckup(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "fuckup.mp3")

    @commands.command(name="damn")
    async def damn(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "damn-son-whered-you-find-this.mp3")

    @commands.command(name="english")
    async def english(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "english.mp3")

    @commands.command(name="hello")
    async def hello(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "hello.mp3")

    @commands.command(name="bye")
    async def bye(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "bye-have-a-great-time.mp3")

    @commands.command(name="sadvio")
    async def sadvio(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "SadViolin.mp3")

    @commands.command(name="sadpia")
    async def sadpia(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "SadPiono.mp3")



    # Dota

    @commands.command(name="spicy")
    async def spicy(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "its-looking-spicy.mp3")

    @commands.command(name="ei")
    async def ei(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ei.mp3")

    @commands.command(name="youup")
    async def youup(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "youup.mp3")

    @commands.command(name="playdota")
    async def playdota(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "playdota.mp3")

    @commands.command(name="waow")
    async def waow(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "waow.mp3")

    @commands.command(name="xiongdei")
    async def xiongdei(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "xiongdei.mp3")

    @commands.command(name="666")
    async def six(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "666.mp3")

    @commands.command(name="jiqi")
    async def jiqi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "jiqi.mp3")

    @commands.command(name="history")
    async def history(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "no-one-has-ever-done-that-in-the-history-of-dota_2.mp3")


    # Trolled

    @commands.command(name="join")
    async def join(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "joined.mp3")

    @commands.command(name="message")
    async def message(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "message.mp3")

def setup(bot):
    bot.add_cog(SoundBoard(bot))

