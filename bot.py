import discord
from discord.ext import commands

data = dict()

class bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        if msg.author.id == self.bot.user.id:
            pass
        else:
            for i in data:
                if i == msg:
                    await message.channel.send(data[msg])

    @commands.command()
    async def 커맨드생성(self, msg, a, b):
        data[a] = b
        await msg.send('성공')
