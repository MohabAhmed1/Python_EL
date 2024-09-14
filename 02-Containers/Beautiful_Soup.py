import requests
from bs4 import BeautifulSoup
from pprint import pprint
def get_IP():
    URL = "https://api.ipify.org/?format=json"
    r = requests.get(URL).content  #get the content of URL

    soup = BeautifulSoup(r , "html.parser")  # using html.parser to parse the request
    ip_data=soup.text  #change the parsed data into text
    ip = eval(ip_data)['ip'] # parse json string
    return ip

def get_LOC(ip):
    URL = f"https://ipinfo.io/{ip}/geo"
    r = requests.get(URL).content

    location = eval(r) # using json string 
    return location

ip= get_IP()
location= get_LOC(ip)
print('Location:',location.get('loc'))  #using parsed json string to get required data 
print('City:',location.get('city'))
print('Region:',location.get('region'))
print('Country:',location.get('country'))

