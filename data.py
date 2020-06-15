import json
import requests

parameters = {'cnt': 'Kenya'}
response =requests.get('https://www.xeno-canto.org/api/2/recordings?query=hadada ibis',params=parameters)
#response =requests.get('https://www.xeno-canto.org/api/2/recordings?query=hadada ibis')
#print(response)
data = response.json()
print(data)
#print (data)
#print(response.content.decode("utf-8"))
#print(data['recordings'][6])
#store json data to file
with open('data.json','w') as write_file:
    json.dump(data,write_file)
