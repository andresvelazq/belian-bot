import traceback
import typing
import discord
import character_update
import verify
from discord import app_commands


class StrModal(discord.ui.Modal, title="Athletics"):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    athletics = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Athletics",
        required=True,
        max_length=2,
        placeholder="0"
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        self.athletics = str(self.athletics)
        if not verify.verifyStats(self.athletics):
            await interaction.response.send_message("Those aren't even numbers...")
        else:
            outcome = character_update.athletics(self.name, self.athletics, interaction.guild.name, interaction.user.id)
            if outcome == 1:
                await interaction.response.send_message("Athletics updated.")
            elif outcome == 0:
                await interaction.response.send_message(f"Please create {self.name} first")
            else:
                await interaction.response.send_message(f"{self.name} does not belong to you.")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        traceback.print_tb(error.__traceback__)

class DexModal(discord.ui.Modal, title="Dexterity Skills"):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    acrobatics = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Acrobatics",
        required=True,
        max_length=2,
        placeholder="0"
    )

    sleight = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Sleight of Hand",
        required=True,
        max_length=2,
        placeholder="0"
    )

    stealth = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Stealth",
        required=True,
        max_length=2,
        placeholder="0"
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        dex_skills = [str(self.acrobatics), str(self.sleight), str(self.stealth)]
        if not verify.verifyStats(dex_skills):
            await interaction.response.send_message("Those aren't even numbers...")
        else:
            outcome =character_update.dexs_update(self.name, dex_skills, interaction.guild.name, interaction.user.id)
            if outcome == 1:
                await interaction.response.send_message("Dexterity skills updated.")
            elif outcome == 0:
                await interaction.response.send_message(f"Please create {self.name} first")
            else:
                await interaction.response.send_message(f"{self.name} does not belong to you.")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        traceback.print_tb(error.__traceback__)

class IntModal(discord.ui.Modal, title="Intelligence Skills"):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    arcana = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Arcana",
        required=True,
        max_length=2,
        placeholder="0"
    )

    history = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="History",
        required=True,
        max_length=2,
        placeholder="0"
    )

    investigation = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Investigation",
        required=True,
        max_length=2,
        placeholder="0"
    )

    nature = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Nature",
        required=True,
        max_length=2,
        placeholder="0"
    )

    religion = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Religion",
        required=True,
        max_length=2,
        placeholder="0"
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        int_skills = [str(self.arcana), str(self.history), str(self.investigation), str(self.nature), str(self.religion)]
        if not verify.verifyStats(int_skills):
            await interaction.response.send_message("Those aren't even numbers...")
        else:
            outcome = character_update.ints_update(self.name, int_skills, interaction.guild.name, interaction.user.id)
            if outcome == 1:
                await interaction.response.send_message("Intelligence skills updated.")
            elif outcome == 0:
                await interaction.response.send_message(f"Please create {self.name} first")
            else:
                await interaction.response.send_message(f"{self.name} does not belong to you.")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        traceback.print_tb(error.__traceback__)

class WisModal(discord.ui.Modal, title="Wisdom Skills"):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    animal = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Animal Handling",
        required=True,
        max_length=2,
        placeholder="0"
    )

    insight = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Insight",
        required=True,
        max_length=2,
        placeholder="0"
    )

    medicine = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Medicine",
        required=True,
        max_length=2,
        placeholder="0"
    )

    perception = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Perception",
        required=True,
        max_length=2,
        placeholder="0"
    )

    survival = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Survival",
        required=True,
        max_length=2,
        placeholder="0"
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        wis_skills = [str(self.animal), str(self.insight), str(self.medicine), str(self.perception), str(self.survival)]
        if not verify.verifyStats(wis_skills):
            await interaction.response.send_message("Those aren't even numbers...")
        else:
            outcome = character_update.wiss_update(self.name, wis_skills, interaction.guild.name, interaction.user.id)
            if outcome == 1:
                await interaction.response.send_message("Wisdom skills updated.")
            elif outcome == 0:
                await interaction.response.send_message(f"Please create {self.name} first")
            else:
                await interaction.response.send_message(f"{self.name} does not belong to you.")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        traceback.print_tb(error.__traceback__)

class ChaModal(discord.ui.Modal, title="Charisma Skills"):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    deception = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Deception",
        required=True,
        max_length=2,
        placeholder="0"
    )

    intimidation = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Intimidation",
        required=True,
        max_length=2,
        placeholder="0"
    )

    performance = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Performance",
        required=True,
        max_length=2,
        placeholder="0"
    )

    persuasion = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Persuasion",
        required=True,
        max_length=2,
        placeholder="0"
    )

    async def on_submit(self, interaction: discord.Interaction) -> None:
        cha_skills = [str(self.deception), str(self.intimidation), str(self.performance), str(self.persuasion)]
        if not verify.verifyStats(cha_skills):
            await interaction.response.send_message("Those aren't even numbers...")
        else:
            outcome = character_update.chas_update(self.name, cha_skills, interaction.guild.name, interaction.user.id)
            if outcome == 1:
                await interaction.response.send_message("Charisma skills updated.")
            elif outcome == 0:
                await interaction.response.send_message(f"Please create {self.name} first")
            else:
                await interaction.response.send_message(f"{self.name} does not belong to you.")

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        traceback.print_tb(error.__traceback__)

@app_commands.command(
        name="updateskill",
        description="Update skill bonuses by related stat"
)
async def update_skills(interaction: discord.Interaction, name:str,
                         choice: typing.Literal['strength', 'dexterity', 'intelligence', 'wisdom', 'charisma']) -> None:
    """Create modal to input any skill modifiers by related stat"""
    match choice:
        case 'strength':
            modal = StrModal(name)
            modal.user = interaction.user
            await interaction.response.send_modal(modal)
        case 'dexterity':
            modal = DexModal(name)
            modal.user = interaction.user
            await interaction.response.send_modal(modal)
        case 'intelligence':
            modal = IntModal(name)
            modal.user = interaction.user
            await interaction.response.send_modal(modal)
        case 'wisdom':
            modal = WisModal(name)
            modal.user = interaction.user
            await interaction.response.send_modal(modal)
        case 'charisma':
            modal = ChaModal(name)
            modal.user = interaction.user
            await interaction.response.send_modal(modal)
        case _:
            await interaction.response.send_message("...How?")


async def setup(bot):
    bot.tree.add_command(update_skills)
