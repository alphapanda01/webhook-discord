from scrape.api import gelapi
from random import randint


def rule34(limit,tags):

    rand = 'score:>='+str(randint(0,200)) # To get random images with help of score

    tags = tags.split(',')
    
    blacklisted = ['loli*','guro*','furry*'] # Enter Blacklisted tags here
    
    tags = "+".join(tags) + '+' + rand + '+-' + "+-".join(blacklisted) 

    payload = {
        "page":"dapi",
        "s":"post",
        "q":"index",
        "limit":limit * 10,
        "tags":tags,
        "json":1 
        }

    url = "https://rule34.xxx/index.php"

    return gelapi(url,payload,limit)


