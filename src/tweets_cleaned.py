#Import the necessary libraries
import os, subprocess, sys
import json

#Open tweets.txt and handle.
def my_fun():
    f = open(sys.argv[1],'r')
    out = (f.read()).split("\n")
    f.close()
    #Remove trailing null string.
    out = out[:-1]
    #Convert to dictionary and extract the meaningful data
    clean_tweet = map((lambda x:(json.loads(x))['text'] + " (timestamp: " + (json.loads(x))['created_at'] + ")"),out)
    clean_tweet = map(uniDet,clean_tweet)
    return clean_tweet

#Detect strings with unicode characters and account for them
def uniDet(i):
    global count
    try:
        uniDeto = i.encode("ascii")
    except UnicodeEncodeError:
        uniDeto= i.encode("ascii","ignore")
        count +=1
    return uniDeto,count

#Set the global count to 0
count = 0
foutput = my_fun()

#Reduce output down to a single string which allows for a single write to disk.
binput = reduce((lambda x,y:x+y),map((lambda x:x[0]+'\n'),foutput))

#Append unicode tweet count
final_output = binput +"\n\n" + str(foutput[-1][-1]) + " tweets contained unicode."


#Output to the specified file
out = open(sys.argv[2], 'w')
out.write(final_output)
out.close()
