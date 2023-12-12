import re
from datetime import date
from typing import Optional

from pydantic import BaseModel, validator

from src.constants.constants import ALPHABETS
from src.schemas.customer_schema import Player
from src.utils.account_utils import check_string_using_regex, to_camel


class PlayerCreate(BaseModel):
    first_name: str
    last_name: str
    dob: Optional[date] = None
    freeze: bool

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("first_name", "last_name")
    def check_name(cls, name):
        name = name.strip()
        if check_string_using_regex(ALPHABETS, name) is None:
            raise ValueError("name type should contain only alphabets")
        name = re.sub(" +", " ", name)
        return name


class PlayerUpdate(Player):
    pass


class PlayerList(BaseModel):
    players: list[PlayerUpdate]
