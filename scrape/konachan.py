from scrape.api import gelapi

def konachan(limit,tags):
    tags = tags.split(',')
    
    blacklisted = ['loli','guro'] #Enter Blacklisted tags

    tags = "+".join(tags) + '+order:random+-' + "+-".join(blacklisted) 


    payload = {
        "limit": limit,
        "tags": tags
    }
    url = "https://konachan.net/post.json"
    
    return gelapi(url,payload,limit)
