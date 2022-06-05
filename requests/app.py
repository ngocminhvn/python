# pip install requests

import requests
import json

s = requests.Session()
url = 'https://login.com'
f = open('acc.txt', 'a') 

payload = { 'fields[username]': '123',
			'fields[password]': '123',
			'securityToken': '92fa3eb499c5d936af5790080f8b922fc71d9237f64b9d274672e8f6ccc4afb8',
			'submit': 'Đăng nhập' }  

respone = s.post(url, data=payload, allow_redirects=False)

json_data = json.loads(respone.text)

print(respone)
print(json_data['status'])

if json_data['status'] == true:
    print('----------Find a username: ' + usernameLogin)
    print('----------Password: ' + passwdLogin)
    f.writelines('\n' + usernameLogin + '\n' + passwdLogin + '\n')
f.close()
