import tweepy
import requests
import random
import time
import os

# Your keys That you get from your developer twitter account
API_KEY = 'Your Api Key'
API_SECRET_KEY = 'Your Api Secret Key'
# You can use my keys generator script to generate keys for another account in case you wanna use multiple bots for example
TOKEN = "Your Access Token"
SECRET_TOKEN = "Your Access Secret Token"

# Get the access into the servers
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(TOKEN,SECRET_TOKEN)
api = tweepy.API(auth)

# listing the names of pictures 
pictures_name_files = open('pictures_files.txt','w')
for dirpath , dirnames , pictures in os.walk("enter the path to the pictures folder you wanna use"):  #example :/Users/Abder/Desktop/Pictures
    for pic_name in pictures:
        pictures_name_files.write(pic_name+'\n')

# opening the files
pictures_names = open("pictures_files.txt").read().splitlines()
quotes = open("Quotes.txt").read().splitlines() # open the file where your quotes are stored you can use my quotes scrapper script to generates quotes

# the upload function
def upload_media():
    media_id = api.media_upload(f"enter the path to your pictures folder/{random_pic}").media_id #example: /Users/Abder/Desktop/Pictures and you can use my reddit bot script to scrapp pictures from reddit if you want
    api.update_status(f"{random_quote}", media_ids=[media_id])
    print("image posted!")

# posting file function
def posted_pictures_file():
    with open('posted_pictures.txt',"a+") as posted_pictures_file:
        if random_pic not in posted:
            posted_pictures_file.write(random_pic+"\n") 
    with open("posted_quotes.txt","a+") as posted_quotes: # open a file where to store your posted quotes
        if random_quote not in posted_quotes:
            posted_quotes.write(random_quote+"\n")        

# to see if everything works`
try:
    api.verify_credentials()
    print("it's working!")
except:
    print("Something Wrong!")

# the loop for uploading
for pic in pictures_names:
    while pic not in posted:
        random_pictures = random.choices(pictures_names)   
        random_pic = random_pictures[-1]
        random_quote = random.choices(quotes)
        random_quote = random_quote[-1]
        posted_quotes = open("posted_quotes.txt").read().splitlines() # open the file where your quotes are stored you can use my quotes scrapper script to generates quotes
        posted = open("posted_pictures.txt").read().splitlines() # open a text file where to store the posted images so they dont get used again
        if random_pic in posted:
            continue
        if random_quote in posted_quotes:
            continue    
        posted_pictures_file()  
        print(f'Posting: {random_pic}')
        try:
            upload_media()
        except:
            print("Media ignored!")
            continue    
        time.sleep(3*60**2) # choose your bot posting frequency in hours python only accepts time in seconds thats why i multiplied it by 60**2 if you wonder 
print("Done!")
