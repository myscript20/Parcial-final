import requests, re, json

print("Incio")

def extractFromRegularExpresion(regex, file):
    if file:
        data=""
        with open(file,"rt") as f:
            data=f.read()
        return re.findall(regex,data)
    return None

    
def apiRequestData(data):
    JsonData = []
    if not data:
        print("No hay datos para procesar.")
        return
    URI = "http://ip-api.com/json/"

    ip_seen = set()

    for ip, date, hour, method, path in data:
        if ip in ip_seen:
            continue  # Ya procesada

        ip_seen.add(ip)
        formatData = {
            "ip": ip,
            "date": date,
            "hour": hour,
            "method": method,
            "path": path
            }

        try:
            response = requests.get(f"{URI}{ip}").json()
            formatData["country"] = response.get("country")
            formatData["city"] = response.get("city")
        except Exception as e:
            formatData["country"] = None
            formatData["city"] = None

        JsonData.append(formatData)
    return JsonData

regex = r"(\d{1,3}(?:\.\d{1,3}){3})\s-\s-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4}):(\d{2}:\d{2}:\d{2})\s.+?\"([A-Z]{3,7})\s(.+?)\s"

resultado0 = extractFromRegularExpresion(regex, "apache(1).log")
resultado1 = extractFromRegularExpresion(regex, "apache(2).log")
resultado2 = extractFromRegularExpresion(regex, "apache(3).log")

resultado_0 = apiRequestData(resultado0)
resultado_1 = apiRequestData(resultado1)
resultado_2 = apiRequestData(resultado2)


def imprimir_resultado(data):
    print(f"{'IP':<20}{'País':<20}{'Fecha':<20}{'Metodo':<20}{'Ruta':<20}")
    print("-" * 65)

    for entrada in data:
        ip = entrada.get("ip", "")
        pais = entrada.get("country") or "Desconocido"
        fecha = entrada.get("date", "")
        metodo = entrada.get("method") or "-"
        ruta = entrada.get("path") or "-"
        

        print(f"{ip:<20}{pais:<20}{fecha:<20}{metodo:<20}{ruta:<9}")

# almacenar.py

def construir_json_por_pais(data):
    pais_dict = {}

    for entrada in data:
        pais = entrada.get("country") or "Desconocido"
        fecha = entrada.get("date", "")
        metodo = entrada.get("method") or "-"
        ruta = entrada.get("path") or "-"

        ataque = {
            "fecha": fecha,
            "metodo": metodo,
            "ruta": ruta
        }

        if pais not in pais_dict:
            pais_dict[pais] = []
        
        pais_dict[pais].append(ataque)

    # Convertimos a lista con la estructura deseada
    resultado = []
    for pais, ataques in pais_dict.items():
        resultado.append({
            "country": pais,
            "attacks": ataques
        })

    return resultado


print(" Apache 1 ")
imprimir_resultado(resultado_0)
print(" Apache 2 ")
imprimir_resultado(resultado_1)
print(" Apache 3 ")
imprimir_resultado(resultado_2)
