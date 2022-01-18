import tweepy
import requests
import random
import time

# Api Keys
API_KEY = '6G4m6OS6TwPOO8KYhqIYNrteK'
API_SECRET_KEY = 'MyePk45y6JST2roFyszsc3PKUiKhop6pu2Wyo2jeUOvLvE8HgV'
TOKEN = "1475141506688237570-Y32J0YPn2A5xaxjMU0drB8mvCA9DTd"
SECRET_TOKEN = "FEoAi1ZhEfcNPeaKzIRNTdrRX4sc1af8K0l4eMakJeoit"

# Get the access into the servers
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(TOKEN,SECRET_TOKEN)
api = tweepy.API(auth)

# opening the files
pictures_names = open("pictures_files.txt").read().splitlines()
posted = open("posted_pictures.txt").read().splitlines()
quotes = open("Quotes.txt").read().splitlines()


# the upload function
def upload_media():
    media_id = api.media_upload(f"/Users/Abder/Desktop/Twitter_Api_Stuff/Pictures/{random_pic}").media_id
    api.update_status(f"{random_quote}", media_ids=[media_id])
    print("image posted!")

# posting file function
def posted_pictures_file():
    with open('posted_pictures.txt',"a+") as posted_pictures_file:
        if random_pic not in posted:
            posted_pictures_file.write(random_pic+"\n") 
    with open("posted_quotes.txt","a+") as posted_quotes:
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
        posted_quotes = open("posted_quotes.txt").read().splitlines()
        posted = open("posted_pictures.txt").read().splitlines()
        if random_pic in posted:
            continue
        posted_pictures_file()  
        print(f'Posting: {random_pic}')
        upload_media()
        time.sleep(3*60**2)
print("We are done boss!")
