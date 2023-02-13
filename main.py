import disnake #библеотека

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all()) #префикс


@bot.slash_command()#команда
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("тест")

bot.run("токен бота") #token
