# SupportFlow

Sistema de atendimento para empresas, com organização de chamados e colaboração entre administradores e atendentes.

## Estado atual

Implementado:

- API inicial em Python + FastAPI, executada com Uvicorn.
- `GET /health`, com HTTP 200 e corpo `{"status": "ok"}`.
- Teste com pytest e TestClient que verifica o status HTTP e o corpo da resposta.

O endpoint `/health` indica apenas que a API está respondendo. Ele não verifica banco de dados, serviços externos ou disponibilidade de funcionalidades futuras.

## Executar localmente no Windows (PowerShell)

Requer **Python 3.14 ou superior**. Esta etapa foi validada com Python **3.14.0**.

Execute os comandos abaixo a partir da raiz do repositório.

### Criar o ambiente virtual e instalar as dependências

```powershell
python --version
python -m venv backend\.venv
```

Se `python` não estiver disponível no PATH, use o caminho completo do interpretador com o operador `&`. Para uma instalação padrão do Python 3.14 pelo gerenciador do Python no Windows:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.14-64\python.exe" -m venv backend\.venv
```

Instale a aplicação e as dependências de teste:

```powershell
.\backend\.venv\Scripts\python.exe -m pip install -e "./backend[test]"
```

As dependências estão em `backend/pyproject.toml`: FastAPI e Uvicorn são de execução; pytest e HTTPX pertencem ao extra `test`. Para instalar somente as dependências de execução, omita `[test]`.

Os comandos usam diretamente o Python do ambiente virtual, sem precisar ativá-lo ou alterar a política de execução do PowerShell. O ambiente `backend/.venv` é local e ignorado pelo Git.

### Iniciar a API

```powershell
.\backend\.venv\Scripts\python.exe -m uvicorn supportflow_api:app --host 127.0.0.1 --port 8000
```

Em outro terminal PowerShell, confira a resposta:

```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -UseBasicParsing |
    Select-Object StatusCode, Content
```

Resultado esperado: status `200` e conteúdo `{"status":"ok"}`. Encerre o servidor com `Ctrl+C` no terminal em que ele foi iniciado.

### Executar os testes

```powershell
.\backend\.venv\Scripts\python.exe -m pytest backend/tests
```

## Escopo inicial planejado

- Cadastro, login e logout.
- Organizações com administradores e atendentes.
- Isolamento dos dados entre empresas.
- Chamados com responsável, prioridade e status.
- Comentários e histórico dos chamados.
- Busca, filtros e paginação.

## Stack planejada

- **Frontend:** React + TypeScript.
- **Banco de dados:** PostgreSQL.
- **CI/CD:** GitHub Actions.

O escopo funcional acima, o banco de dados, o frontend, a infraestrutura e as rotinas de CI/CD ainda não foram implementados.
