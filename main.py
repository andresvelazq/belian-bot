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
async def create_character(interaction: discord.Interaction, name: str, str: str, dex: str, con: str, int: str, wis: str, cha: str):
    """Adds a unique character using a slash command"""
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
        name="updatesaves",
        description="Update saving throws from the default value",
        guilds=[discord.Object(id=settings.BOT_TESTER)]
)
async def update_saves(interaction: discord.Interaction, name: str, str: str, dex: str, con: str, int: str, wis: str, cha: str):
    """Updates the saving throw values in the character's information"""
    saves = [str, dex, con, int, wis, cha]
    if not verify.verifyStats(saves):
        await interaction.response.send_message("Those aren't even numbers...")
        return
    else:
        if format.updateSaves(name, saves, interaction.guild.name):
            await interaction.response.send_message(f"{name}'s saves have been updated")
        else:
            await interaction.response.send_message(f"Please create {name} first.")


@tree.command(
    name="updatestats",
    description="Update stats of a character",
    guilds=[discord.Object(id=settings.BOT_TESTER)]
)
async def update_stats(interaction: discord.Interaction, name: str, str: str, dex: str, con: str, int: str, wis: str, cha: str):
    """Updates a character's stats"""
    stats = [str, dex, con, int, wis, cha]
    if not verify.verifyStats(stats):
        await interaction.response.send_message("Those aren't even numbers...")
        return
    else:
        if format.updateStats(name, stats, interaction.guild.name):
            await interaction.response.send_message(f"{name}'s stats have been updated")
        else:
            await interaction.response.send_message(f"Please create {name} first.")

@tree.command(
    name="test",
    description="Just a little test to make sure things are ok",
    guilds=[discord.Object(id=settings.BOT_TESTER)]
)
async def test(interaction: discord.Interaction):
    """Placeholder command to test functionality before implementing"""
    print("Received.")
    await interaction.response.send_message('Active.')


client.run(settings.DISCORD_TOKEN)
