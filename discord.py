import requests
from time import sleep

# Enter Discord webhook Url here

webhook = ""

# Colors

FAIL = '\033[91m'
ENDC = '\033[0m'

ERROR = FAIL +"Error: "+ENDC

if webhook == '':
    print(ERROR+"Webhook empty\nAdd Discord Webhook in ./discord.py")
    exit()


def SendDisc(imgs,ver):
    sent = 0
    failed = 0
    try:
        for i in imgs:
            payload = { 'content' : i } 
            try:
                r = requests.post(webhook, json=payload )
                if r.status_code == 204:
                    sent += 1
                else:
                    failed += 1
                if ver == True:
                    print(i,'Status code:',r.status_code)
                print(f"Sent: {sent}, Failed: {failed}\r",end="")
                sleep(0.5)
            except:
                print(ERROR+"Getting Image, Status code:",r.status_code)
    except Exception as e:
        print(ERROR+e.__class__)
    # To print the final send and failed values
    print(f"Sent: {sent}, Failed: {failed}")
