"""
NECESITO INSTALAR PAQUETES TALES COMO 

    - pip install pymysql
    - https://pypi.org/project/pymysql/

"""

import pymysql
import os


from CRUD_CONN.data_protegida import    MYSQL_URL,\
                                        MYSQLDATABASE,\
                                        MYSQLHOST,\
                                        MYSQLPASSWORD,\
                                        MYSQLPORT,\
                                        MYSQLUSER,\
                                        MYSQL_TABLE



class InsertOp:
    def insert_data(self):
        pass




class CrudApp:

    table_name =  MYSQL_TABLE

    def __init__(self,**kwargs):

        try:
            self.cnx = pymysql.connect(
                url =  kwargs["url"],

            )
            self.tabla_creada = False
            self.cursor = self.cnx.cursor()
        except Exception as Error:
            print(Error)

    def crear_table(self):
        if not self.tabla_creada:
            print(" TABLA YA FUE CREADA")
            return

        print("Se esta creando la tabla")

        query = f"""
        CREATE TABLE {self.table_name} (
                        user_id INT NOT NULL AUTO_INCREMENT,
                        nombre VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        edad INT(11),
                        PRIMARY KEY (user_id)    
        """
        self.cursor.execute(query)
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        self.tabla_creada = True

        print("Se ha creado la tabla ...")


crud = CrudApp(
    url    =   MYSQL_URL

)