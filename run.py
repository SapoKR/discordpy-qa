import discord
from discord.ext import commands

TOKEN = 'token'

class qabot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["!"])
        self.load_extension('bot')

    async def on_readys(self):
        print(self.user.name, 'Ready!')
        print('\n')

    async def on_message(self, msg):
        await self.process_commands(msg)

qabot().run(TOKEN)
