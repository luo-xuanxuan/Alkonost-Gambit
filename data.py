from pydantic import BaseModel, Field

class Gambit(BaseModel):
    item_buy: str = Field(alias="item_buy")
    ratio: int = Field(alias="ratio")
    item_sell: str = Field(alias="item_sell")
    time_checked: float = Field(default=0)