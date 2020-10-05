from typing import List

from fastapi import APIRouter

from server.schemas import cerveja_schema
from server.services.cerveja_service import CervejaService

router = APIRouter()

cerveja_service = CervejaService()


@router.get("/cervejas", response_model=List[cerveja_schema.Cerveja], tags=["cervejas"])
def read_cervejas():
    cervejas = cerveja_service.get_cervejas()
    return cervejas


@router.post("/cervejas", response_model=cerveja_schema.Cerveja, tags=["cervejas"])
def create_cerveja(cerveja: cerveja_schema.CervejaCreate):
    cerveja = cerveja_service.create_cerveja(cerveja)
    return cerveja
