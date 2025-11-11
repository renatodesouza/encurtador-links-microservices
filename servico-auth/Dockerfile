FROM python:3.12-slim

# Definindo variaveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

# Criando um diretorio para o app
WORKDIR /app

# Instala as dependências
COPY requirements.txt
RUN pip install -r requirements.txt

# 5. Copie o código do seu projeto para dentro do container
# (Estamos assumindo que 'core' e 'manage.py' estão na raiz de 'servico-auth')
COPY . .