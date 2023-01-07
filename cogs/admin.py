from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import discord
from discord import Interaction, app_commands, ui
from discord.ext import commands

if TYPE_CHECKING:
    from bot import ValorantBot


class Admin(commands.Cog):
    """Error handler"""

    def __init__(self, bot: ValorantBot) -> None:
        self.bot: ValorantBot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, sync_type: Literal['guild', 'global']) -> None:
        """Sync the application commands"""

        async with ctx.typing():
            if sync_type == 'guild':
                self.bot.tree.copy_global_to(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced guild !")
                return

            await self.bot.tree.sync()
            await ctx.reply(f"Synced global !")

    @commands.command()
    @commands.is_owner()
    async def unsync(self, ctx: commands.Context, unsync_type: Literal['guild', 'global']) -> None:
        """Unsync the application commands"""

        async with ctx.typing():
            if unsync_type == 'guild':
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Un-Synced guild !")
                return

            self.bot.tree.clear_commands()
            await self.bot.tree.sync()
            await ctx.reply(f"Un-Synced global !")

    @app_commands.command(description='Shows basic information about the bot.')
    async def about(self, interaction: Interaction) -> None:
        """Shows basic information about the bot."""

        owner_url = f'https://discord.com/users/391531631925526528'
        github_project = 'https://github.com/staciax/Valorant-DiscordBot'
        support_url = 'https://discord.gg/hFDbWUrW'

        embed = discord.Embed(color=0xFFFFFF)
        embed.set_author(name='VALORANT BOT PROJECT')
        embed.set_thumbnail(url='https://i.imgur.com/M93U4m6.jpg')
        embed.add_field(name='DEV:', value=f"[Threo#0515]({owner_url})", inline=False)
        view = ui.View()

        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: ValorantBot) -> None:
    await bot.add_cog(Admin(bot))
