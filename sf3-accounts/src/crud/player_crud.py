import loguru
from fastapi import status

from src.exception.common_exception import SomethingWentWrongException
from src.exception.customer_exception import CustomerNotExistException
from src.exception.player_exception import (
    PlayerCreationException,
    PlayerNotExistException,
)
from src.schemas import player_schema
from src.utils.account_utils import parse_json


def create_player(player, customer_id):
    try:
        json_file_path = "src/json/list_of_players.json"
        customer_id = customer_id.strip()
        json_data = parse_json(json_file_path)
        for data in json_data:
            if customer_id == data["customerId"]:
                loguru.logger.debug("parent has created successfully")
                headers = {"id": "PL001"}
                temp_dict = {"headers": headers, "status_code": status.HTTP_201_CREATED}
                return temp_dict
    except PlayerCreationException as e:
        loguru.logger.exception(e)
        raise PlayerCreationException(exception=str(e))
    else:
        raise CustomerNotExistException(name=customer_id)


def list_players(customer_id):
    json_file_path = "src/json/list_of_players.json"
    json_data = parse_json(json_file_path)
    temp = []
    for data in json_data:
        temp.append(data["customerId"])
    if customer_id not in temp:
        raise CustomerNotExistException(name=customer_id)

    try:
        player_list = []
        for data in json_data:
            if data["customerId"] == customer_id:
                player = player_schema.PlayerUpdate(
                    id=data["id"],
                    first_name=data["firstName"],
                    last_name=data["lastName"],
                    user_group=data["userGroup"],
                    dob=data["dob"],
                    freeze=data["freeze"],
                )
                player_list.append(player)
        return player_schema.PlayerList(players=player_list)
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))


def update_player(customer_id, player_id):
    temp = []
    json_file_path = "src/json/list_of_players.json"
    json_data = parse_json(json_file_path)
    for data in json_data:
        temp.append(data["customerId"])
    if customer_id not in temp:
        raise CustomerNotExistException(name=customer_id)

    try:
        for data in json_data:
            if data["id"] == player_id and data["customerId"] == customer_id:
                return status.HTTP_200_OK
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise PlayerNotExistException(name=player_id)


def delete_player(customer_id, player_id):
    temp = []
    json_file_path = "src/json/list_of_players.json"
    json_data = parse_json(json_file_path)
    for data in json_data:
        temp.append(data["customerId"])
    if customer_id not in temp:
        raise CustomerNotExistException(name=customer_id)

    try:
        json_file_path = "src/json/list_of_players.json"
        json_data = parse_json(json_file_path)
        for data in json_data:
            if data["id"] == player_id and data["customerId"] == customer_id:
                return status.HTTP_204_NO_CONTENT
    except Exception as e:
        loguru.logger.exception(e)
        raise SomethingWentWrongException(error=str(e))
    else:
        raise PlayerNotExistException(name=player_id)
