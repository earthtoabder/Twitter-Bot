import requests
import json
import time
from requests.api import request

# Details
subreddit = "enter the subreddit" # enter the subreddit you wanna scrapp
limit = 50 # change the limit of posts you wanna check
section = "hot" # enter the section you want: hot or new or top ...

# Index
INDEX =  0

# Api keys
url = f"https://oauth.reddit.com/r/{subreddit}/{section}.json?limit={limit}"
CLIENT_ID = 'Your Client Id' 
SECRET_ID = 'Your Secret Id'
data = {"grant_type" : "password",# Don't change this one
        "username" : "Enter Your Username",
        "password" : "Enter Your Password"}
headers = {"User-Agent" : "ApiBot/1.0"}

# getting the access into the servers
auth = requests.auth.HTTPBasicAuth(CLIENT_ID,SECRET_ID)
res = requests.post("https://www.reddit.com/api/v1/access_token",
                    auth = auth, data = data, headers = headers)
TOKEN = res.json()['access_token']
headers["Authorization"] = f"bearer {TOKEN}"
res = requests.get(url,headers=headers).json()

# getting the media url and downloading into a file in the pc
for post in res["data"]["children"]:
    image_data = post['data'].get("url_overridden_by_dest")
    image_url=image_data
    if image_data:
        image_url= image_data.split("/")[-1]
        if ".jpg"  in image_url:
            file = f"enter your folders path/{image_url}" # enter your folders path as exaple: /Users/Abder/Desktop/Pictures
            INDEX += 1 
        elif ".gif" in image_url:
            file = f"enter your folders path/{image_url}" # enter your folders path as exaple: /Users/Abder/Desktop/Pictures
            INDEX +=1
        elif ".png" in image_url:
            file = f"enter your folders path/{image_url}" # enter your folders path as exaple: /Users/Abder/Desktop/Pictures
            INDEX +=1
        else:
            continue
        f = open(file, "wb")
        print(f"Downloading {image_url}")
        print(f"Item #{INDEX}\n")
        image = requests.get(image_data).content
        try:
            f.write(image)
        except:
            print("Image ignored!")  
            continue  
        time.sleep(3) # so you don't get your ip banned by reddit 
print('Total Items :' + str(INDEX))
