# API Vitivinicultura Embrapa - FIAP Tech Challenge

Esta API foi desenvolvida como parte do Tech Challenge da FIAP, com o objetivo de disponibilizar dados públicos sobre vitivinicultura do Brasil, fornecidos pela Embrapa. A API permite a consulta estruturada desses dados para futuras análises e utilização em modelos de Machine Learning.

## 🌐 Link para acesso à API

Acesse a documentação interativa (Swagger UI):  
[https://embrapa-fiap.onrender.com/docs](https://embrapa-fiap.onrender.com/docs)

---

## 📌 Objetivo

Criar uma API pública RESTful, desenvolvida em Python com FastAPI, que realiza Web Scraping em páginas da Embrapa e fornece os dados organizados para consumo por sistemas terceiros. A API utiliza autenticação JWT, está hospedada no Render e armazena informações de usuários e tokens em um banco de dados PostgreSQL.

---

## 🧩 Funcionalidades

A API disponibiliza dados das seguintes áreas:

- ✅ Produção  
- ✅ Processamento  
- ✅ Comercialização  
- ✅ Importação  
- ✅ Exportação  

Os dados podem ser retornados em formato JSON ou CSV, conforme preferência do cliente.

---

## 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação. Cada requisição deve conter um token válido no cabeçalho `Authorization: Bearer <token>`.

### Validação:
- O token é verificado pelo FastAPI.
- A API consulta o banco PostgreSQL para validar o usuário e o token.
- Se inválido ou expirado, a requisição é negada com resposta de erro.
- Se válido, a requisição segue normalmente.

---

## 🛠️ Arquitetura da Solução

```mermaid
graph TD
    A[Usuário Cliente] -->|HTTP com JWT| B[API FastAPI - Render]
    B --> C[Valida Token com PostgreSQL]
    C -->|Válido| D[Web Scraping - Embrapa]
    D --> E[Processamento dos Dados]
    E --> F[Resposta em JSON/CSV]
    F --> G[Retorno ao Cliente]
    C -->|Inválido| X[Erro 401 - Não autorizado]
