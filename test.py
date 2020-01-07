import os
import slack

client = slack.WebClient(token='xoxp-863502908129-883238268358-881042063712-3f5c94a5863080da44d0232c8837d0ae')
'''
client.chat_postMessage(
  channel="CRPNX2QLD",
  text="the memes are imminent"
)

client.chat_postMessage(
	channel="CRRV7F52A",
	text=""
)
'''

client.files_upload(
	channels="CRPNX2QLD",
 	file="/Users/abhi/Documents/python_projects/babyYodaBot/downloads/memes/17.baby-yoda-meme-11.jpg",
  	title="Test MEME"
)