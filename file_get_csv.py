import pandas as pd
from db.postgres.query import Query
from db.postgres.conn import Conn
from file_check_folder import CheckFolder

class FileGetCsv():
    
    def __init__(self):
        self.conn = Conn
        self.query = Query
        self.CheckFolder = CheckFolder()
        
        
    def import_categories_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_categories(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['category_id', 'category_name', 'description', 'picture'])
       str_date = self.CheckFolder.check_folder_csv('categories.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_customer_customer_demo_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_customer_customer_demo(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['customer_id', 'customer_type_id'])
       str_date = self.CheckFolder.check_folder_csv('customer_customer_demo.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_customer_demographics_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_customer_demographics(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['customer_type_id', 'customer_desc'])
       str_date = self.CheckFolder.check_folder_csv('customer_demographics.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_customers_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_customers(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['customer_id', 'company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax'])
       str_date = self.CheckFolder.check_folder_csv('customers.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_employee_territories_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_employee_territories(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['employee_id', 'territory_id'])
       str_date = self.CheckFolder.check_folder_csv('employee_territories.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_employees_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_employees(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['employee_id', 'last_name', 'first_name', 'title', 'title_of_courtesy', 'birth_date', 'hire_date', 
                                             'address', 'city', 'region', 'postal_code','country', 'home_phone', 'extension', 'photo', 'notes', 
                                             'reports_to', 'photo_path'])
       str_date = self.CheckFolder.check_folder_csv('employees.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_orders_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_orders(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['order_id', 'customer_id', 'employee_id', 'order_date', 'required_date', 
                                             'shipped_date', 'ship_via', 'freight', 'ship_name', 'ship_address', 'ship_city', 
                                             'ship_region', 'ship_postal_code', 'ship_country'])
       str_date = self.CheckFolder.check_folder_csv('orders.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_products_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_products(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['product_id', 'product_name', 'supplier_id', 'category_id', 'quantity_per_unit', 
                                             'unit_price', 'units_in_stock', 'units_on_order', 'reorder_level', 'discontinued'])
       str_date = self.CheckFolder.check_folder_csv('products.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_region_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_region(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['region_id', 'region_description'])
       str_date = self.CheckFolder.check_folder_csv('region.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_shippers_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_shippers(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['shipper_id', 'company_name', 'phone'])
       str_date = self.CheckFolder.check_folder_csv('shippers.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_suppliers_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_suppliers(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['supplier_id', 'company_name', 'contact_name', 'contact_title', 'address', 
                                             'city', 'region', 'postal_code', 'country', 'phone', 'fax', 'homepage'])
       str_date = self.CheckFolder.check_folder_csv('suppliers.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_territories_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_territories(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['territory_id', 'territory_description', 'region_id'])
       str_date = self.CheckFolder.check_folder_csv('territories.csv')
       df.to_csv(str_date, index = False, header=True)
       
    def import_us_states_csv(self):
       df_dbase = []
       for dataframe in self.conn.select(self,(self.query.select_us_states(self))):
            df_dbase.append(dataframe)
       df = pd.DataFrame(df_dbase, columns= ['state_id', 'state_name', 'state_abbr', 'state_region'])
       str_date = self.CheckFolder.check_folder_csv('us_states.csv')
       df.to_csv(str_date, index = False, header=True)
       
       

# FileGetCsv().import_customers_csv()

