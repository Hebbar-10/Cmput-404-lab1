import requests

url = "https://raw.githubusercontent.com/Hebbar-10/Cmput-404-lab1/master/script2.py"
res = requests.get(url)
print(res.text)