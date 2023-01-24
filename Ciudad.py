from Conectar import Conectar

class Ciudad:
    def __init__(self):
        self.conectar = Conectar()

    def listarCiudades(self):
        sql = "SELECT * FROM ciudades"
        resultados = self.conectar.listarTodos(sql)
        return resultados
