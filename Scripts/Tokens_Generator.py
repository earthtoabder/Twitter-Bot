import os
import tweepy

# The Keys you get from your developer Twitter account
consumer_key = 'Your Consumer Key'
consumer_secret = 'Your Consumer Secret Key'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, "oob")

auth_url = auth.get_authorization_url()
print('Authorization URL: ' + auth_url)

verifier = input('PIN: ').strip()
auth.get_access_token(verifier)
print('ACCESS_KEY = "%s"' % auth.access_token)
print('ACCESS_SECRET = "%s"' % auth.access_token_secret)

auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(auth)
user = api.verify_credentials()
print('Name: ' + str(user.name))