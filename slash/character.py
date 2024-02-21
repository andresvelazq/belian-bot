import discord
import character_update
from discord import app_commands


@app_commands.command(
    name="add",
    description="Add your character"
)
async def create_character(interaction: discord.Interaction, name: str,
                           str: int, dex: int, con: int,
                           int: int, wis: int, cha: int):
    """Adds a unique character using a slash command"""
    stats = [str, dex, con, int, wis, cha]

    if character_update.addCharacter(name, stats, interaction.guild.name, interaction.user.id):
        await interaction.response.send_message(f"{name} created.")
    else:
        await interaction.response.send_message(f"Nice try, {name} already exists.")


@app_commands.command(
        name="saves",
        description="Update saving throws from the default value"
)
async def update_saves(interaction: discord.Interaction, name: str,
                       str: int, dex: int, con: int,
                       int: int, wis: int, cha: int):
    """Updates the saving throw values in the character's information"""
    saves = [str, dex, con, int, wis, cha]

    outcome = character_update.updateSaves(name, saves, interaction.guild.name, interaction.user.id)
    if outcome == 1:
        await interaction.response.send_message(f"{name}'s saves have been updated")
    elif outcome == 0:
        await interaction.response.send_message(f"Please create {name} first.")
    else:
        await interaction.response.send_message(f"{name} does not belong to you.")


@app_commands.command(
    name="stats",
    description="Update stats of a character"
)
async def update_stats(interaction: discord.Interaction, name: str,
                       str: int, dex: int, con: int,
                       int: int, wis: int, cha: int):
    """Updates a character's stats"""
    stats = [str, dex, con, int, wis, cha]

    outcome = character_update.updateStats(name, stats, interaction.guild.name, interaction.user.id)
    if outcome == 1:
        await interaction.response.send_message(f"{name}'s stats have been updated")
    elif outcome == 0:
        await interaction.response.send_message(f"Please create {name} first.")
    else:
        await interaction.response.send_message(f"{name} does not belong to you.")


@app_commands.command(
        name="hp",
        description="Set the HP stat of a character"
)
async def update_hp(interaction: discord.Interaction, name: str, hp: int):
    """Updates the max HP stat"""
    outcome = character_update.update_HP(name, hp, interaction.guild.name, interaction.user.id)
    if outcome == 1:
        await interaction.response.send_message(f"{name}'s max HP has been set.")
    elif outcome == 0:
        await interaction.response.send_message(f"Please create {name} first.")
    else:
        await interaction.response.send_message(f"{name} does not belong to you.")


@app_commands.command(
        name="damage",
        description="Deals damage to the character's HP"
)
async def damage(interaction: discord.Interaction, name: str, damage: int):
    """Reduces a character's current HP and notifies if they died"""
    (exists, alive) = character_update.damage(name, damage, interaction.guild.name, interaction.user.id)
    if exists == 1:
        if alive <= 0:
            await interaction.response.send_message(f"{name} has taken {damage} damage and died. :skull:")
        else:
            await interaction.response.send_message(f"{name} has taken {damage} damage.")
    elif exists == 0:
        await interaction.response.send_message(f"Please create {name} first.")
    else:
        await interaction.response.send_message(f"{name} does not belong to you.")


@app_commands.command(
        name="heal",
        description="Heals the character's HP"
)
async def heal(interaction: discord.Interaction, name: str, heal: int):
    """Heals a character to a maximum of their max HP"""
    if character_update.heal(name, heal, interaction.guild.name):
        await interaction.response.send_message(f"{name} has healed ||redacted|| health.")
    else:
        await interaction.response.send_message(f"Please create {name} first.")


async def setup(bot):
    bot.tree.add_command(create_character)
    bot.tree.add_command(update_saves)
    bot.tree.add_command(update_stats)
    bot.tree.add_command(update_hp)
    bot.tree.add_command(damage)
    bot.tree.add_command(heal)
