
from Adafruit_IO import Client, RequestError, Feed
import os
import webbrowser
import urllib.request as url
ADAFRUIT_IO_KEY = '383967b959ef4f67946904bc0eff15d3'

ADAFRUIT_IO_USERNAME = 'amirkhan1092'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    foo = aio.feeds('apt')
except RequestError: # Doesn't exist, create a new feed
    feed = Feed(name="apt")
    foo = aio.create_feed(feed)


# Send a string value 'bar' to the feed 'Foo'.
aio.send_data(foo.key, 'O')

flag=''
while 1:
  
    data = aio.receive(foo.key)
    data=data.value
    if not flag==data:
        print(data)
        if data=='songmp':
            os.startfile('Most.mp4')
        elif data=='songmpstop':
            os.system('TASKKILL /F /IM vlc.exe')
        elif data=='opennote':
            os.startfile('notepad.exe')
        elif data=='closenote':
            os.system('TASKKILL /F /IM notepad.exe')
        elif data=='openiot':    
            webbrowser.open('http://amkr.co.nf') # Go to example.com
        elif data=='closeiot':    
            os.system('TASKKILL /F /IM chrome.exe')    
        elif data=='ON':
            url.urlopen('http://amkr.co.nf/my_data_write.php?a_data=on')
        elif data=='OFF':
            url.urlopen('http://amkr.co.nf/my_data_write.php?a_data=off')
        elif data=='shutlap':    
            os.system("shutdown /r /t 1");   
            
        flag=data



