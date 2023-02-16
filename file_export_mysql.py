from datetime import date
import pandas as pd
from db.mysql.query import Query
from db.mysql.conn import Conn
from file_check_folder import CheckFolder

class FileExportMysql():
    
    def __init__(self):
      self.time = date.today()
      self.query = Query
      self.conn = Conn
      self.CheckFolder = CheckFolder()
    
    def export(self):
       df_dbase = []
       data = self.conn.select(self,(self.query.select_orders_order_detail(self)))
       for dataframe in data:
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['order', 'customer', 'employee', 'date order',
                                             'date required','via ship','freight','name ship',
                                             'adress ship','city ship','region ship','postal code ship',
                                             'cod product','price unit','quantity','discout'])
       str_date = self.CheckFolder.check_folder_import_result('orders_order_details.csv')
       df.to_csv(str_date, index = False, header=True)
       

