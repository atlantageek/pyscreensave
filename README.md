pyscreensave

A simple project to display some images on your TV/Home Theatre system.  
Pair this with the excellent bluetooth rpi speaker and a few images from deviantart. Great for a chillout space.


* Install Raspbian PI OS Lite on a raspberry pi
* checkout this repo
* Grab your favorite images and drop them in /home/pi/images directory on the pi
* Add to crontab.  In my /etc/crontab file I have the line:
** * * * * * root python /home/pi/screensave/screensave.py



