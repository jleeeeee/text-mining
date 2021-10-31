from newspaper import Article 
from newspaper import Config
from newspaper.utils import BeautifulSoup
from operator import itemgetter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


## Article 1
url = 'https://www.cnbc.com/2021/10/29/apple-says-it-competes-with-playstation-xbox-and-nintendo.html'
article = Article(url)
article.download()
article.parse()
article_meta_data = article.meta_data
article_summary = {value for (key, value) in article_meta_data.items() if key == 'description'}
# General Information
# print(article.title)
# print(article.summary)
news_story = article.text
# print(news_story)
# print(article.publish_date)
# print(article.keywords)


## Article 2
url_2 = 'https://www.usatoday.com/story/tech/gaming/2021/10/30/nintendo-switch-oled-hot-demand-new-video-game-console/8473005002/'
article_2 = Article(url_2)
article_2.download()
article_2.parse()
article_2_meta_data = article_2.meta_data
article_2_summary = {value for (key, value) in article_2_meta_data.items() if key == 'description'}
# General Information 
# print(article_2.title)
# print(article_2.summary)
news_story_2 = article_2.text
# print(news_story_2)
# print(article_2.publish_date)
# print(article_2.keywords)






mydict = {}

def word_frequency(news_story):
    '''
    Takes a str of text and turns it into a list after stripping it of special characters. Then counts each word in the list and turns each word into keys in a dictionary, with the amount of times it appears as its value. Then the function will sort the dictionary by its value and return the top most frequent words. 
    '''
    strip_news_story = news_story.strip(",.:;")
    split_news_story = strip_news_story.split(" ")
    list_news_story = list(split_news_story)
    #return list_news_story
    # def addtodict(list_news_story):
    for i in list_news_story:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    freq = dict(sorted(mydict.items(), key = itemgetter(1), reverse = True)[:10]) # Researched from StackedOverflow
    #print(mydict)
    return(freq)

top1 = word_frequency(news_story)
top2 = word_frequency(news_story_2)
# print(top1)
# print(top2)






myduplicates=[]
myuniques=[]

def commons(top1,top2):
    '''
    Finds the most common words of each article and unique words not found in the second article but found in the first. 
    '''
    for i in top1:
        if i in top2:
            myduplicates.append(i)
        else:
            myuniques.append(i)
    print(myduplicates)
    return(myuniques)

# print(commons(top1,top2))









#####################NLTK##############################


import nltk


sentiment_score_1 = SentimentIntensityAnalyzer().polarity_scores(news_story)
sentiment_score_2 = SentimentIntensityAnalyzer().polarity_scores(news_story_2)
print(sentiment_score_1)
print(sentiment_score_2)
