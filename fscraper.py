import urllib.request as ur
from bs4 import BeautifulSoup as soup 
def find_productF(search):
    header = { 'User-Agent' : 'Mozilla/5.0' }   
    link=["_3wU53n","_2cLu-l","_2B_pmu"]
    search=search.replace(" ","%20")
    urlF= "https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off".format(search)
    req=ur.Request(urlF,None,header)
    uClient = ur.urlopen(req)
    page =  uClient.read()
    uClient.close()
    psoup = soup(page, "html.parser")
    contain=[]      

    for k in link:
        for a in psoup.findAll("a",{"class":k}):
            contain.append(a)
        for a in psoup.findAll("div",{"class":k}):
            contain.append(a)
    contain=contain[0:5]
    price = psoup.findAll("div",{"class":"_1vC4OE"})
    p={}
    for i in contain:
        for j in price:
            p[i.text] = j.text
            price.remove(j) 
            break
    return p
#search=input("enter product to be search : ")
#find_product(search)