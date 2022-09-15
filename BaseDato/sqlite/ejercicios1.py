
import sqlite3 as sql
import pandas as pd

def createDB():
    conn = sql.connect('BaseDatos.db')
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect('BaseDatos.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE tb_usuario (
                id_user integer primary key autoincrement,
                nombre text,
                correo text

            )"""
    )
    conn.commit()
    conn.close()

def connectDB(dataBase):
    conn = sql.connect(dataBase)
    return conn

def insertRow(PNombre, PEmail, PId):
    conn = sql.connect('BaseDatos.db')
    cursor = conn.cursor()
    querysql = f"insert into tb_usuario values ({PId},'{PNombre}', '{PEmail}')"
    cursor.execute(querysql)
    conn.commit()
    conn.close()

def dropTable(tabla):
    conn = sql.connect('BaseDatos.db')
    cursor = conn.cursor()
    querysql = f"DROP table {tabla}"
    cursor.execute(querysql)
    conn.commit()
    conn.close()
    
def selectAll():
    conn = sql.connect('BaseDatos.db') # Conexion
    querySql = f"SELECT * FROM BaseDatos.db"
    # QUERY por pandas retornando la tabla en formato pandas o como tabla
    df = pd.read_sql_query(querySql, conn)
    conn.commit()
    conn.close()
    return df

if __name__ == '__main__':
    pass