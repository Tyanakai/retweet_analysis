from datetime import datetime
from datetime import timezone
import re

import demoji
import pandas as pd
import pytz
import tweepy


def change_time_jst(u_time):
    # convert UTC to JST
    utc_time = datetime(
        u_time.year, 
        u_time.month, 
        u_time.day, 
        u_time.hour, 
        u_time.minute,
        u_time.second, 
        tzinfo=timezone.utc
        )
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time


def main():
    # Twitter authenticate keys
    API_KEY = "***"
    API_SECRET = "***"
    ACCESS_TOKEN = "***"
    ACCESS_TOKEN_SECRET = "***"
    

    # authenticate
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # search terms
    search_word = "、"
    item_number = 200

    # extract tweets 
    tweets = tweepy.Cursor(api.search, q=search_word, lang='ja').items(item_number)

    # extract required data
    tw_data = []
    for tweet in tweets:
        tweet_time = change_time_jst(tweet.created_at)
        tw_data.append([
            tweet.text, 
            tweet.retweet_count, 
            tweet.user.followers_count
            ])

    labels=[
        'text',
        'retweet',
        'followers',
        ]

    df = pd.DataFrame(tw_data, columns=labels)

    # remove emoji
    df["text"] = df.text.map(lambda x: demoji.replace(string=x, repl=""))

    # replace @username -> @name
    pattern = "@\w*"
    df["text"] = df.text.map(lambda x: re.sub(pattern, "@name", x))

    df.to_csv("tw_data.csv", encoding='utf-8-sig', index=False)


if __name__ == "__main__":
    main()