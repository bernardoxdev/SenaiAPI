FROM python:3.10-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Copia apenas arquivos necessários
COPY pyproject.toml README.md /app/

# Instala dependências
RUN pip install --upgrade pip \
    && pip install .

# Copia o código
COPY backend /app/backend

# Porta da API
EXPOSE 5693

# Comando de execução
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "5693"]
