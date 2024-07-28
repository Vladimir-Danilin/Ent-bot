import disnake
from disnake.ext import commands


class CMDAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Админы", aliases=["Админ", "админ", "админы", "admin"])
    async def admins(self, ctx):
        await ctx.send("Админы")

    @commands.command(name='кик', aliases=['кикнуть', 'выкинуть', 'отстранить'])
    @commands.has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member: disnake.Member, *, reason=None):
        if reason is None:
            await ctx.send(f"Админ {ctx.author.mention} не указал причину", delete_after=60)
        else:
            await ctx.send(f"Админ {ctx.author.mention}, забанил {member.mention} по причине \"{reason}\"", delete_after=60)

        await member.kick(reason=reason)
        await ctx.message.delete(delay=60)


def setup(bot):
    bot.add_cog(CMDAdmin(bot=bot))
