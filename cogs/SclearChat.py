import disnake
from disnake.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Клининг", aliases=["Очистки", "Варианты Отчисток"])
    async def cleaning(self, ctx):
        await ctx.send("Клининг")

    @commands.slash_command(description="Команда для отчистки чата")
    async def clear(self, interaction, amount: int):
        embed = disnake.Embed(title='Очистка чата', description=f'Удалено {amount} сообщений', color=0xffffff)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Clear(bot=bot))
