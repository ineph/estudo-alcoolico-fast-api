from typing import List

from fastapi import APIRouter

from server.schemas import cerveja_schema
from server.services.cerveja_service import CervejaService
from fastapi import HTTPException

router = APIRouter()

cerveja_service = CervejaService()


@router.get("/cervejas", response_model=List[cerveja_schema.Cerveja], tags=["cervejas"])
def read_cervejas():
    cervejas = cerveja_service.get_cervejas()
    return cervejas


@router.get("/cerveja/{cerveja_id}", response_model=cerveja_schema.Cerveja, tags=["cervejas"])
def get_cerveja_by_id(cerveja_id):
    cerveja = cerveja_service.get_cerveja_by_id(cerveja_id)
    return cerveja


@router.post("/cervejas", response_model=cerveja_schema.Cerveja, tags=["cervejas"])
def create_cerveja(cerveja: cerveja_schema.CervejaCreate):
    cerveja = cerveja_service.create_cerveja(cerveja)
    return cerveja


@router.delete("/cerveja/{cerveja_id}", status_code=201, tags=["cervejas"])
def delete_cerveja(cerveja_id: int):
    cerveja = cerveja_service.delete_cerveja(cerveja_id)
    return cerveja
