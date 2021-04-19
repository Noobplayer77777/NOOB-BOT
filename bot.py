import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")


f = open("rules.txt","r")
rules = f.readlines()

filtered_words = ["fuck","nigger","gay","cunt","boob","motherfucker","mf","ass"]



@client.event
async def on_message(msg):
	for word in filtered_words:
		if word in msg.content:
			await msg.delete()

	await client.process_commands(msg)

@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send("You don't have permission to use this command >:l")
		await ctx.message.delete()
	elif isinstance(error,commands.MissingRequiredArgument):
		await ctx.send("Please enter all the required arguments")
		await ctx.message.delete()
	else:
		raise error	

@client.event
async def on_ready():
	print("Bot is ready")

@client.command()
async def hello(ctx):
	await ctx.send("*Hello*")

@client.command()
async def !invite(ctx):
	await ctx.send("https://discord.com/api/oauth2/authorize?client_id=832997483369332767&permissions=0&scope=bot")

@client.command(aliases=['rules'])
async def rule(ctx,*,number):
	await ctx.send(rules[int(number)-1])

@client.command(aliases=['c'])	
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=10):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])	
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send(member.name+"been kicked from the server, Because"+reason)
	await member.send("You have been kicked from the server, Because"+reason)
	await member.kick(reason=reason)

@client.command(aliases=['b'])	
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send(member.name+"been banned from the server, Because"+reason)
	await member.ban(reason=reason)

@client.command(aliases=['m'])	
@commands.has_permissions(kick_members = True)
async def mute(ctx,member : discord.Member):
	muted_role = ctx.guild.get.role(833341618009407488)

	await member.add_roles(muted_role)
	await ctx.send(member.mention + "has been muted")

@client.command(aliases=['um'])	
@commands.has_permissions(kick_members = True)
async def unmute(ctx,member : discord.Member):
	muted_role = ctx.guild.get.role(833341618009407488)

	await member.remove_roles(muted_role)
	await ctx.send(member.mention + "has been unmuted")

@client.command(aliases=['user','info'])	
@commands.has_permissions(kick_members = True)
async def whois(ctx,member : discord.Member):
	embed = discord.Embed(title = member.name , description = member.mention , color = discord.Color.green())
	embed.add_field(name = "ID", value = member.id , inline = True)
	embed.set_thumbnail(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(aliases=['ub'])	
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')

	for banned_entry in banned_users:
		user = banned_entry.user

		if(user.name, user.discriminator)==(member_name,member_disc):
			await ctx.guild.unban(user)
			await ctx.send(member_name +" has been unbanned!")
			return

client.run("ODMyOTk3NDgzMzY5MzMyNzY3.YHr7XA.n7x99yepzFEzZlILHudXp8d-aGc")	