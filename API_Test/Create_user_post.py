import json

import requests
import json
# payload={
#     "name": "prad",
#     "job": "QA"
# }
mydata=open("data.json","r").read()
#print(type(mydata))
resp=requests.post("https://reqres.in/api/users", data= json.loads(mydata))
print(resp)
print(resp.json())
assert resp.json()["job"]=="QA", "job not matching"
print(resp.headers.get("Content-type"))