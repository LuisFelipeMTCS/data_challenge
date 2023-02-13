from pathlib import Path
from datetime import date
import pandas as pd
from data_enginner.db.query import Query
from data_enginner.db.conn import Conn

class SendCsv():
    
    def __init__(self):
        self.conn = Conn
        self.query = Query
        self.send = SendCsv
        
        
    def send_categories_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_categories(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['category_id', 'category_name', 'description', 'picture'])
       str_date = self.send.check_folder(self,'categories.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def send_customers_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_customers(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['customer_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax'])
       str_date = self.send.check_folder(self,'customers.csv')
       df.to_csv(str_date, index = False, header=True)
       
       
    def check_folder(self,file):
       time = date.today()
       path = Path('data/csv/'+ str(time))
       path.mkdir(parents=True, exist_ok=True)
       str_date = 'data/csv/'+ str(time) + '/' + str(file)
       return str_date
       

SendCsv().send_customers_csv()

