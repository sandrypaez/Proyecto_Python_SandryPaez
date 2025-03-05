import json

def cargar_datos_poblacion():
    with open('datos/poblacion.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def cargar_datos_paises():
    with open('datos/paises.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def obtener_poblacion_pais_periodo(pais, inicio, fin):
    datos = cargar_datos_poblacion()
    return [d for d in datos if d["pais"] == pais and inicio <= d["ano"] <= fin]

def listar_paises():
    return cargar_datos_paises()

def obtener_poblacion_por_indicador(indicador):
    datos = cargar_datos_poblacion()
    return [d for d in datos if d["indicador_id"] == indicador]

def obtener_poblacion_ultimos_10_anios():
    datos = cargar_datos_poblacion()
    anio_actual = max(d["ano"] for d in datos)
    return [d for d in datos if d["ano"] >= anio_actual - 10]

def poblacion_total_pais_anio(pais, anio):
    datos = cargar_datos_poblacion()
    for d in datos:
        if d["pais"] == pais and d["ano"] == anio:
            return d["valor"]
    return None
