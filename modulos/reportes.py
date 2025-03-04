class Reportes:
    def __init__(self, gestion_datos):
        self.gestion = gestion_datos

    def obtener_datos_poblacion(self, pais, anio_inicio, anio_fin):
        datos = self.gestion.obtener_datos_poblacion(pais, anio_inicio, anio_fin)
        return datos

    def listar_paises(self):
        return self.gestion.listar_paises()