# Enter Discord Webhook here

webhook = "" 

# Colors

FAIL = '\033[91m'
ENDC = '\033[0m'

ERROR = FAIL +"Error: "+ENDC

if webhook == '':
    print(ERROR+"Webhook empty\nAdd Discord Webhook in ./discord.py")
    exit()

import requests

def SendDisc(imgs):
    try:
        for i in imgs:
            payload = { 'content' : i } 
            try:
                r = requests.post(webhook, json=payload )
                print(i,'Status code:',r.status_code)
            except:
                print(ERROR+"Getting Image, Status code:",r.status_code)
    except Exception as e:
        print(ERROR+e.__class__)
