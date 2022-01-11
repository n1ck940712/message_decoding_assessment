# Decoding Message Assessment for MAX 1938 (Application Developer - Intermediate)


Completed by Nick Hoo on 11 January 2022.

# How to get it running
- Clone to directory from GitHub repo https://github.com/n1ck940712/message_decoding_assessment
- Below is the exact lines of code for me to get it running on a fresh machine
```
cd ~

git clone https://github.com/n1ck940712/message_decoding_assessment message_decode

cd message_decode

virtualenv -p python3 env

source env/bin/activate 

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```
- Visit localhost:8000/


# Specifications

Function for the message decoding can be found inside /app/views.py

 - Framework: Django 
 - platform: Ubuntu 20.04 
