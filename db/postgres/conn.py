import psycopg2 

class Conn:
  
     
  def conecta_db(self):
    try:
      con = psycopg2.connect(host='127.0.0.1',
                            port='5432',
                            dbname='northwind',
                            user='postgres', 
                            password='123')
      return con
    except Exception as e:
          print(e)
          
  def select(self,sql):
      cur = Conn.conecta_db(self).cursor() 
      cur.execute(sql)
      recset = cur.fetchall()
      return recset
    
    
Conn().conecta_db()

