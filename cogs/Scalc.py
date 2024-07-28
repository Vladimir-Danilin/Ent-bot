import disnake
from disnake.ext import commands
import math


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Калькулятор")
    async def calc(self, ctx):
        await ctx.send("Калькулятор")

    @commands.slash_command(description="Калькулятор")
    async def calc(self, interaction, first: str, operator: str, second: str):
        embed = disnake.Embed(title='Калькулятор', color=0xFFFFFF)
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        if first == "e" or first == "е":
            first = math.e
        elif second == "e" or second == "е":
            second = math.e
        elif first == "pi" or first == "пи":
            first = math.pi
        elif second == "pi" or second == "пи":
            second = math.pi

        first = float(first)
        second = float(second)

        match operator:
            case "+":
                result = first + second
                embed.description = f'Ответ {result}'
                await interaction.response.send_message(embed=embed, ephemeral=True)
            case "-":
                result = first - second
                embed.description = f'Ответ {result}'
                await interaction.response.send_message(embed=embed, ephemeral=True)
            case "*":
                result = first * second
                embed.description = f'Ответ {result}'
                await interaction.response.send_message(embed=embed, ephemeral=True)
            case "/":
                result = first / second
                embed.description = f'Ответ {result}'
                await interaction.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Calculator(bot=bot))
