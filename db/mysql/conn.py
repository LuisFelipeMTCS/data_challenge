import mysql.connector
class Conn:
  
     
  def conecta_db(self):
    try:
      con = mysql.connector.connect(
                            host='127.0.0.1', 
                            port = '3306',
                            database='northwind',
                            user='root', 
                            password='mysql123')
      return con
    except Exception as e:
          print(e)
          
  def select(self,sql):
      cur = Conn.conecta_db(self).cursor() 
      cur.execute(sql)
      recset = cur.fetchall()
      return recset
    

