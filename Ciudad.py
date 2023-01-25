from clases.Conectar import Conectar

class Ciudad:
    def __init__(self):
        self.__conectar = Conectar()

    def listarCiudades(self):
        sql = 'SELECT * FROM ciudades'
        ciudades = self.__conectar.listarTodos(sql)
        return ciudades
