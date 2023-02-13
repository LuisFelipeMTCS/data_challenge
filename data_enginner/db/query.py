class Query():
            
    def select_categories(self):
        try:
            sql = "SELECT * FROM categories "
            return sql
        except Exception as e:
            print(e)
            
    def select_customers(self):
        try:
            sql = "SELECT * FROM customers "
            return sql
        except Exception as e:
            print(e)
            
    def select_employee_territories(self):
        try:
            sql = "SELECT * FROM employee_territories"
            return sql
        except Exception as e:
            print(e)
            
    def select_employees(self):
        try:
            sql = "SELECT * FROM employees"
            return sql
        except Exception as e:
            print(e)
            
    def select_orders(self):
        try:
            sql = "SELECT * FROM orders"
            return sql
        except Exception as e:
            print(e)
            