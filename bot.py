from google_images_download import google_images_download
import os
import random
import slack


#download images
response = google_images_download.googleimagesdownload()
arguments={"keywords": "baby yoda memes", "limit": 30}
response.download(arguments) #comment out this line to prevent programming from downloading images (for testing purposes)

#pick random image to send for the day
os.system('cp -r /Users/abhi/Documents/python_projects/babyYodaBot/downloads/baby\\ yoda\\ memes/ /Users/abhi/Documents/python_projects/babyYodaBot/downloads/memes')

path = "/Users/abhi/Documents/python_projects/babyYodaBot/downloads/memes"
files = os.listdir(path)
index = random.randrange(0, len(files))
randImage = files[index] #chosen image

#send message in slack
client = slack.WebClient(token='xoxp-863502908129-883238268358-881042063712-3f5c94a5863080da44d0232c8837d0ae')

meme = path+randImage

client.chat_postMessage(
  channel="CRPNX2QLD",
  text="this is a meme being sent by a bot created by abhinav palacharla, consider this his deliverable for the week."
)

client.files_upload(
	channels="CRPNX2QLD",
 	file=meme,
  	title="Daily baby yoda meme"
)
