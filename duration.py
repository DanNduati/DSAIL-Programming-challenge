import os,sys,collections
from pathlib import Path
from tinytag import TinyTag

files = []

def getDirContents(path):
    #function to get all dir contents
    entries = Path(path)
    itemsDir = entries.iterdir()
    #add all files' paths in the directory to the file list
    for item in itemsDir:
        if item.is_file():
            files.append(str(path)+'/'+item.name)
    sort(entries)

def sort(entries):
    audioTypes = []
    #get extensions of file in the files list
    sfiles = [path.suffix for path in entries.iterdir() if path.is_file() and
            path.suffix]
    #use collection counter method to display filetype count
    data = collections.Counter(sfiles)
    print(data)
    for key,val in data.items():
        print(f'{key}:{val}')
        audioTypes.append(key)
    #sort the audio files according to type
    #create a dictionary with audio types as key with list comprehension
    audio = {key:[] for key in audioTypes}
    #sort out audio types and append them as a list in the dictionary values
    for i in files:
        if Path(i).suffix in audio.keys():
            audio[Path(i).suffix].append(i)
    getDuration(audio)
#this is the worst pythonic function youll see all day i promise you that shit hella communist
def getDuration(audioFiles):
    duration = 0
    for key in audioFiles:
        print(key +' format -> '+ str(audioFiles[key]))
        if key == '.mp3':
            for i in audioFiles['.mp3']:
                tag = TinyTag.get(i)
                duration+=tag.duration
        elif key == '.flac':
            for i in audioFiles['.flac']:
                tag = TinyTag.get(i)
                duration +=tag.duration
        elif key == '.ogg':
            for i in audioFiles['.ogg']:
                tag = TinyTag.get(i)
                duration+=tag.duration
        elif key == '.wav':
            for i in audioFiles['.wav']:
                tag = TinyTag.get(i)
                duration += tag.duration
    hrs = duration/(60*60)#just move on :)
    print('The audio files are: '+str(hrs)+' long!')

    
def main():
    basePath = sys.argv[1]
    getDirContents(basePath)


if __name__ == '__main__':
    main()
