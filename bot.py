from typing import Optional
import disnake
from disnake.ext import commands
from config import TOKEN
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), help_command=None, intents=disnake.Intents.all(), test_guilds=[1099396890648395980])


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    ctx.send(f"Файл {extension} загружен")


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    ctx.send(f"Файл {extension} отгружен")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    ctx.send(f"Файл {extension} перезагружен")


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f'бот {bot.user} начал работу!')


class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10.0)
        self.value = Optional[bool]

    @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green)
    async def confirm(self,  button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message("Отлично")
        self.value = True
        self.stop()

    @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.red)
    async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message("Не отлично")
        self.value = False
        self.stop()


class LinkToParty(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(disnake.ui.Button(label="Присоеденяйся", url="https://youtube.com/"))


@bot.command(name="Пати", aliases=["party", "Party", "пати", "ПАТИ", "PARTY"])
async def ask_party(ctx):
    view = Confirm()

    await ctx.send("Приглашение", view=view)
    await view.wait()

    if view.value is None:
        await ctx.send("Ошибка")
    elif view.value:
        await ctx.send("Принято", view=LinkToParty())
    else:
        await ctx.send("Отклонено")


if __name__ == "__main__":
    bot.run(TOKEN)
