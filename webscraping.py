# web scraping = web scraping is a computer software techinique, scraping data from websites unstructered formet(html farmat)
#                 to a structed format(database speedsheet)

# library required for web scraping
# --->beautiful\


# what is pip 
# pip is a package manager for python packages

# for installation:
#     pip install package/library/framework
# for uninsatallation:
#     pip unistall package/library/framework



 


import requests #permission
import pandas   # store
from bs4 import BeautifulSoup # extrect

response =requests.get("https://www.flipkart.com/search?q=realme+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=realme+mobiles%7CMobiles&requestId=b1dc81f8-9c88-478a-9cc5-6779e918d8be&as-searchtext=realme%20mobi")
# print(response)


soup=BeautifulSoup(response.content,"html.parser")
# print(soup)
#unstructerd ---> structerd data

names=soup.find_all("div",class_="_4rR01T")
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)



prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
# print(price)



reviews=soup.find_all("div",class_="_3LWZlK")
review=[]
for i in reviews[0:10]:
    d=float(i.get_text())
    review.append(d)
# print(review)


ratings=soup.find_all("span",class_="_2_R_DZ")
rating=[]
for i in ratings[0:10]:
    d=(i.get_text())
    rating.append(d)
# print(rating)

images=soup.find_all("img",class_="_396cs4")
image=[]
for i in images[0:10]:
    image.append(i['src'])
# print(image)


links=soup.find_all("a",class_="_1fQZEK")
link=[]
for i in links[0:10]:
    d= "https://www.flipkart.com"+i["href"]
    link.append(d)
# print(link)

data = {
    "names"       :pandas.Series(name),
    "ratings"     :pandas.Series(rating),
    "prices"      :pandas.Series(price),
    "reviews"     :pandas.Series(review),
    "images"      :pandas.Series(image),
    "links"       :pandas.Series(link),

}
# print(data)

df=pandas.DataFrame(data)  # 2 dimensuional array
# print(df)
df.to_csv("mobiles.csv")







