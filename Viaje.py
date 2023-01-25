from clases.Conectar import Conectar

class Viaje:
    def __init__(self, id = 0, ciudadInicio = '', ciudadFin = ''):
        self.__id = id
        self.__ciudadInicio = ciudadInicio
        self.__ciudadFin = ciudadFin
        self.__conectar = Conectar()

    def listarViajes(self):
        sql = f"SELECT * FROM viaje WHERE ciudadInicio = '{self.__ciudadInicio}' AND ciudadFin = '{self.__ciudadFin}'"
        viajes = self.__conectar.listarTodos(sql)
        return viajes

    def listarViaje(self):
        sql = f"SELECT * FROM viaje WHERE id = {self.__id}"
        viaje = self.__conectar.listarUno(sql)
        return viaje

    def disminuirViaje(self):
        sql = f"UPDATE viaje SET cantidad = cantidad - 1 WHERE id = {self.__id}"
        resultado = self.__conectar.ejecutar(sql)

        if resultado == 1:
            resultado = 'Se ha actualizado la cantidad'
        elif resultado == 0:
            resultado = 'No se ha actualizado la cantidad'

        return resultado

    def cantidadViajes(self):
        sql = f"SELECT cantidad FROM viaje WHERE id = {self.__id}"
        tupla = self.__conectar.listarUno(sql)
        return tupla
