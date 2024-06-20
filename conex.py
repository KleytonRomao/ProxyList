import json
import os

# Abrir o arquivo JSON
with open('proxy.json', 'r') as f:
    # Carregar os dados do arquivo JSON
    proxies = json.load(f)
    
    # Iterar sobre cada proxy no arquivo JSON
    for proxy in proxies:
        if 'ip' in proxy and 'porta' in proxy:
            ip = proxy['ip']
            porta = proxy['porta']
            
            # Executar o comando para verificar a conexão usando netcat (nc)
            command = f"nc -vz {ip} {porta}"
            os.system(command)
            
            print(f"Verificando proxy {ip}:{porta}")
        else:
            print("Proxy inválido encontrado no arquivo JSON.")
