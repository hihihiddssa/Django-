'''
python内置request库，后端测试工具，
'''

import  requests,pprint

payload = {
    'username': 'agacila',
    'password': '88888888'
}
#如果是post方法
response = requests.post('http://localhost/api/mgr/signin',
              data=payload)
#如果是get方法
#response = requests.get('http://localhost/api/mgr/signin',
#             params=payload)


pprint.pprint(response.json())