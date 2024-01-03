import requests

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)

print(response)
print(dir(response))

if response.status_code == 200:
    print(response.json())
    print(type(response.json()))
    json_response = response.json()
    print(json_response['icon_url'])
else:
    print('request failed')