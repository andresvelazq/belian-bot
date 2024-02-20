import discord
import typing
import get_character
import roll
from discord import app_commands


@app_commands.command(
        name="save",
        description="Roll a saving throw for a character"
)
async def roll_save(interaction: discord.Interaction, name: str,
                    choice: typing.Literal['strength', 'dexterity', 'constitution',
                                           'intelligence', 'wisdom', 'charisma']) -> None:
    """Rolls the saving throw for the specified stat"""
    try:
        modifier = get_character.saving_throw(name, choice, interaction.guild.name)
        result = roll.onedymod(20, modifier)
        if result == 20:
            await interaction.response.send_message(f':white_check_mark: {name} crit their {choice} save!')
        elif result == 1:
            await interaction.response.send_message(f':x: {name} crit failed their {choice} save!')
        else:
            await interaction.response.send_message(f'{name} rolled a {choice} save of {result}')
    except Exception as err:
        await interaction.response.send_message('Something went wrong.')
        print(f'Error: {err}')


async def setup(bot):
    bot.tree.add_command(roll_save)