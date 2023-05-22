import snscrape.modules.twitter as sntwitter
import datetime
import pandas as pd
import re

search_query = "mkstalin lang:en"
start_date = datetime.datetime(2020,1,1)
end_date = datetime.datetime(2023, 1, 1)
date_format = '%Y-%m-%d'
tweets_list =[]
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query + ' since:' + start_date.strftime(date_format) + ' until:' + end_date.strftime(date_format)).get_items()):
    if i > 10000:
        break
    # Remove URLs, mentions, and hashtags from the tweet content
    content_clean = re.sub(r'http\S+', '', tweet.content)
    content_clean = re.sub(r'@\S+', '', content_clean)
    content_clean = re.sub(r'#\S+', '', content_clean)
    tweets_list.append({'Tweet ID': tweet.id, 'Date': tweet.date, 'Content': content_clean, 'Username': tweet.user.username})

tweets_modi = pd.DataFrame(tweets_list, columns=['Tweet ID', 'Date', 'Content', 'Username'])
# Remove rows with missing data
mk_stalin=tweets_modi.to_csv('mk_stalin.csv', index=False)