import json

class GestionDatos:
    def __init__(self, indicadores, paises, poblacion):
        self.indicadores = indicadores
        self.paises = paises
        self.poblacion = poblacion

    def mostrar_info(self):
        print("Clase GestionDatos cargada correctamente.")

    def listar_paises(self):
        return [pais["nombre"] for pais in self.paises]

    def agregar_dato_poblacion(self, nuevo_dato):
        self.poblacion.append(nuevo_dato)

    def guardar_datos(self, nombre_archivo, datos):
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

print("Módulo gestion_datos importado correctamente.")  
