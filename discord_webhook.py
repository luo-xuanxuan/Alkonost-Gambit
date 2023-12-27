from typing import List
from universalis import Listing

import requests
import data
import discord
import json

def post_webhook(webhook_url: str, gambit: data.Gambit, sellPrice: int ,buyList: List[Listing]):
    buy_name: str = json.loads(requests.get(f"https://xivapi.com/search?indexes=Item&filters=ID={gambit.item_buy}").content)["Results"][0]["Name"]
    sell_name: str = json.loads(requests.get(f"https://xivapi.com/search?indexes=Item&filters=ID={gambit.item_sell}").content)["Results"][0]["Name"]

    embed = discord.Embed(title=f"{buy_name} Gambit")
    embed.set_thumbnail(url=f"https://raw.githubusercontent.com/luo-xuanxuan/icons/main/{gambit.item_buy}.png")
    
    worlds = {}
    cost = 0
    quantity = 0

    for listing in buyList:
        cost += listing.pricePerUnit * listing.quantity
        quantity += listing.quantity
        if listing.worldName in worlds.keys():
            worlds[listing.worldName].append(listing)
            continue
        worlds[listing.worldName] = [listing]

    cost *= 1.05 #tax

    for world, listings in worlds.items():
        value = ""
        for listing in listings:
            value += f"{(int((listing.pricePerUnit*1.05))):,}g | {listing.retainerName}\n"
        embed.add_field(name=world, value=value, inline=True)

    embed.description = f"Current {sell_name} value: **{sellPrice:,}g**\nTotal Cost of available gambits: **{int(cost):,}g**\nQuantity of gambits: **{quantity}**\nRatio is set to {gambit.ratio} {buy_name} to 1 {sell_name}"

    dictionary_embed = embed.to_dict()

    dictionary_embed.pop("type")

    request = "{\"embeds\":[" + json.dumps(dictionary_embed) + "]}"

    response = requests.post(url=webhook_url, data=request, headers={'Content-Type': 'application/json'})