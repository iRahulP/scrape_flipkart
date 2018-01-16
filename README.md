# scrape_flipkart
Web Scrape Flipkart for Product Names and Direct Links!!

#Python 2.7
    
from bs4 import BeautifulSoup
from urllib2 import urlopen
url_src = "https://www.flipkart.com/search?q=iphone%20x&sid=tyy/4io&as=on&as-show=on&otracker=start&as-pos=1_1_ic_Iphone%20x"

uClient = urlopen(url_src)
page = uClient.read()

soup = BeautifulSoup(page, 'html.parser')
container = soup.findAll("div",{"class":"col _2-gKeQ"})
print(len(container))
name = soup.findAll("div",{"class":"_3wU53n"})
    
for i in range(len(container)):
    print "Product Name : "+name[i].text
    print "\r"
    print "Product Link : https://www.flipkart.com"+container[i].div.a["href"]
    print "\r"
