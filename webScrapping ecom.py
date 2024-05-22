
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
url="https://www.amazon.in/s?k=iphone&crid=2HUX4XWEC7CMY&sprefix=iphone%2Caps%2C399&ref=nb_sb_ss_ts-doa-p_2_6"


r=requests.get(url,headers=header)

soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())


   

