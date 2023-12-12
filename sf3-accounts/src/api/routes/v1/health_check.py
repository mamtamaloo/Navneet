from fastapi import APIRouter, status

router = APIRouter(prefix="/accounts/v1")


@router.get("/healthcheck", tags=["Healthcheck"])
def healthcheck():
    return status.HTTP_200_OK
