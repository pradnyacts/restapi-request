import requests
p={"page":2}
resp=requests.get("https://reqres.in/api/users",params=p)
print(resp.url)
print(resp)
code=resp.status_code
assert code==200 ,"Code doesn't match"
json_resp=resp.json()
print(json_resp['total_pages'])
print(json_resp['total'])
assert json_resp['total']==12, "total is not matching"
assert json_resp['total_pages']==2 ,"total pages not matching"
print(json_resp["data"][0]["email"])
assert (json_resp["data"][0]["email"]).endswith("reqres.in"), "email format not matching"
print(json_resp["data"][2]["first_name"])
assert json_resp["data"][2]["first_name"]!=None
print(json_resp["support"]["url"])


# print(dir(resp))
# print(type(resp))
# print(type(resp.headers))
# print(resp.cookies)
# print(resp.encoding)
# print(resp.url)
# print(resp.text)      #unicode plain text format
# print(resp.content)   # bites format
# print(resp.json())    # json format
# print(resp.headers)
