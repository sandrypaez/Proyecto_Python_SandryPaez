class GestionDatos:
    def __init__(self, poblacion, paises, indicadores):
        self.poblacion = poblacion
        self.paises = paises
        self.indicadores = indicadores

    def obtener_datos_poblacion(self, pais, anio_inicio, anio_fin):
        return [
            dato for dato in self.poblacion
            if dato['pais'] == pais and anio_inicio <= dato['ano'] <= anio_fin
        ]

    def listar_paises(self):
        return self.paises

    def obtener_poblacion_por_anio(self, pais, anio):
        for dato in self.poblacion:
            if dato['pais'] == pais and dato['ano'] == anio:
                return dato['valor']
        return None