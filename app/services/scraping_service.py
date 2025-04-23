import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
from typing import List, Dict, Any
from functools import lru_cache

class ScrapingService:
    def __init__(self, url_param: str):
        """
        Serviço de scraping genérico para o site VitiBrasil.
        
        Args:
            url_param: Parâmetro da URL que identifica a página (ex: 'opt_02' para produção)
        """
        self.BASE_URL = f'http://vitibrasil.cnpuv.embrapa.br/index.php?{url_param}'

    def _limpar_valor(self, valor: str) -> Any:
        """
        Tenta converter valores para o tipo apropriado (int, float ou mantém string).
        """
        valor = valor.strip()
        
        # Verifica se é um número no formato brasileiro (1.234,56)
        if valor.replace('.', '').replace(',', '').isdigit():
            # Remove pontos de milhar e substitui vírgula decimal por ponto
            cleaned = valor.replace('.', '').replace(',', '.')
            # Retorna float se tiver parte decimal, int caso contrário
            return float(cleaned) if '.' in cleaned else int(cleaned)
        
        # Se não for número, retorna a string original
        return valor


    @lru_cache(maxsize=100)
    def _scrape_ano(self, ano: int) -> List[Dict[str, Any]]:
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
                detail=f"Tabela não encontrada para o ano {ano}"
            )

        # Encontra os cabeçalhos da tabela
        headers = []
        thead = table.find('thead')
        if thead:
            header_row = thead.find('tr')
            if header_row:
                headers = [th.get_text(strip=True) for th in header_row.find_all('th')]
        
        # Se não encontrar no thead, tenta pegar a primeira linha do tbody
        if not headers:
            first_row = table.find('tr')
            if first_row:
                headers = [th.get_text(strip=True) for th in first_row.find_all('td')]
        
        # Se ainda não tiver cabeçalhos, usa padrão
        if not headers:
            headers = ['Produto', 'Valor']  # padrão mínimo

        data = []
        rows = table.find_all('tr')
        
        # Se pegou cabeçalhos na primeira linha, começa da segunda
        start_idx = 1 if not thead and len(rows) > 1 else 0
        
        for row in rows[start_idx:]:
            cols = row.find_all('td')
            if cols:
                row_data = {'ano': ano}  # sempre inclui o ano
                
                # Mapeia cada coluna para seu cabeçalho correspondente
                for i, col in enumerate(cols):
                    header = headers[i] if i < len(headers) else f'coluna_{i}'
                    row_data[header] = self._limpar_valor(col.get_text(strip=True))
                
                data.append(row_data)
        
        return data

    def get_data_by_year(self, ano: int) -> List[Dict[str, str]]:
        """
        Realiza o scraping e retorna os dados para o ano informado.
        """
        return self._scrape_ano(ano)

    def get_data_range(self, ano_inicio: int, ano_fim: int) -> List[Dict[str, str]]:
        """
        Retorna dados de um intervalo de anos (inclusive).
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