from fastapi import FastAPI
from pathlib import Path
import yaml
from controllers import auth_controller, producao_controller

# Carrega o YAML
def load_openapi():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    DATA_DIR = BASE_DIR / "fastapi-embrapa"
    # DATA_DIR = BASE_DIR / "API Tech Challenge"

    with open(DATA_DIR / "openapi.yaml", encoding='utf-8') as f:
        return yaml.safe_load(f)

app = FastAPI(
    title="API EMBRAPA",
    description="API para gerenciar Produção, Processamento, Comercialização, Importação e Exportação.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Mescla a especificação YAML com as rotas
app.openapi_schema = load_openapi()
app.include_router(auth_controller.router, prefix="/api/v1/auth")
app.include_router(producao_controller.router, prefix="/api/v1")