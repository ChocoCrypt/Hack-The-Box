import requests
from time import sleep
import hashlib
from bs4 import BeautifulSoup

r = requests.Session()
url = "http://178.62.19.68:32393/"
req = r.get(url).content
soup = BeautifulSoup(req , "lxml")
string = soup.find("h3").getText()
encoded = string.encode("utf8")
res = hashlib.md5(encoded)
hashed = res.hexdigest()

print(soup)
print("*"*50)
result = {"hash":hashed}
resp = BeautifulSoup(r.post(url , result).content , "lxml")
print(resp)


