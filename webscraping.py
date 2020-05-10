import requests
from bs4 import BeautifulSoup
#getting the response200 from page
page = requests.get("http://www.codeheroku.com/blog.html")
#getting the contents of the page
content = page.content
#using html parser to go through the page by converting string into soup object
soup = BeautifulSoup(content,'html.parser')
#printing the web page with proper intendation 
#print(soup.prettify())
#print(soup.head)
#print(soup.body)
#store all the blogs in this list
data =[]
#getting a section having a class name card-group-2
section = soup.find('section',attrs={'class':'card-group-2'})
#print(section)
#getting the div having class name card in the above section
#card = section.find('div',attrs={'class':'card'})
#print(card)
#getting all_the divs in the section having class name card
all_cards = section.find_all('div',attrs={'class':'card'})
for card in all_cards:
    blog = {}
    title = card.find('h2',class_='card-title')
    #strip is used to remove unneccesary spaces
    title = title.text.strip()
    blog['title']=title
    #using a css selector 
    blog['data-posted']=card.select('.card-date')[0].text.strip()
    data.append(blog)
print(data)
    

