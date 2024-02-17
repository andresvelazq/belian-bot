import discord
import json
import traceback
from discord import app_commands

import format
import settings
import verify


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    servers = ""
    for guild in client.guilds:
        servers += '' if not servers else  ', '
        servers += guild.name

    await tree.sync(guild=discord.Object(id=settings.BOT_TESTER))
    print(f'I have logged into {servers}.')


@tree.command(
    name="character",
    description="Add your character",
    guilds=[discord.Object(id=settings.BOT_TESTER)]
)
async def create_character(interaction, name: str, str: str, dex: str, con: str, int: str, wis: str, cha: str):
    stats = [str, dex, con, int, wis, cha]
    if not verify.verifyStats(stats):
        await interaction.response.send_message(f"Invalid stats, everyone point and laugh at <@{interaction.user.id}>.")
        return
    else:
        if format.addCharacter(name, stats, interaction.guild.name):
            await interaction.response.send_message(f"{name} created.")
        else:
            await interaction.response.send_message(f"Nice try, {name} already exists.")


@tree.command(
    name="test",
    description="Just a little test to make sure things are ok",
    guilds=[discord.Object(id=settings.BOT_TESTER)]
)
async def test(interaction):
    
    print("Yes, that worked.")


client.run(settings.DISCORD_TOKEN)
