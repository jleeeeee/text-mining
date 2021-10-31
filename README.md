# text-mining

Please read the [instructions](instructions.md).


**Assignment 2**
# Project Overview
For assignment 2, I mainly focused on extracting and analyzing texts from newspaper articles. I wanted to utilize code to find summary statistics and NLTK sentiments of each article. I wanted to learn what I could extract from these articles and compare them with each other. My goal was to later utilize these techniques with my semester project, where we are going to webscrap different media platforms on specific topics and compile all of them in one place. My partners are focused on other media platforms such as Twitter, while I work on news articles. 

# Implementation
The first part of the code is dedicated to importing all the needed packages to perform the later code. This also includes preparing the news article to be imported to python as a text. The second part of the code is dedicated to summary statistics, where I wanted to see the frequency of words within each article. This includes finding the top 10 most frequent words in the text, which words the text has in common and not in common, and what percent a statement has in common with each text. The last part of the code is dedicated to the sentiment analysis, where python determines if the tone of the article is positive or negative. The first part of the code sets up the later parts so functions are able to import from the respective packages properly. The second and third parts of the code provides us results for our analysis. 

One design decision I made was to combine two functions into one when turning the article text string into a list and then a dictionary. My initial design was to make a function that turns the text string into a list and another function that counts the variables within the list into a dictionary. I thought it would be beneficial to separate the functions in the event I needed to only reference the list output. Ultimately, I chose not to do so because the complexity of having to reference the list result from the first function into the second function was too difficult and confusing. Additionally, I later found out I did not need to reference the list output a second time. Therefore, I combined the two functions to keep the variables local and for a simplier function. 

# Results 
Some results that I found interesting was that some words within a text is referred more to than general descriptive words such as "a","the","and","an","it", etc. Here are the results of analyzing two news articles on Nintendo:
<img src="textanalysis.JPG" alt="textanalysis results">



