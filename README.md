# Proxy Scraper

O **Proxy Scraper** é uma ferramenta simples em Python para extrair informações de proxies de uma página web e armazená-las em um arquivo TXT. Além disso, a ferramenta oferece a capacidade de carregar e analisar esses proxies a partir do arquivo gerado.

## Como Usar

1. **Requisitos:**
   - Certifique-se de ter os módulos Python `requests` e `beautifulsoup4` instalados. Você pode instalá-los executando:

     ```bash
     pip install requests beautifulsoup4
     ```

2. **Exemplo de Uso:**
   - Importe a classe `ProxyScraper` no seu script Python.

     ```python
     from proxy_scraper import ProxyScraper
     ```

   - Crie uma instância da classe, fornecendo a URL da página web que contém os proxies desejados e o nome do arquivo de saída TXT.

     ```python
     url = 'https://www.freeproxy.world/?type=socks5&anonymity=&country=&speed=&port=&page=1'
     output_file = 'output.txt'
     proxy_scraper = ProxyScraper(url, output_file)
     ```

   - Utilize o método `scrape_and_save` para extrair os proxies da página web e salvá-los em um arquivo TXT.

     ```python
     proxy_scraper.scrape_and_save()
     ```

   - Use o método `load_and_parse_proxies` para carregar o arquivo TXT e imprimir as informações formatadas dos proxies.

     ```python
     proxy_scraper.load_and_parse_proxies()
     ```

   - **Exemplo de Uso Completo:**

     ```python
     url = 'https://www.freeproxy.world/?type=socks5&anonymity=&country=&speed=&port=&page=1'
     output_file = 'output.txt'

     proxy_scraper = ProxyScraper(url, output_file)
     proxy_scraper.scrape_and_save()
     proxy_scraper.load_and_parse_proxies()
     ```

3. **Observações sobre Tipos de Proxy:**

   O **Proxy Scraper** permite a coleta de proxies de diferentes tipos, como socks5 e socks4, ao ajustar a URL fornecida. Se você deseja obter proxies de um tipo específico, você pode modificar a URL de acordo.

   ### Exemplo: Obtendo Proxies SOCKS5,SOCKS4,HTTP,HTTPS

   Ao alterar a URL de:

   ```python
   url = 'https://www.freeproxy.world/?type=socks5&anonymity=&country=&speed=&port=&page=1'
   url = 'https://www.freeproxy.world/?type=socks4&anonymity=&country=&speed=&port=&page=1'
   url = 'https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page=1'
   url = 'https://www.freeproxy.world/?type=https&anonymity=&country=&speed=&port=&page=1'
