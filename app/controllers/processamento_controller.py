from fastapi import APIRouter, Depends, status, Query
from typing import List, Dict, Union

from services.auth_service import get_current_user
from services.processamento_service import (
    processamento_service_viniferas, 
    processamento_service_americanas, 
    processamento_service_uvas
    )

router = APIRouter(prefix="/processamento", tags=["Processamento"])

# Endpoint para buscar viniferas
@router.get("/viniferas/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return processamento_service_viniferas.get_data_by_year(year)


# Endpoint para buscar viniferas
@router.get("/viniferas", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return processamento_service_viniferas.get_data_range(ano_inicio, ano_fim)


# Endpoint para buscar americanas
@router.get("/americanas/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return processamento_service_americanas.get_data_by_year(year)


# Endpoint para buscar americanas
@router.get("/americanas", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return processamento_service_americanas.get_data_range(ano_inicio, ano_fim)


# Endpoint para buscar Uvas
@router.get("/uvas/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return processamento_service_uvas.get_data_by_year(year)


# Endpoint para buscar Uvas
@router.get("/uvas", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return processamento_service_uvas.get_data_range(ano_inicio, ano_fim)

