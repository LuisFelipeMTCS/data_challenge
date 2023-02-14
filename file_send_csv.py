import pandas as pd 
from db.mysql.query import Query

class FileSendCsv():
    
    def __init__(self):
        self.insert = Query()
    
    
    def send_categories_csv(self):
        self.insert.insert_order_details(data = [10248,11,14,12,0])
        data =  pd.read_csv(self.path,sep=";", encoding='utf-8-sig')
        
        
FileSendCsv().send_categories_csv()
        
        
    