import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = 'token'

class qabot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["!"])
        self.load_extension('qa')

    async def on_ready(self):
        logging.info(f'{self.user.name} Ready!\n')

    async def on_message(self, msg):
        await self.process_commands(msg)

qabot().run(TOKEN)
