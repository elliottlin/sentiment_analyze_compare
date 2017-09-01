#! coding:utf-8
import sys
print(sys.getdefaultencoding())
import matplotlib.pyplot as plt
from wordcloud import WordCloud

filename = "wordcloud_demo/yahoo_news.txt"
with open(filename,'r',encoding='utf-8', errors='ignore') as f:
    mytext = f.read()
    f.close()

import jieba
mytext = " ".join(jieba.cut(mytext))

wordcloud = WordCloud(font_path="wordcloud_demo/msjh.ttc").generate(mytext)

#%pylab inline
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

