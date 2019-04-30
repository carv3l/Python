from __future__ import print_function
import psutil
import subprocess
import httplib, urllib
import thingspeak
import time
import re


sleep = 1 # how many seconds to sleep between posts to the channel
key = '3XB0VKZ00XNW0R9T'  # Thingspeak channel to update

#Report Raspberry Pi internal temperature to Thingspeak Channel
def cpu_measure():
    while True:
        
        cpu_load = psutil.cpu_percent(interval=1)

       # raw_memory_load = psutil.virtual_memory()
       # optimized_memory_read = str(raw_memory_load)
   
  #      memory_read_extract = re.search('percent=(.+?)used', optimized_memory_read)
   #     if memory_read_extract:
    #        memory_measure = memory_read_extract.group(1)
     #       memory_measure = memory_measure.replace(",","")

    #    params = urllib.urlencode({'field1': cpu_load,'key': key } ) 
    #    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            print (cpu_load)
            data = response.read()
            conn.close()
        except:
            print("Connection failed")
        break
if __name__ == "__main__":
        while True:
                cpu_measure()
