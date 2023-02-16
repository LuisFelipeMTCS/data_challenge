import pandas as pd 
from db.mysql.query import Query
from file_check_folder import CheckFolder

class FileSendCsv():
    
    def __init__(self):
        self.insert = Query()
        self.CheckFolder = CheckFolder()
    
    
    def send_categories_csv(self):
        path = self.CheckFolder.check_folder_db('categories','categories.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_categories(data = row)
            
    def send_customer_customer_demo_csv(self):
        path = self.CheckFolder.check_folder_db('customer_customer_demo','customer_customer_demo.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_customer_customer_demo(data = row)
            
    def send_customer_demographics_csv(self):
        path = self.CheckFolder.check_folder_db('customer_demographics','customer_demographics.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_customer_demographics(data = row)
            
    def send_customers_csv(self):
        path = self.CheckFolder.check_folder_db('customers','customers.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_customers(data = row)
            
    def send_employee_territories_csv(self):
        path = self.CheckFolder.check_folder_db('employee_territories','employee_territories.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_employee_territories(data = row)
    
    def send_employees_csv(self):
        path = self.CheckFolder.check_folder_db('employees','employees.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_employees(data = row)
            
    def send_orders_csv(self):
        path = self.CheckFolder.check_folder_db('orders','orders.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_orders(data = row)
            
    def send_products_csv(self):
        path = self.CheckFolder.check_folder_db('products','products.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_products(data = row)
            
    def send_region_csv(self):
        path = self.CheckFolder.check_folder_db('region','region.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_region(data = row)
            
    def send_shippers_csv(self):
        path = self.CheckFolder.check_folder_db('shippers','shippers.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_shippers(data = row)
            
    def send_suppliers_csv(self):
        path = self.CheckFolder.check_folder_db('suppliers','suppliers.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_suppliers(data = row)
            
    def send_territories_csv(self):
        path = self.CheckFolder.check_folder_db('territories','territories.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_territories(data = row)
            
    def send_us_states_csv(self):
        path = self.CheckFolder.check_folder_db('us_states','us_states.csv')
        data =  pd.read_csv(path, encoding='utf-8-sig')
        for row in data.values:
            self.insert.insert_us_states(data = row)
            
    def send_order_details_csv(self):
        path = self.CheckFolder.check_folder_file('order_details.csv')
        if path == False:
            print("Arquivo não enviado ao diretório")
        else:
            data =  pd.read_csv(path, encoding='utf-8-sig')
            for row in data.values:
                self.insert.insert_order_details(data = row)
        
            
        
        
        
        
    