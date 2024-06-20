# Usa a imagem oficial do Python 3.9 como base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY . .

# Instala as dependências do Python, se houver
# Exemplo: se você tiver dependências, adicione aqui
RUN pip install -r requirements.txt
# Instala o netcat-openbsd, uma implementação do netcat
RUN apt-get update && \
    apt-get install -y netcat-openbsd

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "ProxysV1.py"]
