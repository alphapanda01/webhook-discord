from scrape.api import gelapi

# Add your gelbooru api

api_key = 'anonymous'
user_id = '9455'


# Convert the input text into Api Format
def gelbooru(limit,tags):
    
    tags = tags.split(',')

    blacklisted = ['loli','guro'] #Enter Blacklisted tags here

    tags = "+".join(tags) + '+sort:random+-' + "+-".join(blacklisted)

    payload = {
        "api_key": api_key,
        "user_id": user_id,
        "page":"dapi",
        "s":"post",
        "q":"index",
        "limit":limit * 3,
        "tags":tags,
        "json":1 
    }  

    url = "https://gelbooru.com/index.php"
    
    return gelapi(url,payload,limit)  # Scrape Images From api

