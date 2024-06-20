import json
import os

# Abrir e ler o arquivo JSON
with open('proxy.json', 'r') as f:
    data = json.load(f)

# Iterar sobre cada objeto (proxy) no arquivo JSON
for proxy in data:
    # Verificar se as chaves 'IP' e 'porta' existem para este proxy
    if "IP" in proxy and "Porta" in proxy:
        ip_adrss = {proxy['IP']}
        porta_addrss = {proxy['Porta']}
        command = f"nc -vz {ip_adrss}{porta_addrss}"
        command = command.replace("{", "").replace("}", "").replace("'", "")
        os.system(command)
    else:
        print("Chaves 'IP' e/ou 'porta' não encontradas para este proxy.")
