from import_csv import ImportCsv
import MySQLdb



class Main():
    def __init__(self):
        self.import_csv = ImportCsv()
    
    def process(self):
    
        self.import_csv.import_categories_csv()
        self.import_csv.import_customer_customer_demo_csv()
        self.import_csv.import_customer_demographics_csv()
        self.import_csv.import_customers_csv()
        self.import_csv.import_employee_territories_csv()
        self.import_csv.import_employees_csv()
        self.import_csv.import_orders_csv()
        self.import_csv.import_products_csv()
        self.import_csv.import_us_states_csv()
        self.import_csv.import_shippers_csv()
        self.import_csv.import_suppliers_csv()
        self.import_csv.import_region_csv()
        self.import_csv.import_territories_csv()
    
    
    
Main().process()