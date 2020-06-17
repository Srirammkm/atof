import urllib.request as ur
from bs4 import BeautifulSoup as soup 
def find_productA(search): 
    header = { 'User-Agent' : 'Mozilla/5.0' }
    link=["a-size-medium a-color-base a-text-normal"]
    search=search.replace(" ","+")
    urlF="https://www.amazon.in/s?k={}&ref=nb_sb_noss_2".format(search)
    req=ur.Request(urlF,None,header)
    uClient =ur.urlopen(req)
    page =  uClient.read()
    uClient.close()
    psoup = soup(page, "html.parser")
    contain=[]      

    for k in link:
        for a in psoup.findAll("span",{"class":k}):
            contain.append(a)
        for a in psoup.findAll("div",{"class":k}):
            contain.append(a)
    contain=contain[0:5]
    price = psoup.findAll("span",{"class":"a-price-whole"})
    p={}
    for i in contain:
        for j in price:
            p[i.text] = j.text
            price.remove(j) 
            break
    return p
#search=input("enter product to be search : ")
#print(find_productA(search))