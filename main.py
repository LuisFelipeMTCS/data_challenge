from file_get_csv import FileGetCsv
from file_send_csv import FileSendCsv



class Main():
    def __init__(self):
        self.import_csv = FileGetCsv()
        self.send_csv = FileSendCsv()
    
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
        
        self.send_csv.send_categories_csv()
        self.send_csv.send_customer_customer_demo_csv()
        self.send_csv.send_customer_demographics_csv()
        self.send_csv.send_customers_csv()
        self.send_csv.send_employee_territories_csv()
        self.send_csv.send_employees_csv()
        self.send_csv.send_products_csv()
        self.send_csv.send_orders_csv()
        self.send_csv.send_shippers_csv()
        self.send_csv.send_region_csv()
        self.send_csv.send_suppliers_csv()
        self.send_csv.send_territories_csv()
        self.send_csv.send_us_states_csv()
        
        
        self.send_csv.send_order_details_csv()
    
    
Main().process()