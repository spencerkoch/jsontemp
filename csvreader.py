#!/usr/bin/python
import csv
import urllib

url  = "http://api.thingspeak.com/channels/15486/feed.csv?key=1X5610SMHNUIF9XL"
response = urllib.urlopen(url)
cr = csv.reader(response)







rows=list(cr)
row0=rows[0]
row1=rows[1]
print row1[2]
print float(row1[2])
print "Current temp is %d degrees." % (float(row1[2]))
print "Current temp is " + row1[2] + " degrees."




