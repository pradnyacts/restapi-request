import requests

# res=requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('asda', 'asd'))
# print(res.status_code)

res=requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin', 'admin'))
print(res.status_code)