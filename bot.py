import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = 951556935088480326  # замени на ID своего сервера

class PartyModal(discord.ui.Modal, title="Сбор Mythic +"):

    key_level = discord.ui.TextInput(label="Уровень ключа (1-20)", placeholder="Например, 10", max_length=2)
    dungeon = discord.ui.TextInput(label="Название подземелья", placeholder="Например, Театр Боли")
    roles_needed = discord.ui.TextInput(label="Нужные роли (через запятую)", placeholder="танк, хил, ДД")

    async def on_submit(self, interaction: discord.Interaction):
        author = interaction.user.display_name
        embed = discord.Embed(
            title=f"Сбор Mythic +{self.key_level.value}",
            description=f"**Подземелье:** {self.dungeon.value}\n"
                        f"**Нужны роли:** {self.roles_needed.value}\n"
                        f"**Собирает:** {author}",
            color=discord.Color.green()
        )
        await interaction.response.send_message("Объявление отправлено в канал!", ephemeral=True)

        # Отправить сообщение в конкретный канал (замени CHANNEL_ID)
        channel = bot.get_channel(1372918127209222197)  # замени на ID нужного канала
        await channel.send(embed=embed)

@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Синхронизировано {len(synced)} команд.")
    except Exception as e:
        print(e)

@bot.tree.command(name="пати", description="Собрать пати Mythic +", guild=discord.Object(id=GUILD_ID))
async def party(interaction: discord.Interaction):
    await interaction.response.send_modal(PartyModal())

bot.run("MTM3Mjk4MTQxODg5MTgwODkzMA.GsA__K.XMczg32-hnm_ETIckV75TA9wwXu0pqlAz3MLlw")
