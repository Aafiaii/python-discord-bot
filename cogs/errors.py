import asyncio
from discord.ext import commands
from tools import Embed


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_embed = Embed(type="error")

        if isinstance(error, commands.CommandOnCooldown):
            error_embed.description = f"This command is on cooldown. Please try again in **{error.retry_after:.1f}** seconds."
        elif isinstance(error, commands.MissingRequiredArgument):
            error_embed.description = f"Missing required argument: `{error.param.name}`. Please provide it and try again."
        elif isinstance(error, commands.CommandNotFound):
            error_embed.description = (
                "Command not found. Please check the command name and try again."
            )
        elif isinstance(error, commands.MissingPermissions):
            error_embed.description = "You do not have permission to use this command."
        else:
            raise error

        message = await ctx.send(content=f"{ctx.author.mention}", embed=error_embed)
        await asyncio.sleep(5)
        await message.delete()


async def setup(bot):
    await bot.add_cog(Errors(bot))
