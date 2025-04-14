from fastapi import APIRouter, Depends, status, Query
from typing import List, Dict, Union

from services.auth_service import get_current_user
from services.comercializacao_service import comercializacao_service

router = APIRouter()

# ✅ Endpoint para buscar comercializacao por ano
@router.get("/comercializacao/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_comercializacao_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de comercializacao para um ano específico.
    """
    return comercializacao_service.get_data_by_year(year)


# ✅ Endpoint para buscar comercializacao por intervalo de anos
@router.get("/comercializacao", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_comercializacao_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de comercializacao em um intervalo de anos (inclusive).
    """
    return comercializacao_service.get_data_range(ano_inicio, ano_fim)
