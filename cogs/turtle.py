from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from database.models import Turtle as TurtleModel
from tools import Embed


class Turtle(commands.Cog):
    """Turtle command"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["michelangelo"])
    @cooldown(3, 5, BucketType.user)
    async def create_turtle(self, ctx, *, name: str):
        """Create a turtle"""
        existing = TurtleModel.objects(name=name).first()

        if existing:
            error_embed = Embed(type="error")
            error_embed.description = f"A turtle with the name `{name}` already exists."
            await ctx.send(embed=error_embed)
            return

        success_embed = Embed(type="success")
        new_turtle = TurtleModel(name=name)
        new_turtle.save()

        success_embed.description = f"Successfully created a turtle named `{name}`!"
        await ctx.send(embed=success_embed)

    @commands.command(aliases=["turtles"])
    @cooldown(3, 5, BucketType.user)
    async def list_turtles(self, ctx):
        """List all turtles"""
        turtles = TurtleModel.objects()
        if not turtles:
            error_embed = Embed(type="error")
            error_embed.description = "No turtles found."
            await ctx.send(embed=error_embed)
            return

        turtle_list = "\n".join([f"- {turtle.name}" for turtle in turtles])
        success_embed = Embed(type="info")
        success_embed.description = f"Here are the turtles:\n{turtle_list}"
        await ctx.send(embed=success_embed)


async def setup(bot):
    await bot.add_cog(Turtle(bot))
