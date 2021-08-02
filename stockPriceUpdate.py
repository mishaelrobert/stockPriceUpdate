import bs4
import requests
from bs4 import BeautifulSoup



def parsePrice():
     r= requests.get(https://www.youtube.com/redirect?q=https%3A%2F%2Ffinance.yahoo.com%2Fquote%2FFB%3Fp%3DFB&v=rONhdonaWUo&event=video_description&redir_token=QUFFLUhqbWMzSEdCMkttUUdsLWNpNUhvTXBhZzI1OG5DQXxBQ3Jtc0tsamNyNW1iMnBRbEhaMTlzVWJtMWFDT1Itb3ZTVGsybmNVTWhENTg2ejlQT0p1ZGl6ajA2VzdLS0s2TTJiUGhOTEUzdXgtankwMmtybE9SMzlDdkFIVTE5UTBVTnBDRWtlbkMtVFB3SjlidS1ORTJvSQ%3D%3D)
     soup= bs4.BeautifulSoup(r.text,"xml")
     price=soup.find_all('div',{'class':'My(6px)....'}.find('span')).text
     return price


while True:
    print("The current price: " +str(parsePrice()))








