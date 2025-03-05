import json
import sys
from os import path

sys.path.append(path.abspath("modulos"))

from gestion_datos import GestionDatos

def cargar_datos():
    with open('datos/indicadores.json', 'r', encoding='utf-8') as f:
        indicadores = json.load(f)
    with open('datos/paises.json', 'r', encoding='utf-8') as f:
        paises = json.load(f)
    with open('datos/poblacion.json', 'r', encoding='utf-8') as f:
        poblacion = json.load(f)
    return indicadores, paises, poblacion

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def ver_datos_poblacion(poblacion):
    print("\n=== Registro de Población (2000 - 2023) ===")
    datos_filtrados = [dato for dato in poblacion if 2000 <= dato["anio"] <= 2023]
    
    if not datos_filtrados:
        print("No hay datos disponibles en este período.")
        return
    
    for dato in datos_filtrados:
        print(f"\nAño: {dato['anio']} - País: {dato['pais']} ({dato['codigo_iso3']})")
        print(f"Indicador: {dato['indicador_id']} ({dato.get('descripcion', 'Sin descripción')})")
        print(f"Valor: {dato['valor']} {dato['unidad']} | Estado: {dato['estado']}")

def mostrar_menu():
    print("\n=========================")
    print("   SISTEMA DE REGISTRO   ")
    print("=========================")
    print("1) Agregar País")
    print("2) Agregar Indicador")
    print("3) Registrar Dato de Población")
    print("4) Consultar Datos de Población")
    print("5) Salir")
    print("=========================")

def main():
    indicadores, paises, poblacion = cargar_datos()
    gestion = GestionDatos(indicadores, paises, poblacion)
    gestion.mostrar_info()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del país: ")
            iso = input("Código ISO: ")
            iso3 = input("Código ISO3: ")
            paises.append({"nombre": nombre, "codigo_iso": iso, "codigo_iso3": iso3})
            guardar_datos("datos/paises.json", paises)
            print(f"\n✔ País '{nombre}' registrado correctamente.")
        
        elif opcion == "2":
            id_indicador = input("ID del indicador: ")
            descripcion = input("Descripción: ")
            indicadores.append({"id": id_indicador, "descripcion": descripcion})
            guardar_datos("datos/indicadores.json", indicadores)
            print("✔ Indicador agregado correctamente.")
        
        elif opcion == "3":
            anio = int(input("Año del dato: "))
            pais = input("Nombre del país: ")
            codigo_iso3 = input("Código ISO3: ")
            indicador_id = input("ID del indicador: ")
            descripcion = input("Descripción del indicador: ")
            unidad = input("Unidad de medida: ")
            valor = int(input("Valor: "))
            poblacion.append({
                "anio": anio, "pais": pais, "codigo_iso3": codigo_iso3,
                "indicador_id": indicador_id, "descripcion": descripcion,
                "valor": valor, "estado": "disponible", "unidad": unidad
            })
            guardar_datos("datos/poblacion.json", poblacion)
            print("✔ Dato de población registrado correctamente.")
        
        elif opcion == "4":
            ver_datos_poblacion(poblacion)
        
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
