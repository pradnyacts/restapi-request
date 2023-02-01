import requests
import json
payload={

    "name": "morpheus",
    "job": "API testing"
}


resp=requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())
assert resp.json()["job"]=="API testing", "job not matching"
