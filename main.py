import pyjson5
import settings
import data
import time
from typing import List

import universalis
import discord_webhook

local_settings = settings.get_settings()

def load_gambits() -> List[data.Gambit]:
    gambits: List[data.Gambit]
    with open('gambits.jsonc', 'r') as f:
        json_gambits = pyjson5.load(f)
        gambits = [data.Gambit(**item) for item in json_gambits]
    return gambits

if __name__ == '__main__':
    gambits = load_gambits()

    sellConfig = universalis.MBCurrentConfiguration(listingConfiguration=universalis.ListingConfiguration(pricePerUnit=True),
                                                    minPrice=True)
    
    buyConfig = universalis.MBCurrentConfiguration(listingConfiguration=universalis.ListingConfiguration(pricePerUnit=True,
                                                                                                         quantity=True,
                                                                                                         worldName=True,
                                                                                                         retainerName=True))

    while True:
        for gambit in gambits:
            if gambit.time_checked > time.time() - local_settings.cooldown:
                continue

            sellPrice = universalis.query_mb_current(itemID=gambit.item_sell,
                                                     worldDcRegion=local_settings.home_world,
                                                     config=sellConfig).minPrice
            
            listings = universalis.query_mb_current(itemID=gambit.item_buy, worldDcRegion="North-America", config=buyConfig).listings

            buyList: List[universalis.Listing] = [listing for listing in listings
                                                  if listing.pricePerUnit <= sellPrice / gambit.ratio]
            if buyList != []:
                discord_webhook.post_webhook(local_settings.webhook_url, gambit, sellPrice, buyList)
                gambit.time_checked = time.time()

        time.sleep(local_settings.query_frequency)