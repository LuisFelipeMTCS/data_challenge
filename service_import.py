from pathlib import Path
from datetime import date
import pandas as pd
import os
from data_enginner.db.query import Query
from data_enginner.db.conn import Conn

class ServiceImport():
    
    def __init__(self):
        self.query_categories = Conn.select(self,(Query.select_categories(self)))
        
        
    def dataframe_extract(self):
       df_dbase = []
       for dataframe in self.query_categories:
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['category_id', 'category_name', 'description', 'picture'])
       time = date.today()
       path = Path('data/csv/'+ str(time))
       path.mkdir(parents=True, exist_ok=True)
       str_date = 'data/csv/'+ str(time) + '/categories.csv'
       df.to_csv(str_date, index = False, header=True)
       
ServiceImport().dataframe_extract()

