import discord
# import os
# import requests
import random
from settings import TOKEN # bikin file "settings.py" terus taro token bot di situ
from discord.ext import commands

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default() 
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

# bikin command bot yang bisa memberikan langkah-langkah mudah untuk mengurangi sampah
# bikin command yang memberikan info kenapa harus mengurangi polusi

@bot.command()
async def langkah(ctx):

    choice_list = ["Kurangi Penggunaan Bahan yang Sulit Terurai.",
                   "Menggunakan Kendaraan Ramah Lingkungan.",
                   "Mengurangi Pemakaian Kendaraan Bermotor.",
                   "Kurangi Merokok.",
                   "Jangan Membakar Sampah.",
                   "Menggunakan Produk Ramah Lingkungan.",
                   "Menanam Pohon.",
                   "Tidak Membakar Hutan."]
    
    random_choice = choice_list[random.randint(0,7)]
    await ctx.send("Hari ini, coba untuk melakukan hal ini: " + random_choice)

@bot.command()
async def info(ctx):
    await ctx.send("Polusi berbahaya karena bisa berdampak buruk terhadap lingkungan, jadi kita harus coba untuk menguranginya.")

bot.run(TOKEN)