from db.mysql.conn import Conn
class Query():
    
    def __init__(self):
        self.conn = Conn()
            
    def insert_order_details(self,data):
        try:
            sql = "INSERT INTO `northwind`.`order_details`" \
                  "(`order_id`,`product_id`, `unit_price`, `quantity`, `discount`)" \
                  "VALUES({},{},{},{},{});" 
            sql = sql.format(int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4]))
            self.conn.insert(sql)
        except Exception as e:
            print(e)
            
    def insert_categories(self):
        try:
            sql = "insert * FROM categories "
            return sql
        except Exception as e:
            print(e)
            
    def insert_customer_customer_demo(self):
        try:
            sql = "insert * FROM customer_customer_demo "
            return sql
        except Exception as e:
            print(e)
            
    def insert_customer_demographics(self):
        try:
            sql = "insert * FROM customer_demographics "
            return sql
        except Exception as e:
            print(e)
            
    def insert_customers(self):
        try:
            sql = "insert * FROM customers "
            return sql
        except Exception as e:
            print(e)
            
    def insert_employee_territories(self):
        try:
            sql = "insert * FROM employee_territories"
            return sql
        except Exception as e:
            print(e)
            
    def insert_employees(self):
        try:
            sql = "insert * FROM employees"
            return sql
        except Exception as e:
            print(e)
            
    def insert_orders(self):
        try:
            sql = "insert * FROM orders"
            return sql
        except Exception as e:
            print(e)
            
    def insert_products(self):
        try:
            sql = "insert * FROM products"
            return sql
        except Exception as e:
            print(e)
            
    def insert_region(self):
        try:
            sql = "insert * FROM region"
            return sql
        except Exception as e:
            print(e)
            
    def insert_shippers(self):
        try:
            sql = "insert * FROM shippers"
            return sql
        except Exception as e:
            print(e)
            
    def insert_suppliers(self):
        try:
            sql = "insert * FROM suppliers"
            return sql
        except Exception as e:
            print(e)
            
    def insert_territories(self):
        try:
            sql = "insert * FROM territories"
            return sql
        except Exception as e:
            print(e)
            
    def insert_us_states(self):
        try:
            sql = "insert * FROM us_states"
            return sql
        except Exception as e:
            print(e)
            
            
# Query().insert_order_details()