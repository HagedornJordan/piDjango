# piDjango
Quickstart for running a Django server on a Raspberry Pi. Includes GPIO.

## Getting Started
I was using Ubuntu Server 21.04 for development. Python3 was already installed, but if this is not the case for you you'll need to install it. 

1. Clone this repo  
`git clone https://github.com/HagedornJordan/piDjango`
2. Install dependencies.  
`sudo apt-get update`  
`sudo apt-get install python3-venv`
3. Create your python virtual environment and activate it.
`cd piDjango`  
`python3 -m venv env`  
`source env/bin/activate`  
4. This step may not be necessary, but I couldn't install RPi.GPIO without it!  
`export CFLAGS=-fcommon`
5. Install the PIP dependencies  
`pip install requirements.txt`  
6. Generate a secret key.  
`echo -n "SECRET_KEY=" > .env`  
`python3 -c 'import secrets; print(secrets.token_hex(100))' >> .env`  
7. Migrate your database  
`python manage.py migrate`  
8. Run the server. Note, to access from other machines, you'll want to add your pi's IP to your list of `ALLOWED_HOSTS` (example: ALLOWED_HOSTS=['192.168.88.231',])  
`python mangage.py runserver 0.0.0.0:8000` 
9. Test it out. Copy the wiring example below. In a browser (within the same network) send the request `http://192.168.88.231:8000/blink/?pin=23&blinks=5&pause=.25` Your LED connected to pin 23 should blink 5 times with a .25 second delay. 


## Wiring example for blink.py
Note that blue is ground, and green is the pin you want blink.py to use. I used pin 23. To find a pinout diagram, just Google `Rpi.GPIO pinout for Raspberry pi <your_revision>` 
![IMG_20210927_231336980](https://user-images.githubusercontent.com/60068272/135017034-85df56d9-ec6b-43a3-96b6-e74554e8bc3a.jpg)
