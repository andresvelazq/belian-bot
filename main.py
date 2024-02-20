import glob
import roll
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

    for slash_name in glob.glob("slash\\*.py"):
        if slash_name != "__init__.py":
            await bot.load_extension(slash_name[:-3].replace('\\', '.'))

    bot.tree.copy_global_to(guild=discord.Object(id=settings.BOT_TESTER))
    await bot.tree.sync(guild=discord.Object(id=settings.BOT_TESTER))
    print(f'I have logged into {servers}.')


@bot.tree.command(
    name="roll",
    description="Roll some dice",
)
async def test(interaction: discord.Interaction, num_dice: str, d: str):
    """Roll a custom number of dice"""
    if num_dice.isnumeric() and d.isnumeric():
        rolls = roll.xdy(int(num_dice), int(d))
        await interaction.response.send_message(rolls)
    else:
        await interaction.response.send_message("Why are you like this?")


bot.run(settings.DISCORD_TOKEN)
