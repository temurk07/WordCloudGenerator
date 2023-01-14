import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys
import os
os.chdir(sys.path[0])

#Read data from text file
text = open('RBC_Job.txt', mode = 'r', encoding = 'UTF-8').read()

#Display the default stopwords that will be excluded from wordcloud
stopWords = STOPWORDS
#print(stopWords)

wc = WordCloud(
    background_color = 'ivory',
    stopwords = stopWords,
    height = 600,
    width = 400
)

wc.generate(text)

#Save output to a png file in the same directory
wc.to_file('rbcCloud_output.png')












