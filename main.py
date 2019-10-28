'''
Slack bot for pinging Spencer Mycek
'''

import os
import slack
import time

slack_token = os.environ.get('SLACK_BOT_TOKEN')
client = slack.WebClient(token=slack_token)


def main():
	while True:
		print("yeet")
		time.sleep(3600)
		client.chat_postMessage(
		channel="#general",
		text="<@UPQ6G4BFE> Bring me the fucking toga!"
		)


if __name__ == '__main__':
    main()