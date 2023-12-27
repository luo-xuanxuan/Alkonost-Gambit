import pyjson5
from typing import List
from pydantic import BaseModel, Field

class Settings(BaseModel):
    webhook_url: str = Field(alias="webhook_url")
    home_world: str = Field(alias="home_world")
    query_frequency: int = Field(alias="query_frequency")
    cooldown: int = Field(alias="cooldown")

settings: Settings

def get_settings() -> Settings:
    return settings

def load_settings():
    global settings
    with open('settings.jsonc', 'r') as f:
        settings = Settings(**pyjson5.load(f))

load_settings()