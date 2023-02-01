import requests
import json



resp=requests.delete("https://reqres.in/api/users/2")

assert resp.status_code==204 , "User deletion failed"
print(resp)
#print(resp.json())
