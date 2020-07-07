# DSAIL-Programming-challenge
## Background
## Tasks
<img src="https://github.com/DanNduati/DSAIL-Programming-challenge/blob/master/challenge.png" width="400">

## Task 1
## duration.py script

## tinytag module
tinytag is a library for reading music meta data of MP3, OGG, OPUS, MP4, M4A, FLAC, WMA and Wave files with python

[![Build Status](https://travis-ci.org/devsnd/tinytag.png?branch=master)](https://travis-ci.org/devsnd/tinytag)
[![Build status](https://ci.appveyor.com/api/projects/status/w9y2kg97869g1edj?svg=true)](https://ci.appveyor.com/project/devsnd/tinytag)
[![Coverage Status](https://coveralls.io/repos/devsnd/tinytag/badge.png)](https://coveralls.io/r/devsnd/tinytag)

Install
-------

```pip install tinytag```

## Expected Output
<img src="https://github.com/DanNduati/DSAIL-Programming-challenge/blob/master/duration.png" width="600">

## Task 2
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
python data.py
```
## 2.main.py
```bash
python main.py /your/directory example: python3 main.py /home/daniel/Desktop
```
## Expected Output
<img src="https://github.com/DanNduati/DSAIL-Programming-challenge/blob/master/output.png" width="450">
<img src="https://github.com/DanNduati/DSAIL-Programming-challenge/blob/master/dir.png" width="450">
