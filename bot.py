import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=1,name="with AtanuAD"))
    print('Online')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mass(ctx,*,msg):

    for member in ctx.guild.members:
        try:
            await member.send(msg)
            await ctx.message.channel.send(f"DM sent to {member.name}#{member.discriminator} ✅ ")
        except:
            await ctx.message.channel.send(f'''DM Not sent to {member.name}#{member.discriminator} ❌ ''')

    await ctx.message.channel.send("DM sent to all ✅ ")

bot.run('NjE2Mjk5NDcxMzc4MTg2MjU2.XWzD6A.khxpIACfSDtUzvVJcdGNxzVXeAE')
