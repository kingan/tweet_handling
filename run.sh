#!/usr/bin/env bash

#Ensure proper permissions are set
chmod a+x ./src/tweets_cleaned.py

#Execute python script tweets_cleaned.py with appropriate parameters
python ./src/tweets_cleaned.py ./tweet_input/tweets_cut.txt ./tweet_output/ft1.txt


