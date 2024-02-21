import discord
import character_update
import get_character
import roll
from discord import app_commands


@app_commands.command(
    name="addatk",
    description="Add an attack to a specified character"
)
@app_commands.rename(damage_numdice="damage", damage_dice="d", damage_plus="+")
async def add_attack(interaction: discord.Interaction, name: str, attack: str,
                     hit: int, damage_numdice: int, damage_dice: int,
                     damage_plus: int):
    """Adds an attack and it's roll information to a character"""
    attack_info = [hit, damage_numdice, damage_dice, damage_plus]
    outcome = character_update.update_attack(name, attack, attack_info, interaction.guild.name)
    if outcome == 1:
        await interaction.response.send_message(f"{name}'s attacks have been updated.")
    elif outcome == 0:
        await interaction.response.send_message(f"Please create {name} first.")
    else:
        await interaction.response.send_message(f"{name} does not belong to you.")


@app_commands.command(
        name="attack",
        description="Use a character's attack"
)
async def get_attack(interaction: discord.Interaction, name: str, attack: str):
    """Roll a character's attack dice"""
    try:
        yesno = [':white_check_mark:',':x:']
        attack_info = get_character.attack(name, attack, interaction.guild.name) 
        hit = roll.oned20mod(20, attack_info["hit mod"])
        if hit == 100:
            # TODO: damage calculation 
            await interaction.response.send_message(f'**CRIT!!!**')
        if hit == -100:
            await interaction.response.send_message(f'**CRIT MISS...***')
        else:
            message = await interaction.response.send_message(f'Does a {hit} hit?')
            
            for react in yesno:
                await message.add_reaction(react)
            
            # TODO: damage calculation on hit
            # remove reactions

        
    except Exception as err:
        await interaction.response.send_message('Something went wrong.')
        print(f'Error: {err}')
    

async def setup(bot):
    bot.tree.add_command(add_attack)
