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
9. Run the server. Note, to access from other machines, you'll want to add your pi's IP to your list of `ALLOWED_HOSTS`  
`python mangage.py runserver 0.0.0.0:8000` 
