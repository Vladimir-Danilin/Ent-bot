import re
from disnake.ext import commands

censored = open(file="bad_word.txt", mode="r", encoding="utf-8")
second = [line.rstrip() for line in censored]
censored.close()


class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.bot.process_commands(message)
        for content in re.split('[ ,_.-]', message.content):
            for block_word in second:
                if content.lower() == block_word:
                    if message.author.bot:
                        return 0
                    else:
                        await message.delete()
                        await message.channel.send(f"{message.author.mention}~вот так не надо")
                        return 0


def setup(bot):
    bot.add_cog(Filter(bot=bot))
