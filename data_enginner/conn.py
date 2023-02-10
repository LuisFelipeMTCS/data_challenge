import psycopg2 

def conecta_db():
  try:
    con = psycopg2.connect(host='localhost', 
                          database='rorthwind',
                          user='postgres', 
                          password='123')
  except Exception as e:
        print(e)
  return con