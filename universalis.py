from pydantic import BaseModel, Field
from typing import List

import requests
import json

class Materia(BaseModel):
    slotID: int | None = Field(alias="slotID", default=None)
    materiaID: int | None = Field(alias="materiaID", default=None)

class MateriaConfiguration(BaseModel):
    slotID: bool = Field(alias="slotID", default=False)
    materiaID: bool = Field(alias="materiaID", default=False)

class History(BaseModel):
    hq: bool | None = Field(alias="hq", default=None)
    pricePerUnit: int | None = Field(alias="pricePerUnit", default=None)
    quantity: int | None = Field(alias="quantity", default=None)
    timestamp: int | None = Field(alias="timestamp", default=None)
    onMannequin: bool | None = Field(alias="onMannequin", default=None)
    worldName: str | None = Field(alias="worldName", default=None)
    worldID: int | None = Field(alias="worldID", default=None)
    buyerName: str | None = Field(alias="buyerName", default=None)
    total: int | None = Field(alias="total", default=None)

class HistoryConfiguration(BaseModel):
    hq: bool = Field(alias="hq", default=False)
    pricePerUnit: bool = Field(alias="pricePerUnit", default=False)
    quantity: bool = Field(alias="quantity", default=False)
    timestamp: bool = Field(alias="timestamp", default=False)
    onMannequin: bool = Field(alias="onMannequin", default=False)
    worldName: bool = Field(alias="worldName", default=False)
    worldID: bool = Field(alias="worldID", default=False)
    buyerName: bool = Field(alias="buyerName", default=False)
    total: bool = Field(alias="total", default=False)

class Listing(BaseModel):
    lastReviewTime: int | None = Field(alias="lastReviewTime", default=None)
    pricePerUnit: int | None = Field(alias="pricePerUnit", default=None)
    quantity: int | None = Field(alias="quantity", default=None)
    stainID: int | None = Field(alias="stainID", default=None)
    worldName: str | None = Field(alias="worldName", default=None)
    worldID: int | None = Field(alias="worldID", default=None)
    creatorName: str | None = Field(alias="creatorName", default=None)
    hq: bool | None = Field(alias="hq", default=None)
    isCrafted: bool | None = Field(alias="isCrafted", default=None)
    listingID: str | None = Field(alias="listingID", default=None)
    materia: List[Materia] | None = Field(alias="materia", default=None)
    onMannequin: bool | None = Field(alias="onMannequin", default=None)
    retainerCity: int | None = Field(alias="retainerCity", default=None)
    retainerID: str | None = Field(alias="retainerID", default=None)
    retainerName: str | None = Field(alias="retainerName", default=None)
    sellerID: str | None = Field(alias="sellerID", default=None)
    total: int | None = Field(alias="total", default=None)
    tax: int | None = Field(alias="tax", default=None)

class ListingConfiguration(BaseModel):
    lastReviewTime: bool = Field(alias="lastReviewTime", default=False)
    pricePerUnit: bool = Field(alias="pricePerUnit", default=False)
    quantity: bool = Field(alias="quantity", default=False)
    stainID: bool = Field(alias="stainID", default=False)
    worldName: bool = Field(alias="worldName", default=False)
    worldID: bool = Field(alias="worldID", default=False)
    creatorName: bool = Field(alias="creatorName", default=False)
    hq: bool = Field(alias="hq", default=False)
    isCrafted: bool = Field(alias="isCrafted", default=False)
    listingID: bool = Field(alias="listingID", default=False)
    materia: bool = Field(alias="materia", default=False)
    materiaConfiguration: bool = Field(alias="materiaConfiguration", default=MateriaConfiguration())
    onMannequin: bool = Field(alias="onMannequin", default=False)
    retainerCity: bool = Field(alias="retainerCity", default=False)
    retainerID: bool = Field(alias="retainerID", default=False)
    retainerName: bool = Field(alias="retainerName", default=False)
    sellerID: bool = Field(alias="sellerID", default=False)
    total: bool = Field(alias="total", default=False)
    tax: bool = Field(alias="tax", default=False)

class MBCurrentResponse(BaseModel):
    itemID: int | None = Field(alias="itemID", default=None)
    #itemIDs: List[int] | None = Field(alias="itemIDs", default=None) implement multiple queries in one later
    worldID: int | None = Field(alias="worldID", default=None)
    lastUploadTime: int | None = Field(alias="lastUploadTime", default=None)
    listings: List[Listing] | None = Field(alias="listings", default=None)
    recentHistory: List[History] | None = Field(alias="recentHistory", default=None)
    regionName: str | None = Field(alias="regionName", default=None)
    dcName: str | None = Field(alias="dcName", default=None)
    currentAveragePrice: float | None = Field(alias="currentAveragePrice", default=None)
    currentAveragePriceNQ: float | None = Field(alias="currentAveragePriceNQ", default=None)
    currentAveragePriceHQ: float | None = Field(alias="currentAveragePriceHQ", default=None)
    regularSaleVelocity: float | None = Field(alias="regularSaleVelocity", default=None)
    nqSaleVelocity: float | None = Field(alias="nqSaleVelocity", default=None)
    hqSaleVelocity: float | None = Field(alias="hqSaleVelocity", default=None)
    averagePrice: float | None = Field(alias="averagePrice", default=None)
    averagePriceNQ: float | None = Field(alias="averagePriceNQ", default=None)
    averagePriceHQ: float | None = Field(alias="averagePriceHQ", default=None)
    minPrice: int | None = Field(alias="minPrice", default=None)
    minPriceNQ: int | None = Field(alias="minPriceNQ", default=None)
    minPriceHQ: int | None = Field(alias="minPriceHQ", default=None)
    maxPrice: int | None = Field(alias="maxPrice", default=None)
    maxPriceNQ: int | None = Field(alias="maxPriceNQ", default=None)
    maxPriceHQ: int | None = Field(alias="maxPriceHQ", default=None)
    stackSizeHistogram: dict | None = Field(alias="stackSizeHistogram", default=None)
    stackSizeHistogramNQ: dict | None = Field(alias="stackSizeHistogramNQ", default=None)
    stackSizeHistogramHQ: dict | None = Field(alias="stackSizeHistogramHQ", default=None)
    worldName: str | None = Field(alias="worldName", default=None)
    worldUploadTimes: dict | None = Field(alias="worldUploadTimes", default=None)
    listingsCount: int | None = Field(alias="listingsCount", default=None)
    recentHistoryCount: int | None = Field(alias="recentHistoryCount", default=None)
    unitsForSale: int | None = Field(alias="unitsForSale", default=None)
    unitsSold: int | None = Field(alias="unitsSold", default=None)

class MBCurrentConfiguration(BaseModel):
    itemID: bool = Field(alias="itemID", default=False)
    worldID: bool = Field(alias="worldID", default=False)
    lastUploadTime: bool = Field(alias="lastUploadTime", default=False)
    listings: bool = Field(alias="listings", default=False)
    listingConfiguration: ListingConfiguration = Field(alias="listingConfiguration", default=ListingConfiguration())
    listingQuantity: int | None = Field(alias="listingQuantity", default=None)
    recentHistory: bool = Field(alias="recentHistory", default=False)
    historyConfiguration: HistoryConfiguration = Field(alias="historyConfiguration", default=HistoryConfiguration())
    historyQuantity: int | None = Field(alias="historyQuantity", default=None)
    regionName: bool = Field(alias="regionName", default=False)
    dcName: bool = Field(alias="dcName", default=False)
    currentAveragePrice: bool = Field(alias="currentAveragePrice", default=False)
    currentAveragePriceNQ: bool = Field(alias="currentAveragePriceNQ", default=False)
    currentAveragePriceHQ: bool = Field(alias="currentAveragePriceHQ", default=False)
    regularSaleVelocity: bool = Field(alias="regularSaleVelocity", default=False)
    nqSaleVelocity: bool = Field(alias="nqSaleVelocity", default=False)
    hqSaleVelocity: bool = Field(alias="hqSaleVelocity", default=False)
    averagePrice: bool = Field(alias="averagePrice", default=False)
    averagePriceNQ: bool = Field(alias="averagePriceNQ", default=False)
    averagePriceHQ: bool = Field(alias="averagePriceHQ", default=False)
    minPrice: bool = Field(alias="minPrice", default=False)
    minPriceNQ: bool = Field(alias="minPriceNQ", default=False)
    minPriceHQ: bool = Field(alias="minPriceHQ", default=False)
    maxPrice: bool = Field(alias="maxPrice", default=False)
    maxPriceNQ: bool = Field(alias="maxPriceNQ", default=False)
    maxPriceHQ: bool = Field(alias="maxPriceHQ", default=False)
    stackSizeHistogram: bool = Field(alias="stackSizeHistogram", default=False)
    stackSizeHistogramNQ: bool = Field(alias="stackSizeHistogramNQ", default=False)
    stackSizeHistogramHQ: bool = Field(alias="stackSizeHistogramHQ", default=False)
    worldName: bool = Field(alias="worldName", default=False)
    worldUploadTimes: bool = Field(alias="worldUploadTimes", default=False)
    listingsCount: bool = Field(alias="listingsCount", default=False)
    recentHistoryCount: bool = Field(alias="recentHistoryCount", default=False)
    unitsForSale: bool = Field(alias="unitsForSale", default=False)
    unitsSold: bool = Field(alias="unitsSold", default=False)

    def get_filter_string(self):
        filters = [field_name for field_name in self.__annotations__.keys() if getattr(self, field_name) == True]
        listing_filters = [f"listings.{field_name}" for field_name in self.listingConfiguration.__annotations__.keys() if getattr(self.listingConfiguration, field_name) == True]
        materia_filters = [f"listings.materia.{field_name}" for field_name in self.listingConfiguration.materiaConfiguration.__annotations__.keys() if getattr(self.listingConfiguration.materiaConfiguration, field_name) == True]
        history_filters = [f"recentHistory.{field_name}" for field_name in self.historyConfiguration.__annotations__.keys() if getattr(self.historyConfiguration, field_name) == True]
        return ','.join(filters + listing_filters + materia_filters + history_filters)

def query_mb_current(itemID: int, worldDcRegion: str,
                     config: MBCurrentConfiguration = MBCurrentConfiguration()) -> MBCurrentResponse | None:
    request = f"https://universalis.app/api/v2/{worldDcRegion}/{itemID}?"
    query = ""
    if config.listingQuantity != None:
        query += f"listings={config.listingQuantity}&"
    if config.historyQuantity != None:
        query += f"entries={config.historyQuantity}&"
    query += f"fields={config.get_filter_string()}"
    
    request += query

    response = requests.get(request)

    return MBCurrentResponse(**json.loads(response.content))
