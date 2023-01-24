import mysql.connector

class Conectar:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="formativa"
        )
        self.cursor = self.conexion.cursor()
    
    def ejecutar(self, sql):
        self.cursor.execute(sql)
        self.conexion.commit()
        return "La conexion fue exitosa ..."
  
    def listarTodos(self, sql):
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        return resultados
    
    def listarUno(self, sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        return resultado
