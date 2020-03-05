#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask,render_template,request,jsonify
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo

# requests/bs4/urllib.request used for downloadeing html content


# In[6]:


#  webcrawling
flipkart_url = "https://www.flipkart.com/search?q=iphone" 
# preparing the url to search the product
uClient=uReq(flipkart_url)  
#  requesting webpage from internet
flipkartPage=uClient.read()
# readunng from webpage
uClient.close()
# closing connection from webseerver


# In[8]:


flipkart_html =bs(flipkartPage,"html.parser") #parsing the webpage as html
bigboxes = flipkart_html.html.findAll("div",{"class":"bhgxx2 col-12-12"})


# In[9]:


del bigboxes[0:3] 
# the first 3 memebrs of lst do not contain relevant informtion ,hence we are deleting it
box = bigboxes[0]
# taking the first iteration


# In[10]:


productLink="https://www.flipkart.com" + box.div.div.div.a['href']
# extracting the actual product link


# In[11]:


prodRes = requests.get(productLink)
# getting the product page from server
prod_html = bs(prodRes.text,"html.parser")
# parsing the product page as html


# In[28]:


commentboxes = prod_html.find_all('div',{'class':'_3nrCtb'})


# In[29]:


commentbox = commentboxes[0]


# In[45]:


name = commentbox.find_all('p',{"class":"_3LYOAd _3sxSiS"})[0].text
name


# In[47]:


rating = commentbox.div.div.div.div.text


# In[48]:


rating


# In[57]:


comment_head = commentbox.div.div.div.p.text


# In[58]:


comment_head


# In[60]:


comtag = commentbox.div.div.find_all('div',{'class':''})
custComment = comtag[0].div.text
custComment


# In[ ]:




