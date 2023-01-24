from Conectar import Conectar

class Compra:
    def __init__(self, id, rut, nombre):
        self.id = id
        self.rut = rut
        self.nombre = nombre
        self.conectar = Conectar()

    def RegistroCompras(self):
        sql = f"INSERT INTO compras (id, rut, nombre) VALUES ({self.id}, '{self.rut}', '{self.nombre}')"
        self.conectar.ejecutar(sql)

    def AumentarCompra(self):
        sql = f'UPDATE viaje SET cantidad = cantidad + 1  WHERE id = (SELECT id FROM compra WHERE nroTicket = {self.__nroTicket});'
        resultado = self.__conectar.ejecutar(sql)


    def ListarCompra(self):
        sql = f"SELECT * FROM compras WHERE rut = '{self.rut}'"
        resultados = self.conectar.listarTodos(sql)
        return resultados

    def EliminarCompra(self):
        sql = f"DELETE FROM compras WHERE id = {self.id}"
        self.conectar.ejecutar(sql)
