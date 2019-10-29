'''
Slack bot for pinging Spencer Mycek

-t
-time
number of seconds between pings. not fractional. default 3600 (1 hour)

-m
-message
custom message to be displayed. default " Bring me the fucking toga"

-c
-channel
-slackchannel
custom slack channel. default #general

-n
-name
-username
custom user to ping in the form of their member ID. default Spencer's id
'''

import os
import slack
import time
import sys

slack_token = os.environ.get('SLACK_BOT_TOKEN')
client = slack.WebClient(token=slack_token)


def main():
	args = parseargs()
	print(args)
	pingloop(args[0],args[1],args[2],args[3])

def parseargs():
	'''
	find arguments for pingloop
	:return: array with 4 arguments
	'''
	usertag = None
	message = None
	slackchannel = None
	seconds = None
	for i in range (1, len(sys.argv)-1):
		arg = sys.argv[i]
		val = sys.argv[i+1]
		if arg == "-n" or arg == "-name" or arg == "-username":
			usertag = val
			print("set usertag to "+val)
		if arg == "-m" or arg == "-message":
			message = val
			print("set message to "+val)
		if arg == "-c" or arg == "-channel" or arg == "-slackchannel":
			slackchannel = val
			print("set slackchannel to "+val)
		if arg == "-t" or arg == "-time" or arg == "-seconds":
			seconds = str(val)
			print("set time to "+val)
	return [usertag, message, slackchannel, seconds]

def pingloop(usertag, message, slackchannel, seconds):
	'''
	repeatedly ping someone with a custom message in a custom channel every custom number of seconds, mxmeinhold!
	:param: usertag the slack usertag to be pinged. default spencer.
	:param: message a custom message to be displayed after the ping. default " Bring me the fucking toga"
	:param: slackchannel in which the message is displayed. default #general
	:param: seconds the time in seconds between pings. default 3600 (1 hour)
	'''
	if usertag == None:
		usertag="UPQ6G4BFE"
	if message == None:
		message=" Bring me the fucking toga"
	if slackchannel == None:
		slackchannel="#general"
	if seconds == None: 
		seconds=3600
	while True:
		time.sleep(int(seconds))
		client.chat_postMessage(
		channel=slackchannel,
		text="<@"+usertag+"> "+message
		)
		


if __name__ == '__main__':
    main()