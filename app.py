import sys
import argparse
import requests

from scrape.gelbooru import gelbooru
from scrape.konachan import konachan
from scrape.rule34 import rule34
from discord import SendDisc

if __name__=="__main__":
   
        parser = argparse.ArgumentParser(description='Scrapes Imageboard for Discord webhook')

        parser.add_argument('--site','-s',type=str,metavar='',help="Sites : gelbooru[default],rule34,konachan")
        parser.add_argument('--tags','-t',type=str,metavar='',required=True,help="tag(comma seperated): '1girl,1boy'")
        parser.add_argument('--count','-c',type=int,metavar='',required=True,help="count: Images to scrape")

        args = parser.parse_args()  # Gets Args
       
        if args.site == "konachan":
            imgs = konachan(args.count,args.tags) # Gets Images
        elif args.site == 'rule34':
            imgs = rule34(args.count,args.tags) # Gets Images
        else:
            imgs = gelbooru(args.count,args.tags) # Gets Images

        
        SendDisc(imgs)  # Sends Images


