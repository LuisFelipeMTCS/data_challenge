import pandas as pd
from data_enginner.db.query import Query
from data_enginner.db.conn import Conn

class ServiceImport():
    
    def __init__(self):
        self.query_categories = Conn.select(self,(Query.select_categories(self)))
        
        
    def dataframe_extract(self):
       for dataframe in self.query_categories:
            df = pd.DataFrame(dataframe)
            datatypes_per_column = {
                "CNPJ": "string",
                "DataFundacao": "datetime64[ms]",
                "NatJuridica": "object",
                "NumAlunos": "int64"
       }
           
           
ServiceImport().dataframe_extract()