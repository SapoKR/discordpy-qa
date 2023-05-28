import discord
from discord.ext import commands

data = dict()

class qa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        if message.author.id != self.bot.user.id:
            if msg in data:
                await message.channel.send(data[msg])

    @commands.command()
    async def 커맨드생성(self, msg, a, b):
        data[a] = b
        await msg.send('성공')

def setup(bot):
    bot.add_cog(qa(bot))
