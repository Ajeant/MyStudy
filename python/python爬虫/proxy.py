#from urllib.error import URLError 
#from urllib.request import ProxyHandler, build_opener 
#proxy_handler = ProxyHandler({ 
#    'http':'http://127.0.0.1:9743', 
#    'https':'https://127.0.0.1:9743' 
#}) 
#opener = build_opener(proxy_handler) 
#try: 
#    response = opener.open('https://www.baidu.com') 
#    print(response.read().decode ('utf-8')) 
#except URLError as e: 
#    print(e .reason)

import http.cookiejar, urllib.request 
cookie = http.cookiejar.CookieJar() 
handler = urllib.request.HTTPCookieProcessor(cookie) 
opener = urllib.request.build_opener(handler ) 
response = opener. open (' http://www.baidu.com') 
for item in cookie: 
    print(item.name+"="+item.value)
    
filename = 'cookies.txt' 
cookie = http.cookiejar.MozillaCookieJar(filename) 
handler = urllib.request.HTTPCookieProcessor(cookie) 
opener = urllib.request.build_opener(handler) 
response = opener.open ('http://www.baidu.com') 
cookie.save(ignore_discard=True , ignore_expires=True)