import json
import os

class Cones:
    
    def con():
        with open('proxy.json', 'r') as f:
            data = json.load(f)
            
        for proxy in data:
            # Verificar se as chaves 'IP' e 'Porta' existem para este proxy
            if "IP" in proxy and "Port" in proxy:
                ip_adrss = proxy['IP']
                porta_addrss = proxy['Port']
                command = f"nc -vz {ip_adrss} {porta_addrss}"
                os.system(command)
            else:
                print("Error")

Cones.con()