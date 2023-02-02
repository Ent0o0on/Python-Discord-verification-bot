import discord
from discord.ext import commands
import discord.ui
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

@bot.event
async def on_ready():
  print('System rebooted.')
  bot.add_view(Verification())

class Verification(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label="✅",custom_id = "Verify",style = discord.ButtonStyle.success)
  async def verify(self, button, interaction):
    role = 1066356340789870707
    user = interaction.user
    if not any(role == _role .id for _role in user.roles):
      await user.add_roles(user.guild.get_role(role))
      await user.send("🇬🇧 You have been verified!\n🇩🇪 Du wurdest verifiziert!")

@bot.command()
async def verify(ctx):
  embed = discord.Embed(title = "Verification", description = "Click below to get verified!\nKlicken unten, um dich verifizieren zu lassen! ")
  await ctx.send(embed = embed, view = Verification())

#You need to paste your Token into the .env file
bot.run(os.environ.get("TOKEN"))