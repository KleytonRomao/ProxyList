
import requests
from bs4 import BeautifulSoup
import json


class ProxyScraper:
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def scrape_and_save(self):
        # Enviar uma solicitação HTTP para obter o conteúdo da página
        response = requests.get(self.url)

        # Verificar se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Obter o conteúdo da página
            page_content = response.content

            # Criar um objeto BeautifulSoup para analisar o conteúdo HTML
            soup = BeautifulSoup(page_content, 'html.parser')

            # Encontrar todas as tags 'tr'
            rows = soup.find_all('tr')

            # Criar uma lista para armazenar as informações
            data_list = []

            # Adicionar cada linha como um dicionário à lista
            for row in rows:
                data_list.append({'proxy': row.text.strip()})

            # Converter a lista em uma string JSON
            json_data = json.dumps(data_list, ensure_ascii=False)

            # Salvar o JSON em um arquivo
            with open(self.output_file, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)

            print("JSON gerado com sucesso.")
        else:
            print("Falha ao obter a página. Código de status:", response.status_code)

    def load_and_parse_proxies(self):
        # Caminho para o arquivo JSON
        caminho_arquivo = self.output_file

        # Carregue dados JSON do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)

        # Itere sobre os proxies e imprima as informações
        for item in dados:
            if "proxy" in item and item["proxy"]:
                # Divida a string usando '\n' como delimitador
                proxy_info = item["proxy"].split("\n")

                # Remova strings vazias da lista resultante
                proxy_info = list(filter(lambda x: x.strip() != "", proxy_info))
                

