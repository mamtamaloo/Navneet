import re

from pydantic import BaseModel, EmailStr, validator

from src.constants.constants import ALPHABETS, POSTAL, STREET, USA
from src.utils.account_utils import check_string_using_regex, to_camel


class Addresses(BaseModel):
    street1: str
    street2: str
    city: str
    state: str
    postal: str
    country: str = USA

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("city")
    def check_address_city(cls, city):
        city = city.strip()
        if check_string_using_regex(ALPHABETS, city) is None:
            raise ValueError("city name should be alphabets only")
        city = re.sub(" +", " ", city)
        return city

    @validator("state")
    def check_address_state(cls, state):
        state = state.strip()
        if check_string_using_regex(ALPHABETS, state) is None:
            raise ValueError("state name should be alphabets only")
        state = re.sub(" +", " ", state)
        return state

    @validator("street1", "street2")
    def check_address_street(cls, street):
        street = street.strip()
        if check_string_using_regex(STREET, street) is None:
            raise ValueError("street name should be alphanumeric")
        street = re.sub(" +", " ", street)
        return street

    @validator("postal")
    def check_address_postal(cls, post):
        if check_string_using_regex(POSTAL, post) is None:
            raise ValueError("postal code is not correct")
        return post


class BasicInfo(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    address: Addresses

    @validator("first_name", "last_name")
    def check_name(cls, name):
        name = name.strip()
        if check_string_using_regex(ALPHABETS, name) is None:
            raise ValueError("name type should contain only alphabets")
        name = re.sub(" +", " ", name)
        return name


class DisplayInfo(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    address: Addresses

    @validator("first_name", "last_name")
    def check_name(cls, name):
        name = name.strip()
        if check_string_using_regex(ALPHABETS, name) is None:
            raise ValueError("name type should contain only alphabets")
        name = re.sub(" +", " ", name)
        return name
