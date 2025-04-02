import pandas as pd
from pathlib import Path
from fastapi import HTTPException, Query
from typing import List, Dict

class ProducaoService:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.DATA_DIR = self.BASE_DIR / "data"
        self.CSV_PATH = self.DATA_DIR / "Producao.csv"

    def get_producao(self) -> List[Dict[str, str]]:
        """Obtém dados de produção do arquivo CSV"""
        # Verifica se o arquivo existe
        if not self.CSV_PATH.exists():
            raise HTTPException(
                status_code=404,
                detail="Arquivo de produção não encontrado"
            )
        
        try:
            # Lê o arquivo CSV com codificação UTF-8
            df = pd.read_csv(self.CSV_PATH, encoding='utf-8')
            # Converte para lista de dicionários, substituindo NaN por strings vazias
            return df.fillna('').to_dict(orient='records')
        
        except pd.errors.EmptyDataError:
            # Erro específico para arquivo vazio
            raise HTTPException(
                status_code=400,
                detail="O arquivo CSV está vazio"
            )
        except Exception as e:
            # Erro genérico para outros problemas
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao processar arquivo: {str(e)}"
            )

    def get_producao_by_year(self, ano: int = Query(..., description="Ano para filtrar (ex: 1970)", gt=1970, lt=2023)):
        """
        Filtra os dados de produção pelo ano especificado.
        Retorna lista de produtos com a produção no ano solicitado.
        """
        try:
            df = pd.read_csv(self.CSV_PATH, encoding='utf-8', sep=';')

            # Converte todos os cabeçalhos para string
            df.columns = df.columns.astype(str)
            
            # Verifica se o ano existe no DataFrame
            if str(ano) not in df.columns:
                available_years = [col for col in df.columns if col.isdigit()]
                raise HTTPException(
                    status_code=400,
                    detail=f"Ano {ano} não encontrado. Anos disponíveis: {', '.join(available_years)}"
                )
            
            # Filtra e formata os dados
            result = df[['id', 'control', 'produto', str(ano)]] \
                .rename(columns={str(ano): 'producao'}) \
                .to_dict(orient='records')
            
            return result

        except FileNotFoundError:
            raise HTTPException(
                status_code=404,
                detail="Arquivo de produção não encontrado"
            )
        except pd.errors.EmptyDataError:
            raise HTTPException(
                status_code=400,
                detail="Arquivo CSV está vazio ou corrompido"
            )

# Instância global do serviço para ser reutilizada
producao_service = ProducaoService()