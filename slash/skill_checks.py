import discord
import typing
import get_character
import roll
from discord import app_commands


@app_commands.command(
        name="skillcheck",
        description="Roll a skill check for a character"
)
async def skill_check(interaction: discord.Interaction, name: str,
                    skill: typing.Literal['acrobatics', 'animal handling', 'arcana',
                                           'athletics', 'deception', 'history',
                                           'insight', 'intimidation', 'investigation',
                                           'medicine', 'nature', 'perception',
                                           'performance', 'persuasion', 'religion',
                                           'sleight of hand', 'stealth', 'survival']) -> None:
    """Rolls the saving throw for the specified stat"""
    try:
        modifier = get_character.skill_mod(name, skill, interaction.guild.name)
        result = roll.oned20mod(modifier)
        if result == 100:
            await interaction.response.send_message(f':white_check_mark: {name} crit their {skill} check!')
        elif result == -100:
            await interaction.response.send_message(f':x: {name} crit failed their {skill} check!')
        else:
            await interaction.response.send_message(f'{name} rolled a {result} for {skill} check.')
    except Exception as err:
        await interaction.response.send_message('Something went wrong.')
        print(f'Error: {err}')


async def setup(bot):
    bot.tree.add_command(skill_check)