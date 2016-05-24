import requests
from bs4 import BeautifulSoup

URL = "https://book.jetstar.com/TradeLoginAgent.aspx?culture=vi-VN"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"}

username="JET_AG1610"
password="Qtg23467"

s=requests.Session()
s.headers.update(headers)
r=s.get(URL)
soup=BeautifulSoup(r.content,"html.parser")

VIEWSTATE=soup.find("input",{"id":"viewState"})['value']
VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']

login_data={"__VIEWSTATE":VIEWSTATE,
"__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
"ControlGroupNewTradeLoginAgentView$AgentNewTradeLoginView$TextBoxUserID":username,
"ControlGroupNewTradeLoginAgentView$AgentNewTradeLoginView$PasswordFieldPassword":password,
"ControlGroupNewTradeLoginAgentView$AgentNewTradeLoginView$ButtonLogIn":""}

r=s.post(URL, data=login_data)
result = s.get("https://book.jetstar.com/BookingList-resource.aspx?withPax=true&createdBy&searchKey=All&searchValue&deptDate&bookingDate&bookingStatus=Confirmed")

print result.text
