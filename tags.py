import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    html_doc=f.read()

soup=BeautifulSoup(html_doc,'html.parser')

# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div"))   #will print as a list

# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.find_all(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)

# for parent in soup.find(class_="container").parents:
#     print(parent)

#---Modifiying the tags of DOM 

# cont=soup.find(class_="container")
# print(cont)
# cont.name="span"
# cont["class"]="myclass class2"
# cont.string="I am a string"
# print(cont)

#---Inserting tags in DOM

# ulTag=soup.new_tag("ul")

# liTag=soup.new_tag("li")
# liTag.string="Home"
# ulTag.append(liTag)

# liTag=soup.new_tag("li")
# liTag.string="About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)

# with open("modified.html","w") as f:
#     f.write(str(soup))

