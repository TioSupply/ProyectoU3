from Conectar import Conectar

class Viaje:
    def __init__(self, id, ciudad_inicio, ciudad_fin):
        self.id = id
        self.ciudad_inicio = ciudad_inicio
        self.ciudad_fin = ciudad_fin
        self.conectar = Conectar()
    
    def listarViajes(self):
        sql = f"SELECT * FROM viajes WHERE ciudad_inicio = '{self.ciudad_inicio}' AND ciudad_fin = '{self.ciudad_fin}'"
        resultados = self.conectar.listarTodos(sql)
        return resultados
    
    def listarViaje(self):
        sql = f"SELECT * FROM viajes WHERE id = {self.id}"
        resultado = self.conectar.listarUno(sql)
        return resultado
    
    def disminuirViaje(self):
        sql = f"UPDATE viajes SET cantidad = cantidad - 1 WHERE id = {self.id}"
        self.conectar.ejecutar(sql)
    
    def aumentarViaje(self):
        sql = f"UPDATE viajes SET cantidad = cantidad + 1 WHERE id = {self.id}"
        self.conectar.ejecutar(sql)
