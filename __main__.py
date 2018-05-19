# -*- coding: utf-8 -*-
"""Tatsumaki Farm

Bot used to "farm exp" and "farm credits" in `Tatsumaki` Bot.
Written in `discord.py`."""

__author__ = "kubinka0505"
__date__ = "18.05.2018"
__version__ = "1.0"

#---#

import discord
from discord.ext.commands import Bot

from asyncio import sleep
from json import load
from os.path import dirname
from random import randint
from re import findall

#-----#

Bot = Bot(command_prefix=">")
Bot.remove_command("help")

#-----#

Channel = load(open(r"{0}\config.json".format(dirname(__file__))))["ChannelID"]
User = load(open(r"{0}\config.json".format(dirname(__file__))))["UserID"]

#-----#

@Bot.event
async def on_ready():
	print("{0}\n<< Ready >>\n{0}\nLogged in as: {1}\nID: {2}\n{0}".format("-"*5, str(Bot.user.name).encode(), str(Bot.user.id)))
	
	# - Daily Credits - #
	
	a = await Bot.send_message(Bot.get_channel(Channel), "t!daily {0}".format(User))
	await sleep(int(randint(10, 15))) # "Undetectable System", probably not working on 100%
	print("Sent `Daily Credits` message...")
	
	# - Reputation Points - #
	b = await Bot.send_message(Bot.get_channel(Channel), "t!rep {0}".format(User))
	print("Sent `Reputation Points` message...")

	# - Multi-Accounts Message Handling - #
	print("{0}\n`Delete Message Section`\n{0}".format("-"*22))
	await Bot.delete_message(a)
	print("Deleted `Daily Credits` check message...")
	await sleep(0.25)
	await Bot.delete_message(b)
	print("Deleted `Reputation Points` message...")
	print("Done!")
	return await Bot.close()