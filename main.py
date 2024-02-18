import discord
from discord.ext import commands
from discord import app_commands

import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)


@bot.event
async def on_ready():
    servers = ""
    for guild in bot.guilds:
        servers += '' if not servers else  ', '
        servers += guild.name

    await bot.load_extension('slash.character')
    bot.tree.copy_global_to(guild=discord.Object(id=settings.BOT_TESTER))
    await bot.tree.sync(guild=discord.Object(id=settings.BOT_TESTER))
    print(f'I have logged into {servers}.')


@bot.tree.command(
    name="test",
    description="Just a little test to make sure things are ok",
)
async def test(interaction: discord.Interaction):
    """Placeholder command to test functionality before implementing"""
    print("Received.")
    await interaction.response.send_message('Active.')


bot.run(settings.DISCORD_TOKEN)
