import mysql.connector
import time
class Conn():
  
     
  def conecta_db(self):
    try:
      con = mysql.connector.connect(
                            host='127.0.0.1', 
                            port = '3306',
                            database='mydb',
                            user='root', 
                            password='mysql123')
      return con
    except Exception as e:
          print(e)
          
  def insert(self,sql):
      conn = Conn.conecta_db(self)
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
      
      
  def select(self,sql):
      conn = Conn.conecta_db(self)
      cur = conn.cursor()
      cur.execute(sql)
      recset = cur.fetchall()
      cur.close()
      return recset

    

