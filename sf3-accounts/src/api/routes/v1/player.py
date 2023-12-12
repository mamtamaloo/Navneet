from fastapi import APIRouter, Response
from starlette import status

from src.crud import player_crud
from src.schemas.player_schema import PlayerCreate, PlayerUpdate

router = APIRouter(prefix="/accounts/v1/customers/{customer_id}/players")
emp = []


@router.post("", tags=["Players"], status_code=status.HTTP_201_CREATED)
async def create_player(player: PlayerCreate, customer_id: str):
    player_dict = player_crud.create_player(player, customer_id)
    if player_dict["status_code"] == status.HTTP_201_CREATED:
        return Response(
            status_code=status.HTTP_201_CREATED, headers=player_dict["headers"]
        )


@router.get("", tags=["Players"], status_code=status.HTTP_200_OK)
async def list_players(customer_id: str):
    return player_crud.list_players(customer_id)


@router.delete("/{player_id}", tags=["Players"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(customer_id: str, player_id):
    player_status = player_crud.delete_player(customer_id, player_id)
    if player_status:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{player_id}", tags=["Players"], status_code=status.HTTP_200_OK)
async def update_player(player: PlayerUpdate, customer_id: str, player_id: str):
    player_status = player_crud.update_player(customer_id, player_id)
    if player_status == status.HTTP_200_OK:
        return Response(status_code=status.HTTP_200_OK)
