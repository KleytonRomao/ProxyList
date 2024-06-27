from proxys import ProxyScraper  # Importando apenas a classe necessária
from out import refa  # Importando a função refa
from conex import Cones  # Importando a classe Cones

def main():
    url = 'https://www.freeproxy.world/?type=socks5&anonymity=&country=&speed=&port=&page=1'
    output_file = 'output.json'
    
    # Inicializando o scraper de proxies
    proxy_scraper = ProxyScraper(url, output_file)
    
    try:
        # Fazendo a raspagem e salvando os proxies
        proxy_scraper.scrape_and_save()
        # Carregando e analisando os proxies
        proxy_scraper.load_and_parse_proxies()
    except Exception as e:
        print(f"Erro ao raspar e salvar proxies: {e}")
    
    try:
        # Chamando a função refa
        refa()
    except Exception as e:
        print(f"Erro ao executar a função refa: {e}")
    
    try:
        # Chamando o método con da classe Cones
        Cones.con()
    except Exception as e:
        print(f"Erro ao executar o método con: {e}")

if __name__ == "__main__":
    main()

