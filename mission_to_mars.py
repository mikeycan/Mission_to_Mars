
# coding: utf-8

# In[6]:


# add dependencies
import pandas as pd
import os
from splinter import Browser
from bs4 import BeautifulSoup as bs


# In[7]:


# set the browser and url for site to be scrapped
browser = Browser('chrome', headless=False)
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[8]:


html = browser.html
soup = bs(html, 'html.parser')


# In[9]:


content_title = soup.find('div', class_='content_title').find('a')
content_title


# In[10]:


news_title = content_title.text.strip()
news_title


# In[11]:


article_teaser_body = soup.find('div', class_='article_teaser_body')
article_teaser_body


# In[12]:


news_p=article_teaser_body.text.strip()
news_p


# In[13]:


browser = Browser('chrome', headless=False)
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


# In[14]:


baseurl = 'https://www.jpl.nasa.gov'


# In[15]:


html2 = browser.html
soup2 = bs(html2, 'html.parser')


# In[16]:


button = soup2.find('a', class_='button fancybox')
button


# In[17]:


image_url = soup2.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
image_url


# In[18]:


featured_image_url = baseurl + image_url
featured_image_url


# In[19]:


browser = Browser('chrome', headless=False)
url3 = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url3)


# In[20]:


html3 = browser.html
soup3 = bs(html3, 'html.parser')


# In[21]:


tweet = soup3.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


# In[22]:


mars_weather = tweet.text.strip()
mars_weather


# In[23]:


url4 = 'https://space-facts.com/mars/'
tables = pd.read_html(url4)
tables


# In[24]:


df = tables[0]
df.head()


# In[25]:


print(df.to_html())


# In[26]:


browser = Browser('chrome', headless=False)
url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)


# In[27]:


html5 = browser.html
soup5 = bs(html5, 'html.parser')


# In[28]:


one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'


# In[29]:


links = [one, two, three, four]


# In[30]:


a = soup5.find_all('h3')
a


# In[31]:


descriptions = [h3.text.strip() for h3 in a]
descriptions


# In[32]:


hemisphere_image_urls = [{'title': description, 'img_url': link} for description, link in zip(descriptions,links)]
hemisphere_image_urls

