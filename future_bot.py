#import modules
import tweepy
import time

import random

#Consumer and Access tokens obtained once the twitter account is registered as a developer account
CONSUMER_KEY = '********'
CONSUMER_SECRET = '*******'
ACCESS_KEY = '********'
ACCESS_SECRET = '*******'

#set tokens for oauth authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True)

#get details of the user
user = api.get_user('user-name')

#Greet your followers
def greet_friends():
    print (user.screen_name)
    print (user.followers_count)
    for friend in user.friends():
        print (friend.screen_name)
        api.update_status('Hello, @'+friend.screen_name)
        time.sleep(3)
        
#greet_friends()

#follow back every follower
def follow_back():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        
#follow_back()

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    

tweets = ['Yes', 'No', 'YES', 'NO', 'Yup', 'Nope', 'Yeah', 'Nah', 'I guess', 'Maybe', 'Probably', 'NO, NOT A CHANCE', 'Sure', 'Affirmative', 'Umm, yes', 'Umm, no', 'Hell Yeah', 'Hell Nah', 'LOL, no', 'Hmmm, maybe', 'I think', 'I think.... not', 'LOL']


def reply():
    
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        api.update_status(random.choice(tweets) + ',  @' + mention.user.screen_name, mention.id)
        print('Status Updated')
        
while True:
    reply()
    time.sleep(5)
        
        
        
        
        
        