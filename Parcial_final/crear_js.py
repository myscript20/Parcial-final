from almacenar import construir_json_por_pais, resultado_0, resultado_1, resultado_2
import json

# Inicializa la estructura final
estructura_total = []

# Procesa cada resultado por separado y agrégalo
for resultado in [resultado_0, resultado_1, resultado_2]:
    estructura = construir_json_por_pais(resultado)
    estructura_total.extend(estructura)

# Finalmente lo escribes todo junto
with open("ataques.json", "w", encoding="utf-8") as f:
    json.dump(estructura_total, f, indent=4, ensure_ascii=False)


#Prompts

#este regex que valores esta obteniedo y cuantos(Tuve un error al crearlo)
#como se guarda un json con python
#como se puede crear un json con una estructura determinada
#como hago para que al ejecutar crear, utilice lo que esta en almacenamiento
#yo tengo este codigo y en un docuemento py aparte quiero crear el json, en el cual yo ponga el nombre de algo = y que lo extraiga del codigo y lo coloque aqui
#es buena idea sumar los resultados, estos son logs un poco pesados