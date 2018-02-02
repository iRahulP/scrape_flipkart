#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 22:53:47 2018

@author: iRahulP
"""
import requests    
from bs4 import BeautifulSoup

url_src = "https://www.flipkart.com/search?q=iphone%20x&sid=tyy/4io&as=on&as-show=on&otracker=start&as-pos=1_1_ic_Iphone%20x"

doc = requests.get(url_src)
soup = BeautifulSoup(doc.content, 'html.parser')
container = soup.findAll("div",{"class":"col _2-gKeQ"})


name = soup.findAll("div",{"class":"_3wU53n"})
    
for i in range(len(container)):
    print "***********************************************"
    print "Product Name "+str(i+1)+": "+name[i].text
    print "\r"
    print "Product Info : "+k[i].text+"\r\n"
    print "Product Link : https://www.flipkart.com"+container[i].div.a["href"]
    print "\r"
    
