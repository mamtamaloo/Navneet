import re
from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr, validator

from src.constants.constants import ALPHABETS, CONTACT
from src.schemas.common_schema import BasicInfo, DisplayInfo
from src.utils.account_utils import check_string_using_regex, to_camel


class Parent_role(str, Enum):
    PARENT = "PARENT"


class Player(BaseModel):
    id: str = "PL001"
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


class CustomerCreate(BasicInfo):
    user_group: Parent_role
    phone_number: str
    players: Optional[List[Player]] = None

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("phone_number")
    def phone_validation(cls, phone):
        if check_string_using_regex(CONTACT, phone) is None:
            raise ValueError("phone number should be USA format  only")
        return phone


class Frequency(str, Enum):
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    DAILY = "DAILY"


class Membership(BaseModel):
    name: str
    cost: float
    frequency: Frequency


class CustomerPlayerList(BaseModel):
    id: str = "PL001"
    first_name: str
    last_name: str
    membership_details: Membership
    freeze: bool

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class GetCustomer(DisplayInfo):
    user_group: Parent_role
    phone_number: str
    players: List[Player]

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("phone_number")
    def phone_validation(cls, phone):
        if check_string_using_regex(CONTACT, phone) is None:
            raise ValueError("phone number should be USA format  only")
        return phone


class UpdateCustomer(GetCustomer):
    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class AllCustomers(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    players: List[CustomerPlayerList]

    @validator("first_name", "last_name")
    def check_name(cls, name):
        name = name.strip()
        if check_string_using_regex(ALPHABETS, name) is None:
            raise ValueError("name type should contain only alphabets")
        name = re.sub(" +", " ", name)
        return name

    @validator("phone_number")
    def phone_validation(cls, phone):
        if check_string_using_regex(CONTACT, phone) is None:
            raise ValueError("phone number should be USA format  only")
        return phone


class ListAllCustomers(BaseModel):
    customers: List[AllCustomers]
