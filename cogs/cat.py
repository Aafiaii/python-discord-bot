"""Module for generating a random cat picture"""

import json

import requests
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType


class Cat(commands.Cog):
    """Cat command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["meow", "kitty", "pisi"])
    @cooldown(1, 5, BucketType.user)
    async def cat(self, ctx):
        """Get a cat image"""
        req = requests.get("https://api.thecatapi.com/v1/images/search")
        if req.status_code != 200:
            await ctx.message.add_reaction("❌")
            await ctx.send("API error, could not get a meow")
            print("Could not get a meow")
        catlink = json.loads(req.text)[0]
        rngcat = catlink["url"]
        await ctx.send(
            content=f"Here's a random cat for you {ctx.author.mention}!\n{rngcat}"
        )
        await ctx.message.add_reaction("✅")


async def setup(bot):
    await bot.add_cog(Cat(bot))
