from discord.ext.commands import Cog
from discord.ext import commands
import discord
import asyncio


class SoundBoard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def whocallit(self, ctx):
        commandname = ctx.invoked_with
        username = ctx.message.author.display_name
        useravatar = ctx.message.author.avatar_url
        whocallem = discord.Embed(title="{1}{2}{0}{3}{4}".format(commandname, "*","*","*","*"), color=discord.Color.blue())
        whocallem.set_footer(text="Requested by {0} ".format(username), icon_url=useravatar)
        whocall = await ctx.send(embed=whocallem)
        await asyncio.sleep(10)
        await whocall.delete()


    async def CheckVoiceConnectedAndPlay(self, ctx, sound_title):
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
        voice.play(discord.FFmpegPCMAudio("../QAQ/lib/SoundLib/"+ sound_title))

    @Cog.listener()
    async def on_ready(self):
        print("SoundBoard_cog ready")
        await self.bot.stdout.send("**-SoundBoard Cog Ready**")



    # Rick And Morty

    @commands.command(name="dubdub")
    async def dub(self, ctx):
        await self.CheckVoiceConnectedAndPlay(ctx, "woo_vu_luvub_dub_dub.mp3")
        await self.whocallit(ctx)

    @commands.command(name="boo")
    async def boo(self, ctx):
        await self.CheckVoiceConnectedAndPlay(ctx, "boo-not-cool.mp3")
        await self.whocallit(ctx)

    @commands.command(name="cando")
    async def cando(self, ctx):
        await self.CheckVoiceConnectedAndPlay(ctx, "can-do.mp3")
        await self.whocallit(ctx)



    @commands.command(name="genius")
    async def genius(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "genius.mp3")
        await self.whocallit(ctx)


    @commands.command(name="wgn")
    async def wgn(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "going.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ctam")
    async def ctam(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "i-cant-take-it-anymore.mp3")
        await self.whocallit(ctx)



    @commands.command(name="impress")
    async def impress(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "impress.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ohnice")
    async def ohnice(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ohh-nice.mp3")
        await self.whocallit(ctx)




    @commands.command(name="ohokay")
    async def ohokay(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ohh-okay.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ohyeah")
    async def ohyeah(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ooah-yeah.mp3")
        await self.whocallit(ctx)


    @commands.command(name="failure")
    async def failure(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "your-failures-are-your-own-old-man.mp3")
        await self.whocallit(ctx)


    @commands.command(name="tax")
    async def tax(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "tax.mp3")
        await self.whocallit(ctx)


    @commands.command(name="yes")
    async def yes(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "yes.mp3")
        await self.whocallit(ctx)



    @commands.command(name="watchtv")
    async def watchtv(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nobody-exists-on-purpose.mp3")
        await self.whocallit(ctx)


    @commands.command(name="dis")
    async def disqualified(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "disqualified.mp3")
        await self.whocallit(ctx)


    @commands.command(name="show")
    async def show(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "show.mp3")
        await self.whocallit(ctx)


    @commands.command(name="got")
    async def got(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "got.mp3")
        await self.whocallit(ctx)



    #anime


    @commands.command(name="dame")
    async def dame(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "dame.mp3")
        await self.whocallit(ctx)



    @commands.command(name="tsumetai")
    async def tsumetai(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "tsumetai.mp3")
        await self.whocallit(ctx)


    @commands.command(name="id")
    async def id(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "id.mp3")
        await self.whocallit(ctx)


    @commands.command(name="yarashii")
    async def yarashii(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "senpaiyarashi.mp3")
        await self.whocallit(ctx)


    @commands.command(name="yarashi")
    async def yarashi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "yarashi.mp3")
        await self.whocallit(ctx)



    @commands.command(name="yada")
    async def yada(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx,"yada.mp3")
        await self.whocallit(ctx)



    @commands.command(name="yahallo")
    async def yahallo(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "yahallo-yuigahama-yui-yahari-ore-no-seishun-love-comedy-wa-machigatteiru.mp3")
        await self.whocallit(ctx)



    @commands.command(name="chunchunmaru")
    async def chunchunmaru(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "chunchunmaru.mp3")
        await self.whocallit(ctx)


    @commands.command(name="yamero")
    async def yamero(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "megumu-yamerooo.mp3")
        await self.whocallit(ctx)


    @commands.command(name="dondayo")
    async def dondayo(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "Chikas Doon da yo Kaguyasama wa Kokurasetai.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ara")
    async def ara_akeno(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ara-ara.mp3")
        await self.whocallit(ctx)


    # Memes
    @commands.command(name="xi")
    async def xi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "xi.mp3")
        await self.whocallit(ctx)

    @commands.command(name="giao")
    async def giao(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "giao.mp3")
        await self.whocallit(ctx)

    @commands.command(name="iamshabi")
    async def shabi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "shabi.mp3")
        await self.whocallit(ctx)

    @commands.command(name="amogus")
    async def amogus(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "AMOGUS.mp3")
        await self.whocallit(ctx)


    @commands.command(name="run")
    async def run(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "why-are-you-running-original-vine-audiotrimmer_pJyxLm1.mp3")
        await self.whocallit(ctx)



    @commands.command(name="wae")
    async def wae(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "do-you-know-the-way.mp3")
        await self.whocallit(ctx)



    @commands.command(name="gae")
    async def gae(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "gae.mp3")
        await self.whocallit(ctx)


    @commands.command(name="yooo")
    async def yooo(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "yoooooooooo-3.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ahshit")
    async def ahshit(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "gta-san-andreas-ah-shit-here-we-go-again.mp3")
        await self.whocallit(ctx)


    @commands.command(name="niggar")
    async def niggar(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "niggar.mp3")
        await self.whocallit(ctx)


    @commands.command(name="kiryu")
    async def kiryu(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "Kiryu Chan 龍が如く 極2.mp3")
        await self.whocallit(ctx)



    @commands.command(name="listen")
    async def dis(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "hey_listen.mp3")
        await self.whocallit(ctx)



    @commands.command(name="mine")
    async def mine(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "mine.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ohhh")
    async def ohhhh(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ohhhh.mp3")
        await self.whocallit(ctx)


    @commands.command(name="fbi")
    async def fbi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "fbi.mp3")
        await self.whocallit(ctx)


    @commands.command(name="illu")
    async def illu(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "illuminati.mp3")
        await self.whocallit(ctx)


    @commands.command(name="nani")
    async def nani(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nanii.mp3")
        await self.whocallit(ctx)


    @commands.command(name="st")
    async def st(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "sadtrombone.mp3")
        await self.whocallit(ctx)


    @commands.command(name="fail")
    async def fail(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "fail.mp3")
        await self.whocallit(ctx)


    @commands.command(name="haiya")
    async def haiya(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "haiya.mp3")
        await self.whocallit(ctx)


    @commands.command(name="nanilong")
    async def nanilong(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nanilong.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ok")
    async def ok(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ok.mp3")
        await self.whocallit(ctx)


    @commands.command(name="boi")
    async def boi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "boi.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ohno")
    async def ohno(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "oh-no-no-no-no-laugh.mp3")
        await self.whocallit(ctx)



    @commands.command(name="bruh")
    async def bruh(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "bruh.mp3")
        await self.whocallit(ctx)


    @commands.command(name="nope")
    async def nope(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "nope.mp3")
        await self.whocallit(ctx)


    @commands.command(name="fuckup")
    async def fuckup(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "fuckup.mp3")
        await self.whocallit(ctx)


    @commands.command(name="damn")
    async def damn(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "damn-son-whered-you-find-this.mp3")
        await self.whocallit(ctx)


    @commands.command(name="english")
    async def english(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "english.mp3")
        await self.whocallit(ctx)


    @commands.command(name="hello")
    async def hello(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "hello.mp3")
        await self.whocallit(ctx)


    @commands.command(name="bye")
    async def bye(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "bye-have-a-great-time.mp3")
        await self.whocallit(ctx)


    @commands.command(name="sadvio")
    async def sadvio(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "SadViolin.mp3")
        await self.whocallit(ctx)


    @commands.command(name="sadpia")
    async def sadpia(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "SadPiono.mp3")
        await self.whocallit(ctx)




    # Dota


    @commands.command(name="spicy")
    async def spicy(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "its-looking-spicy.mp3")
        await self.whocallit(ctx)


    @commands.command(name="ei")
    async def ei(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "ei.mp3")
        await self.whocallit(ctx)


    @commands.command(name="youup")
    async def youup(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "youup.mp3")
        await self.whocallit(ctx)


    @commands.command(name="playdota")
    async def playdota(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "playdota.mp3")
        await self.whocallit(ctx)


    @commands.command(name="waow")
    async def waow(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "waow.mp3")
        await self.whocallit(ctx)


    @commands.command(name="xiongdei")
    async def xiongdei(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "xiongdei.mp3")
        await self.whocallit(ctx)


    @commands.command(name="666")
    async def six(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "666.mp3")
        await self.whocallit(ctx)


    @commands.command(name="jiqi")
    async def jiqi(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "jiqi.mp3")
        await self.whocallit(ctx)


    @commands.command(name="history")
    async def history(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "no-one-has-ever-done-that-in-the-history-of-dota_2.mp3")
        await self.whocallit(ctx)



    # Trolled

    @commands.command(name="join")
    async def join(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "joined.mp3")

    @commands.command(name="message")
    async def message(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "message.mp3")

    @commands.command(name="disconnect")
    async def disconnect(self, ctx, channel: discord.VoiceChannel = None):
        await self.CheckVoiceConnectedAndPlay(ctx, "discord-leave.mp3")



def setup(bot):
    bot.add_cog(SoundBoard(bot))

