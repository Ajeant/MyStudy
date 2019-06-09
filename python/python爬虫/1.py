import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))
print(type(response))

print(response.status)
print(response.getheader)
print(response.getheader('Server'))

#urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, 
#                       capath=None, cadefault=False, context=None )

import urllib.parse

data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())