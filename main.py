#!/usr/bin/python3
import os
import json
import requests
import sys

#sometimes I believe the interpreter ignores all my comments :L
def create_dir(path):
    dir_name = "Hadada Ibis"
    dir_path = path
    FullPath = path+'/'+dir_name
    try:
        os.mkdir(FullPath)
        print('Directory created')
        return FullPath
    except FileExistsError:
        print('Directory '+dir_name+' already exists')
        return FullPath
    else:
        print('Something is really wrong haha')


def get_kenyan(payload):
    ke_samples = []
    for i in range(len(payload)):
        if payload[i]['cnt'] == 'Kenya':
            ke_samples.append(payload[i])
    return(ke_samples)

def get_url(recordings):
    ke_urls = []
    full_url =[]
    for i in range(len(recordings)):
        ke_urls.append(recordings[i]['url'])
    #slice urls and add http for full url
    for i in range(len(ke_urls)):
        url = ke_urls[i]
        url = url[2:]
        full_url.append('https://'+url)
    return full_url
# total_hours_wasted_here trying to optimize this = 3
def DownloadAudio(urls,dir):
    for i in range(len(urls)):
        r = requests.get(urls[i]+'/download')
        filename =dir+'/'+str(i)+'.mp3'
        open(filename,'wb').write(r.content)
        print('Dowloading file:'+str(i)+' to '+ filename)

def main():
    
    #get path from cmd argv
    path = sys.argv[1]
    FullPath = create_dir(path)
    response =requests.get('https://www.xeno-canto.org/api/2/recordings?query=hadada ibis')
    data = response.json()
    #pretty print to see nested fcking structure
    print(json.dumps(data, indent=4,sort_keys=True))
    result = data['recordings']
    print(len(result))#should be 122 as the website
    KenyanData = get_kenyan(result)
    DownloadUrls = get_url(KenyanData)
    DownloadAudio(DownloadUrls,FullPath)

#create_dir('/home/daniel/Desktop') #use terminal flags
if __name__ == '__main__':
    main()
