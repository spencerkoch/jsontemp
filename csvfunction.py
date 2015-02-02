#!/usr/bin/python
import csv
import urllib

import time
import ImageDraw
from PIL import Image
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix


matrix = Adafruit_RGBmatrix(32, 1)
font = ImageFont.load("10x20.pil")
url  = "http://api.thingspeak.com/channels/15486/feed.csv?key=1X5610SMHNUIF9XL"
def gettemp(url):
    response = urllib.urlopen(url)
    cr = csv.reader(response)
    rows=list(cr)
    row1=rows[100]
    return row1[2]

#print "Current temp is " + gettemp(url)  +" degrees."
count = 0
while (count < 100):
    image = Image.new("RGB", (512, 32), (0,0,0))
    red = (255,0,0)
    draw = ImageDraw.Draw(image)
    drawstring =  "Current temp is " + gettemp(url)  +" degrees."
    draw.text((0,0), drawstring, font=font, fill=red)
    for n in range(32, -image.size[0], -1): # Scroll R to L
            matrix.SetImage(image.im.id, n, 0)
            time.sleep(0.025)
    matrix.Clear()
    time.sleep(20)

