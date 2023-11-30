#Importing discord class library to connect discord API
#Import the OS python module
#importing the random module
#Importing the ec2_metadata from AWS

import discord
import os 
import random 
from ec2_metadata import ec2_metadata

#Retrieving ec2_metadata specified region & instance ID, printing the region and instance ID

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

#establishing client as the discord bot with Discord Library
#defining the token by retrieving the 'TOKEN' string from the OS with getenv

client = discord.Bot() 
token = str(os.getenv('TOKEN')) 

#The client (bot) uses the on ready event provided by Discord API, once API client Initialized it will trigger the operation (Printing then name of our bot)

@client.event 
async def on_ready(): 
	print("Logged in as a bot {0.user}".format(client))

#async def on_message event taking details about the message: username, channel, message

@client.event 
async def on_message(message): 
	username = str(message.author).split("#")[0] 
	channel = str(message.channel.name) 
	user_message = str(message.content) 

	#Prints logs of message by user and on the channel

	print(f'Message {user_message} by {username} on {channel}') 

	#Checks If the message is sent by the bot by looking at the message author, if its client (bot) then return and don't reply

	if message.author == client.user: 
		return

#if statement (channel) put in the "random" discord channel then runs another if statement
#the other if statement: if the user message is hello then in the channel send string containing username and ec2 data (region)

	if channel == "random": 
		if user_message.lower() == "hello" or user_message.lower() == "hi": 
			await message.channel.send(f"Sooner! {username} Your EC2 Data: {ec2_metadata.region}")
			return

		#EC2 Data message request from user and response to it concatenation string

		elif user_message.lower() == "EC2 Data":
			await message.channel.send("Your instance data is" + ec2_metadata.region)

#Running Client with defined 'token' from the linux OS in AWS
client.run(token)
