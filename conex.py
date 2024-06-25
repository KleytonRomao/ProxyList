import json
import os

class Cones:
    @staticmethod
    def con():
        with open('proxy.json', 'r') as f:
            data = json.load(f)
            
        for proxy in data:
            # Verificar se as chaves 'IP' e 'Porta' existem para este proxy
            if "IP" in proxy and "Porta" in proxy:
                ip_adrss = proxy['IP']
                porta_addrss = proxy['Porta']
                command = f"nc -vz {ip_adrss} {porta_addrss}"
                os.system(command)
            else:
                print("Error")

# Exemplo de uso:
# Cones.con()
