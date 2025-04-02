
from fastapi import APIRouter, Depends, status
from typing import List, Dict, Union

from services.auth_service import get_current_user
from services.producao_service import producao_service

router = APIRouter()

# Endpoint GET para obter dados de produção
@router.get("/producao", response_model=List[Dict[str, str]], status_code=status.HTTP_200_OK)
async def get_producao(current_user: str = Depends(get_current_user)):
    """Endpoint for get production data."""
    # Retorna dados do serviço de produção, após validação do usuário autenticado
    return producao_service.get_producao()

@router.get("/producao/{year}", response_model=List[Dict[str, Union[str, int]]], status_code=status.HTTP_200_OK)
async def get_producao_by_year(year):
    """Endpoint for get production data by year"""
    # Retorna dados do serviço de produção, após validação do usuário autenticado
    return producao_service.get_producao_by_year(year)