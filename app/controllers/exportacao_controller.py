from fastapi import APIRouter, Depends, status, Query
from typing import List, Dict, Union

from services.auth_service import get_current_user
from services.exportacao_service import (
    exportacao_service_vinhos_mesa,
    exportacao_service_espumantes,
    exportacao_service_uvas_frescas,
    exportacao_service_suco_uva
)

router = APIRouter(prefix="/exportacao", tags=["Exportacao"])

# Endpoint para buscar vinhosMesa
@router.get("/vinhosMesa/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return exportacao_service_vinhos_mesa.get_data_by_year(year)


# Endpoint para buscar vinhosMesa
@router.get("/vinhosMesa", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return exportacao_service_vinhos_mesa.get_data_range(ano_inicio, ano_fim)


# Endpoint para buscar espumantes
@router.get("/espumantes/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return exportacao_service_espumantes.get_data_by_year(year)


@router.get("/espumantes", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return exportacao_service_espumantes.get_data_range(ano_inicio, ano_fim)


# Endpoint para buscar uvasFrescas
@router.get("/uvasFrescas/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return exportacao_service_uvas_frescas.get_data_by_year(year)


@router.get("/uvasFrescas", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return exportacao_service_uvas_frescas.get_data_range(ano_inicio, ano_fim)


# Endpoint para buscar uvasPassas
@router.get("/sucoUva/{year}", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_by_year(
    year: int,
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento para um ano específico.
    """
    return exportacao_service_suco_uva.get_data_by_year(year)


@router.get("/sucoUva", response_model=List[Dict[str, Union[str, int, float]]], status_code=status.HTTP_200_OK)
async def get_processamento_range(
    ano_inicio: int = Query(..., ge=1970, le=2025, description="Ano inicial do intervalo"),
    ano_fim: int = Query(..., ge=1970, le=2025, description="Ano final do intervalo"),
    current_user: str = Depends(get_current_user)
):
    """
    Retorna dados de processamento em um intervalo de anos (inclusive).
    """
    return exportacao_service_suco_uva.get_data_range(ano_inicio, ano_fim)

