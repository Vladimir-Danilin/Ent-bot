import disnake
from config import *
from disnake.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = disnake.utils.get(member.guild.roles, id=1099592952499687475)
        channel = member.guild.system_channel

        embed = disnake.Embed(title='Новый участник', description=f'{member.name}', color=0xffffff)

        await member.add_roles(role)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot=bot))
