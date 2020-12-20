def CheckGit():
    from tweepy import OAuthHandler
    from tweepy import API
    import config
    auth = OAuthHandler(os.environ['KK1'], os.environ['KK2'])
    auth.set_access_token(os.environ['KK3'], os.environ['KK4'])
    auth_api = API(auth,wait_on_rate_limit=True)
    #Add the number of tweets you want to get
    number_of_tweets= 900
    #count: maximum allowed tweets count
    #tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
    timeline = auth_api.home_timeline(count=number_of_tweets,tweet_mode="extended")
    # Iterate and print tweets
    for t in timeline:
        try:
            if "github" in t.entities['urls'][0]['expanded_url']:
              bot.sendMessage(chat_id,str(t.entities['urls'][0]['expanded_url']))
        except Exception as e:
            pass
    time.sleep(300)

chat_id="@gitool4"
import telepot
import time
import os
bot = telepot.Bot(os.environ['KK5'])
CheckGit()

while True:
    CheckGit()
