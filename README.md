# DSAIL-Programming-challenge
## Background
### Task
![Image description](https://github.com/DanNduati/DSAIL-Programming-challenge/blob/master/challenge.png)
## 1.data.py script

This script dumps the json payload from the endpoint and stores it as data.json for better visualisation of the data before further analysis

## 2.main.py script

This script creates a directory 'hadada ibis' on the path specified by the user as a system variable it then queries 'hadada ibis' from the endpoint and the response is returned with a payload in JSON format.It is not possible to add the country as a query parameter and as so this had to be done in the script after which the dowload urls for kenya recordings are filtered out and the recordings downloaded to the directory created
#### links
1. https://www.xeno-canto.org/
2. https://www.xeno-canto.org/article/153
# Running the scripts
## 1.data.py
```bash
python scraper.py
```
## 2.main.py
```bash
python main.py /your/directory example: python3 main.py /home/daniel/Desktop
```
