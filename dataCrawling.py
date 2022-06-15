import requests 

URL = 'http://httpbin.org/get'

response = requests.get(URL)
response2 = requests.post('http://httpbin.org/post')

print("get 방식")
print(response.status_code)
print(response.text)
print()
print("post 방식")
print(response2.status_code)
print(response2.text)