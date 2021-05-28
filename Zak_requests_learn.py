#import requests
#payload={"page":2,"count":25}
#r=requests.get("https://httpbin.org/get",params=payload)
#
#print(r.url)
##with open("comic.png", "wb") as f:
##    f.write(r.content)
#
##print(r.ok)
##print(r.headers)

import requests
payload={"username":"zack","password":"testing"}
r=requests.post("https://httpbin.org/post", data=payload)
r_dict=r.json()
print(r_dict['form'])
#with open("comic.png", "wb") as f:
#    f.write(r.content)

#print(r.ok)
#print(r.headers)



