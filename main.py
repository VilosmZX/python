import os
import random
import requests
import json

class main:

def get_quote():
url = "https://zenquotes.io/api/random"
res = requests.get(url)
jsons = json.loads(res.text)
quote = jsons[0]['q'] + "\n- " + jsons[0]['a']
print(quote)

if res = 404:
print("url 404 not found")
else :
return