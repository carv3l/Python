import psutil 
import urllib2 
while(True):
     f = urllib2.urlopen('http://api.thingspeak.com/update?api_key=3XB0VKZ00XNW0R9T&field1=' +str(psutil.cpu_percent()))
     f.read()
     f.close()
