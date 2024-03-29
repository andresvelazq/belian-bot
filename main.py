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

    for guild in settings.GUILDS:
        bot.tree.copy_global_to(guild=discord.Object(id=guild))
        await bot.tree.sync(guild=discord.Object(id=guild))
    print(f'I have logged into {servers}.')


@bot.tree.command(
    name="roll",
    description="Roll some dice",
)
@app_commands.rename(num_dice="number_of_dice")
async def test(interaction: discord.Interaction, num_dice: int, d: int):
    """Roll a custom number of dice"""
    if num_dice > 0 and d > 0:
        rolls = roll.xdy(num_dice, d)
        await interaction.response.send_message(f'{num_dice}d{d} : {rolls}')
    else:
        await interaction.response.send_message("Why are you like this?")


bot.run(settings.DISCORD_TOKEN)
