import json

class OutPut:
    @staticmethod
    def load_proxies(file_path='output.json'):
        with open(file_path, 'r') as file:
            return json.load(file)

def extract_ip_and_port(proxy_string):
    parts = proxy_string.split('\n')
    parts = [part.strip() for part in parts if part.strip()]
    
    ip = "N/A"
    port = "N/A"
    
    if len(parts) > 0:
        ip = parts[0]
    
    if len(parts) > 1:
        for part in parts[1:]:
            if part.isdigit():
                port = part
                break
    
    return ip, port

def refa():

    try:
        proxies = OutPut.load_proxies()

        result = []

        for proxy in proxies:
            proxy_string = proxy.get("proxy", "")
            ip, port = extract_ip_and_port(proxy_string)
            if ip != "N/A" and port != "N/A":
                result.append({"IP": ip, "Port": port})

        with open('proxy.json', 'w') as outfile:
            json.dump(result, outfile, indent=4)

        print("Os IPs e Portas válidos foram extraídos e salvos em proxy.json")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
