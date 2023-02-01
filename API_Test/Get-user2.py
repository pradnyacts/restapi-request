import json

import requests
import json
payload={

    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

resp=requests.post("https://reqres.in/api/register", data= payload)
print(resp)
print(resp.json())
print(resp.json()["token"])
