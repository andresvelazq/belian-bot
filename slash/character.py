import discord
import character_info
import settings
import verify
from discord import app_commands


@app_commands.command(
    name="add",
    description="Add your character"
)
async def create_character(interaction: discord.Interaction, name: str,
                           str: str, dex: str, con: str,
                           int: str, wis: str, cha: str):
    """Adds a unique character using a slash command"""
    stats = [str, dex, con, int, wis, cha]
    if not verify.verifyStats(stats):
        await interaction.response.send_message(f"Those aren't even numbers...")
    else:
        if character_info.addCharacter(name, stats, interaction.guild.name):
            await interaction.response.send_message(f"{name} created.")
        else:
            await interaction.response.send_message(f"Nice try, {name} already exists.")


@app_commands.command(
        name="saves",
        description="Update saving throws from the default value"
)
async def update_saves(interaction: discord.Interaction, name: str,
                       str: str, dex: str, con: str,
                       int: str, wis: str, cha: str):
    """Updates the saving throw values in the character's information"""
    saves = [str, dex, con, int, wis, cha]
    if not verify.verifyStats(saves):
        await interaction.response.send_message("Those aren't even numbers...")
    else:
        if character_info.updateSaves(name, saves, interaction.guild.name):
            await interaction.response.send_message(f"{name}'s saves have been updated")
        else:
            await interaction.response.send_message(f"Please create {name} first.")


@app_commands.command(
    name="stats",
    description="Update stats of a character"
)
async def update_stats(interaction: discord.Interaction, name: str,
                       str: str, dex: str, con: str,
                       int: str, wis: str, cha: str):
    """Updates a character's stats"""
    stats = [str, dex, con, int, wis, cha]
    if not verify.verifyStats(stats):
        await interaction.response.send_message("Those aren't even numbers...")
    else:
        if character_info.updateStats(name, stats, interaction.guild.name):
            await interaction.response.send_message(f"{name}'s stats have been updated")
        else:
            await interaction.response.send_message(f"Please create {name} first.")


async def setup(bot):
    bot.tree.add_command(create_character)
    bot.tree.add_command(update_saves)
    bot.tree.add_command(update_stats)