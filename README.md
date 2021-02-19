# Imageboard Scraper for Discord Webhook

> Scrapes Images from imageboards and sends them to discord

## TO DO by user

- add discord webhook in ./discord.py
- optional:
  - Edit Default tags in scrape/{gelbooru.py|konachan.py|rule34.py}




## Working of Program (e.g. if site = gelbooru)
- User Inputs Site Tags And Count as cli args
- `argparse` parses the args 
- These Parsed args are sent to `gelbooru` function in scrape/gelbooru.py
- `gelbooru()` Converts these agrs into payload for api
- It calls the `gelapi()` in scrape/api.py
- `gelapi()` gets images from api and returns it to the app.py
- Then app.py calls `SendDisc()` from ./discord.py 
- `SendDisc()` Sends these images to Discord Via a webhook 
