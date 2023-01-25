from clases.Conectar import Conectar

class Compra:
    def __init__(self, id = 0, rut = '', nombre = '', nroTicket = 0):
        self.__id = id
        self.__rut = rut
        self.__nombre = nombre
        self.__nroTicket = nroTicket
        self.__conectar = Conectar()

    def registrarCompra(self):
        sql = f"INSERT INTO compra(id, rut, nombre) VALUES({self.__id}, '{self.__rut}', '{self.__nombre}')"
        resultado = self.__conectar.ejecutar(sql)

        if resultado == 1:
            resultado = 'Se ha ingresado una nueva compra'
        elif resultado ==0:
            resultado = 'No se ha ingresado la compra'

        return resultado

    def buscarCompra(self):
        sql = f"SELECT c.nroTicket, c.rut, c.nombre, v.horaInicio, v.ciudadInicio, v.ciudadFin, v.precio FROM compra c JOIN viaje v WHERE v.id = c.id AND rut = '{self.__rut}'"
        compras = self.__conectar.listarTodos(sql)
        return compras

    def eliminarCompra(self):
        sql = f"DELETE FROM compra WHERE nroTicket = {self.__nroTicket}"
        resultado = self.__conectar.ejecutar(sql)
        
        if resultado == 1:
            resultado = 'Se ha eliminado la compra'
        elif resultado == 0:
            resultado = 'No se ha eliminado la compra'

        return resultado

    def aumentarCantidad(self):
        sql = f'UPDATE viaje SET cantidad = cantidad + 1  WHERE id = (SELECT id FROM compra WHERE nroTicket = {self.__nroTicket});'
        resultado = self.__conectar.ejecutar(sql)

        if resultado == 1:
            resultado = 'Se ha actualizado cantidad'
        elif resultado == 0:
            resultado = 'No se ha actualizado cantidad'

        return resultado

    def buscarCompraid(self):
        sql = f"SELECT v.id FROM viaje v JOIN compra c WHERE v.id = c.id;"
        lista = self.__conectar.listarTodos(sql)
        return lista
