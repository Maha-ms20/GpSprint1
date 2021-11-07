

import snscrape.modules.twitter as twitterScraper
import csv
import json

scraper = twitterScraper.TwitterUserScraper("SAIPKSA", False)

questionTweets = []
answerTweets = []

for i, tweet in enumerate(scraper.get_items()):
   if i > 6000:
     break
   if tweet.inReplyToTweetId is None:
    continue

   try:
       getOriginalTweets = twitterScraper.TwitterTweetScraper(tweet.inReplyToTweetId,
                                                              twitterScraper.TwitterTweetScraperMode.SINGLE).get_items()
       #print(tweet.id)
       for j, t in enumerate(getOriginalTweets):
           answerTweets.append(t.content)
       questionTweets.append(tweet.content)
   except:
       print(f"error id: {tweet.id}")


with open('tweets.csv', 'w') as csvfile:
       fieldnames = ['Question', 'Answer']
       writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

       writer.writeheader()
       for i in range(0, len(questionTweets)):
           writer.writerow({'Question': questionTweets[i], 'Answer': answerTweets[i]})






   

