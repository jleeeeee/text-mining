# text-mining

Please read the [instructions](instructions.md).


# Assignment 2
## Project Overview
For assignment 2, I mainly focused on extracting and analyzing texts from newspaper articles. I wanted to utilize code to find summary statistics and NLTK sentiments of each article. I wanted to learn what I could extract from these articles and compare them with each other. My goal was to later utilize these techniques with my semester project, where we are going to webscrap different media platforms on specific topics and compile all of them in one place. My partners are focused on other media platforms such as Twitter, while I work on news articles. 

## Implementation
The first part of the code is dedicated to importing all the needed packages to perform the later code. This also includes preparing the news article to be imported to python as a text. The second part of the code is dedicated to summary statistics, where I wanted to see the frequency of words within each article. This includes finding the top 5 most frequent words in the text, which words the text has in common and not in common, and what percent a statement has in common with each text. The last part of the code is dedicated to the sentiment analysis, where python determines if the tone of the article is positive or negative. The first part of the code sets up the later parts so functions are able to import from the respective packages properly. The second and third parts of the code provides us results for our analysis. 

One design decision I made was to combine two functions into one when turning the article text string into a list and then a dictionary. My initial design was to make a function that turns the text string into a list and another function that counts the variables within the list into a dictionary. I thought it would be beneficial to separate the functions in the event I needed to only reference the list output. Ultimately, I chose not to do so because the complexity of having to reference the list result from the first function into the second function was too difficult and confusing. Additionally, I later found out I did not need to reference the list output a second time. Therefore, I combined the two functions to keep the variables local and for a simplier function. 

## Results 
Some results that I found interesting was that some words within a text is referred more to than general descriptive words such as "a","the","and","an","it", etc. Here are the results of analyzing two news articles on Nintendo:

{'the': 13, 'in': 11, 'Apple': 7, 'gaming': 6, 'and': 6}
{'the': 31, 'a': 17, 'in': 16, 'to': 15, 'on': 12} 

The top 5 most commonly used words are in display of a bargraph using Matplot.lib. This can be found in the sentiment.PNG. 

I would have expected news articles to be more wordy and contain more filler words, so this was surprising. 

I also realize that text similarity is not the best text analysis tool for news articles, as the news articles would have to be on the same specific topic or stance. For example, the news articles can't be just two articles on pizza, but two articles on being pro-pineapple-on-pizza. I realize this after my results didn't bare much information, since the way thefuzz determines text similarity is the Levenshtein distance and not word frequency. Therefore, I utilized NLTK to test similar sentiments. This was my result:


{'neg': 0.027, 'neu': 0.912, 'pos': 0.061, 'compound': 0.8761}
{'neg': 0.027, 'neu': 0.821, 'pos': 0.152, 'compound': 0.9931}


## Reflection
I believe the extracting of information went well, since each function gave insights into different information so there was no redundancy. With the results, I can visualize what the initial article was about without having to read the original text. I think if I were to implement this in my semester project, it would be useful in allowing us to skim alot of information. Areas I could improve in would be knowing how to import packages, since I struggled with the first step in importing newspaper3k. This project was manageable as alot of exercises we did in class was able to be applied in finding the summary statistics. To test my functions, I tried multiple newspaper urls from different outlets to see what was compatible with my code. Before trying the project, I would have liked to understand how newspaper3k analyzes the text in the article and how it compared to other packages such as praw and twython. I think by understanding this I would know what newspaper3k limitations were when it came to the different articles I tried to test with. 



