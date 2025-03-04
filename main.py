import json
from pprint import pprint
from modulos.gestion_datos import GestionDatos
from modulos.reportes import Reportes

def cargar_datos():
    with open('datos/indicadores.json') as f:
        indicadores = json.load(f)
    with open('datos/paises.json') as f:
        paises = json.load(f)
    with open('datos/poblacion.json') as f:
        poblacion = json.load(f)
    return indicadores, paises, poblacion

def main():
    indicadores, paises, poblacion = cargar_datos()
    gestion = GestionDatos(poblacion, paises, indicadores)
    reportes = Reportes(gestion)

    # Ejemplo de uso de reportes con mejor formato
    print(json.dumps(reportes.obtener_datos_poblacion("India", 2000, 2023), indent=4))
    pprint(reportes.listar_paises())

if __name__ == "__main__":
    main()