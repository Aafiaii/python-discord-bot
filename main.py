import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from database import connect_to_db


def main():
    load_dotenv()

    class Bot(commands.Bot):
        def __init__(self):
            super().__init__(
                command_prefix=os.getenv("PREFIX"), intents=discord.Intents.all()
            )

        async def setup_hook(self):
            connect_to_db()
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    await self.load_extension(f"cogs.{filename[:-3]}")

    bot = Bot()

    bot.run(os.getenv("BOT_TOKEN"))


if __name__ == "__main__":
    main()
