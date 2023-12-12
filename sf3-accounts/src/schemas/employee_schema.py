import re
from datetime import date, time
from enum import Enum
from typing import List, Optional, Text

from pydantic import BaseModel, validator

from src.constants.constants import ALPHABETS, CONTACT
from src.schemas.common_schema import BasicInfo, DisplayInfo
from src.utils.account_utils import check_string_using_regex, to_camel


class Day(str, Enum):
    SUN = "SUNDAY"
    MON = "MONDAY"
    TUES = "TUESDAY"
    WED = "WEDNESDAY"
    THURS = "THURSDAY"
    FRI = "FRIDAY"
    SAT = "SATURDAY"


class Employee_role(str, Enum):
    TRAINER = "TRAINER"


class Work_Status(str, Enum):
    SCHEDULED = "SCHEDULED"
    UNSCHEDULED = "UNSCHEDULED"


class Availabilities(BaseModel):
    start_time: time
    end_time: time
    location: str

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("location")
    def check_location(cls, location):
        location = location.strip()
        if check_string_using_regex(ALPHABETS, location) is None:
            raise ValueError("location type should contain only alphabets")
        location = re.sub(" +", " ", location)
        return location


class WorkingHours(BaseModel):
    day: Day
    status: Work_Status
    availabilities: Optional[List[Availabilities]] = None

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class Status(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Gender(str, Enum):
    OTHERS = ""
    MALE = "MALE"
    FEMALE = "FEMALE"


class PrimaryContact(BaseModel):
    number: Optional[str]
    notifications: bool

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("number")
    def check_primary_phone_number(cls, phone):
        if check_string_using_regex(CONTACT, phone) is None:
            raise ValueError("phone number should be USA format  only")
        return phone


class SecondaryContact(BaseModel):
    number: str
    notifications: bool

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("number")
    def check_secondary_phone_number(cls, phone):
        if not re.match(r"^$|^(\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$", phone):
            raise ValueError("phone number should be in USA format only")
        return phone


class Contact(BaseModel):
    primary: PrimaryContact
    secondary: SecondaryContact

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class EmployeeCreate(BasicInfo):
    user_group: Employee_role
    email_notifications: bool
    contact: Contact
    profilePhotoS3Url: str
    gender: Gender
    description: Text
    experience: str
    start_date: date
    rate: float
    status: Status
    locations: list
    services: list
    working_hours: List[WorkingHours]

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("description")
    def check_description(cls, description):
        description = description.strip()
        if check_string_using_regex(ALPHABETS, description) is None:
            raise ValueError(
                "description type should contain alphabets and spaces only"
            )
        description = re.sub(" +", " ", description)
        return description


class EmployeeListSchema(DisplayInfo):
    primary_contact_number: str
    creation_date: date
    status: Status

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

    @validator("primary_contact_number")
    def check_primary_phone_number(cls, phone):
        if check_string_using_regex(CONTACT, phone) is None:
            raise ValueError("phone number should be USA format  only")
        return phone


class UpdateEmployee(EmployeeCreate, DisplayInfo):
    pass


# class EmployeeUpdate(BaseModel):
#     pass


class EmployeeList(BaseModel):
    employee: list
