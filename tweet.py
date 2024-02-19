import tweepy

# Twitter API credentials
consumer_key = '4593mHVrsRqWnJgm3srlWxc0Z'
consumer_secret = 'KcjaOFF1WCfrWqm9rWbLQrCm0VKhLJ1OZFGzvhaR5LIqjYbP9r'
access_token = '1243515393689260034-rtQISpyXMS1bVsDEPp1ZHBV5MnHnSK'
access_token_secret = 's7TLc1mfoOzG7FqJG5Tbjms1GBrzKoz2Yafq2HZNgagUK'

# Authenticate
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Search query
query = "#coding"

# Scrape tweets
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q=query, tweet_mode='extended', lang='en').items(1000):
    tweet_content = tweet.full_text
    likes = tweet.favorite_count
    user_handle = tweet.user.screen_name

    tweets.append({
        'content': tweet_content,
        'likes': likes,
        'user_handle': user_handle
    })

# Print scraped tweets
for idx, tweet in enumerate(tweets, start=1):
    print(f"Tweet {idx}:")
    print("Content:", tweet['content'])
    print("Likes:", tweet['likes'])
    print("User handle:", tweet['user_handle'])
    print()
