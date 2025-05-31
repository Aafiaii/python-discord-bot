import discord


class Embed(discord.Embed):
    def __init__(self, type=None):
        super().__init__(timestamp=discord.utils.utcnow())

        match type:
            case "error":
                self.colour = discord.Color.red()
            case "success":
                self.colour = discord.Color.green()
            case "info":
                self.colour = discord.Color.blue()
            case _:
                self.colour = discord.Color.default()
