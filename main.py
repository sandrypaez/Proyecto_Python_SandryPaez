import json
import sys
from os import path

sys.path.append(path.abspath("modulos"))

from gestion_datos import GestionDatos

def cargar_datos():
    try:
        with open('datos/indicadores.json', 'r', encoding='utf-8') as f:
            indicadores = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        indicadores = []
    
    try:
        with open('datos/paises.json', 'r', encoding='utf-8') as f:
            paises = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        paises = []
    
    try:
        with open('datos/poblacion.json', 'r', encoding='utf-8') as f:
            poblacion = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        poblacion = []
    
    return indicadores, paises, poblacion

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def ver_datos_poblacion(poblacion):
    print("\n=== Registro de Población (2000 - 2023) ===")
    
    filtro_pais = input("Ingrese el país para filtrar (o presione Enter para ver todos): ").strip()
    filtro_anio = input("Ingrese el año para filtrar (o presione Enter para ver todos): ").strip()
    
    datos_filtrados = [
        dato for dato in poblacion 
        if 2000 <= dato["anio"] <= 2023 and 
        (not filtro_pais or dato["pais"].lower() == filtro_pais.lower()) and
        (not filtro_anio or str(dato["anio"]) == filtro_anio)
    ]
    
    if not datos_filtrados:
        print("No hay datos disponibles para los criterios seleccionados.")
        return
    
    for dato in datos_filtrados:
        print(f"\nAño: {dato['anio']} - País: {dato['pais']} ({dato['codigo_iso3']})")
        print(f"Indicador: {dato['indicador_id']} ({dato.get('descripcion', 'Sin descripción')})")
        print(f"Valor: {dato['valor']} {dato['unidad']} | Estado: {dato['estado']}")

def mostrar_menu():
    print("\n" + "♡" * 35 )
    print("♡♡♡♡♡♡♡♡♡SISTEMA DE REGISTRO♡♡♡♡♡♡♡")
    print("♡" * 35 )
    print("♡ [1] Agregar País                ♡")
    print("♡ [2] Agregar Indicador           ♡")
    print("♡ [3] Registrar Dato de Población ♡")
    print("♡ [4] Consultar Datos de Población♡")
    print("♡ [5] Salir                       ♡")
    print("♡" * 35 )
    return input("♡ Seleccione una opción: ")

def main():
    indicadores, paises, poblacion = cargar_datos()
    gestion = GestionDatos(indicadores, paises, poblacion)
    gestion.mostrar_info()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre = input("Nombre del país: ").strip()
            iso = input("Código ISO: ").strip().upper()
            iso3 = input("Código ISO3: ").strip().upper()
            
            if any(p["codigo_iso3"] == iso3 for p in paises):
                print("❌ Este país ya está registrado.")
            else:
                paises.append({"nombre": nombre, "codigo_iso": iso, "codigo_iso3": iso3})
                guardar_datos("datos/paises.json", paises)
                print(f"✔ País '{nombre}' registrado correctamente.")
        
        elif opcion == "2":
            id_indicador = input("ID del indicador: ").strip()
            descripcion = input("Descripción: ").strip()
            
            if any(i["id"] == id_indicador for i in indicadores):
                print("❌ Este indicador ya existe.")
            else:
                indicadores.append({"id": id_indicador, "descripcion": descripcion})
                guardar_datos("datos/indicadores.json", indicadores)
                print("✔ Indicador agregado correctamente.")
        
        elif opcion == "3":
            try:
                anio = int(input("Año del dato: "))
                if anio < 1900 or anio > 2025:
                    print("❌ Año fuera de rango permitido.")
                    continue
            except ValueError:
                print("❌ Año inválido.")
                continue
            
            pais = input("Nombre del país: ").strip()
            codigo_iso3 = input("Código ISO3: ").strip().upper()
            indicador_id = input("ID del indicador: ").strip()
            descripcion = input("Descripción del indicador: ").strip()
            unidad = input("Unidad de medida: ").strip()
            
            try:
                valor = float(input("Valor: "))
            except ValueError:
                print("❌ Valor inválido.")
                continue
            
            if not any(p["codigo_iso3"] == codigo_iso3 for p in paises):
                print("❌ País no registrado.")
                continue
            
            if not any(i["id"] == indicador_id for i in indicadores):
                print("❌ Indicador no registrado.")
                continue
            
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
