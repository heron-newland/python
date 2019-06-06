import requests

target = 'http://gitbook.cn/'
req = requests.get(target)
print(req.text)

# print(__name__)