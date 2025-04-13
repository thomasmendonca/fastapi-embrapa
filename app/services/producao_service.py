import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException, Query
from typing import List, Dict
from functools import lru_cache

class ProducaoService:
    def __init__(self):
        self.BASE_URL = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'

    def _limpar_numero(self, valor: str) -> float:
        """
        Limpa string numérica brasileira (ex: '1.234.567,89') e converte para float.
        """
        try:
            return float(valor.replace('.', '').replace(',', '.'))
        except ValueError:
            return 0.0

    @lru_cache(maxsize=100)
    def _scrape_ano(self, ano: int) -> List[Dict[str, str]]:
        """Realiza scraping dos dados do site para um ano específico"""
        url = f'{self.BASE_URL}&ano={ano}'
        response = requests.get(url)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao acessar a página para o ano {ano}. Status code: {response.status_code}"
            )

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})

        if not table:
            raise HTTPException(
                status_code=404,
                detail=f"Tabela de produção não encontrada para o ano {ano}"
            )

        data = []
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if cols:
                produto = cols[0].get_text(strip=True)
                quantidade_str = cols[1].get_text(strip=True)
                quantidade_float = self._limpar_numero(quantidade_str)

                data.append({
                    'ano': ano,
                    'produto': produto,
                    'producao_litros': quantidade_float
                })
        return data

    def get_producao_by_year(self, ano: int = Query(..., description="Ano para filtrar (ex: 2002)", ge=1970, le=2025)) -> List[Dict[str, str]]:
        """
        Realiza o scraping e retorna os dados de produção para o ano informado.
        """
        return self._scrape_ano(ano)

    def get_producao_range(self, ano_inicio: int, ano_fim: int) -> List[Dict[str, str]]:
        """
        Retorna dados de produção de um intervalo de anos (inclusive).
        """
        if ano_inicio > ano_fim:
            raise HTTPException(
                status_code=400,
                detail="Ano inicial deve ser menor ou igual ao ano final"
            )
        
        all_data = []
        for ano in range(ano_inicio, ano_fim + 1):
            all_data.extend(self._scrape_ano(ano))
        
        return all_data


# Instância global
producao_service = ProducaoService()
