from fastapi import APIRouter, Depends, status, Query
from typing import List, Dict, Union

from services.auth_service import get_current_user
from services.producao_service import producao_service

router = APIRouter()

# ✅ Endpoint para buscar produção por ano
@router.get("/producao/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_producao_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de produção para um ano específico.
    """
    return producao_service.get_producao_by_year(year)


# ✅ Endpoint para buscar produção por intervalo de anos
@router.get("/producao", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_producao_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de produção em um intervalo de anos (inclusive).
    """
    return producao_service.get_producao_range(ano_inicio, ano_fim)
