import json

# Carregar JSON de um arquivo
with open('output.json', 'r') as file:
    proxies = json.load(file)

# Função para extrair IP e porta
def extract_ip_and_port(proxy_string):
    parts = proxy_string.split('\n')
    # Filtrar partes vazias
    parts = [part.strip() for part in parts if part.strip()]
    
    ip = "N/A"
    port = "N/A"
    
    if len(parts) > 0:
        ip = parts[0]
    
    if len(parts) > 1:
        for part in parts[1:]:
            if part.isdigit():  # Verifica se a parte é um número (porta)
                port = part
                break
    
    return ip, port

# Lista para armazenar resultados
result = []

# Extração
for proxy in proxies:
    proxy_string = proxy["proxy"]
    ip, port = extract_ip_and_port(proxy_string)
    if ip != "N/A" and port != "N/A":
        result.append({"IP": ip, "Porta": port})

# Salvar resultados em um novo arquivo JSON
with open('extracted_proxies.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)

print("Os IPs e Portas válidos foram extraídos e salvos em extracted_proxies.json")