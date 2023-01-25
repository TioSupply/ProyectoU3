import mysql.connector

class Conectar:
    def __init__(self):
        self.__db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '', 
            database = 'formativa'
        )
        
        self.__cursor = self.__db.cursor()

    def ejecutar(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__db.commit()
            resultado = self.__cursor.rowcount
            return resultado
        except mysql.connector.Error as e:
            return 'Se ha producido un error: '+str(e)

    def listarTodos(self, sql):
        self.__cursor.execute(sql)
        lista = self.__cursor.fetchall()
        return lista

    def listarUno(self, sql):
        self.__cursor.execute(sql)
        tupla = self.__cursor.fetchone()
        return tupla
