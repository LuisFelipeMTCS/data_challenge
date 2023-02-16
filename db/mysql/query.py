from db.mysql.conn import Conn
class Query():
    
    def __init__(self):
        self.conn = Conn()
            

            
    def insert_categories(self,data):
        try:
            sql = "INSERT INTO `mydb`.`categories`" \
                 "(`category_id`,`category_name`,`description`,`picture`)"\
                    "VALUES({},'{}','{}','{}');"
            sql = sql.format(int(data[0]),str(data[1]),str(data[2]),str(data[3]))
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_customer_customer_demo(self,data):
        try:
            sql = "INSERT INTO `mydb`.`customer_customer_demo`" \
                 "(`customer_id`,`customer_type_id`)"\
                    "VALUES({},'{}');"
            sql = sql.format(int(data[0]),int(data[1]))
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_customer_demographics(self,data):
        try:
            sql = "INSERT INTO `mydb`.`customer_demographics`" \
                 "(`trial_customer_id_1`,`customer_type_id`)"\
                    "VALUES({},'{}');"
            sql = sql.format(int(data[0]),int(data[1]))
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_customers(self,data):
        try:
            sql = "INSERT INTO `mydb`.`customers`" \
                 "(`customer_id`,`company_name`,`contact_name`,`contact_title`,`address`,"\
                 "`city`,`region`,`postal_code`,`country`,`phone`,`fax`)"\
                    "VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"
            sql = sql.format(str(data[0]),str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5])
                             ,str(data[6]),str(data[7]),str(data[8]),str(data[9]),str(data[10]))
            self.conn.insert(sql)
        except Exception as e:
            print(e)
            
    def insert_employee_territories(self,data):
        try:
            sql = "INSERT INTO `mydb`.`employee_territories`" \
                 "(`employee_id`,`territory_id`)"\
                 "VALUES({},'{}');"
            sql = sql.format(data[0],data[1])
            self.conn.insert(sql)
            
            return sql
        except Exception as e:
            print(e)
            
    def insert_employees(self,data):
        try:
            sql = "INSERT INTO `mydb`.`employees`" \
                 "(`employee_id`,`last_name`,`first_name`,`title`,`title_of_courtesy`,`birth_date`,"\
                 "`hire_date`,`address`,`city`,`region`,`postal_code`,`country`,`home_phone`,`extension`," \
                 "`photo`,`notes`,`reports_to`,`photo_path`)" \
                 "VALUES({},'{}','{}','{}','{}','{}'" \
                 ",'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"
            sql = sql.format(data[0],data[1],data[2],data[3],data[4],data[5]
                             ,data[6],data[7],data[8],data[9],data[10],data[11]
                             ,data[12],data[13],data[14],data[15],data[16],data[17])
            self.conn.insert(sql)
            
            return sql
        except Exception as e:
            print(e)
            
    def insert_orders(self,data):
        
        try:
            sql = "INSERT INTO `mydb`.`orders`" \
                 "(`order_id`,`customer_id`,`employee_id`,`order_date`,"\
                 "`required_date`,`shipped_date`,`ship_via`,`freight`," \
                 "`ship_name`,`ship_address`,`ship_city`,`ship_region`," \
                 "`ship_postal_code`,`ship_country`)"\
                 "VALUES({},'{}',{},'{}','{}','{}'" \
                 ",{},{},'{}','{}','{}','{}','{}','{}');"
            sql = sql.format(data[0],data[1],data[2],data[3],data[4],data[5]
                             ,data[6],data[7],data[8],data[9],data[10],data[11]
                             ,data[12],data[13])
            self.conn.insert(sql)
            
            return sql
        except Exception as e:
            print(e)
                   
    def insert_products(self,data):
        try:
            sql = "INSERT INTO `mydb`.`products`"\
                "(`product_id`,`product_name`,`supplier_id`,`category_id`,"\
                "`quantity_per_unit`,`unit_price`,`units_in_stock`,`units_on_order`,"\
                "`reorder_level`,`discontinued`)" \
                "VALUES({},'{}',{},{},'{}',{},{},{},{},{});"
            sql = sql.format(data[0],data[1],data[2],data[3],data[4],data[5]
                             ,data[6],data[7],data[8],data[9])
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_region(self,data):
        try:
            sql = "INSERT INTO `mydb`.`region`" \
                "(`region_id`,`region_description`)"\
                 "VALUES({},'{}');"
            sql = sql.format(data[0],data[1])
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_shippers(self,data):
        try:
            sql = "INSERT INTO `mydb`.`shippers`"\
                "(`shipper_id`,`company_name`,`phone`)"\
                "VALUES({},'{}','{}');"
            sql = sql.format(data[0],data[1],data[2])
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_suppliers(self,data):
        try:
            sql = "INSERT INTO `mydb`.`suppliers`" \
                "(`supplier_id`,`company_name`,`contact_name`,`contact_title`,"\
                "`address`,`city`,`region`,`postal_code`,`country`,`phone`,"\
                "`fax`,`homepage`)"\
                "VALUES({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"
            sql = sql.format(data[0],data[1],data[2],data[3],data[4]
                             ,data[5],data[6],data[7],data[8],data[9],data[10],data[11])
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_territories(self,data):
        try:
            sql = "INSERT INTO `mydb`.`territories`" \
                "(`territory_id`,`territory_description`,`region_id`)" \
                "VALUES('{}','{}',{});"
            sql = sql.format(data[0],data[1],data[2])
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_us_states(self,data):
        try:
            sql = "INSERT INTO `mydb`.`us_states`" \
                "(`state_id`,`state_name`,`state_abbr`,`state_region`)"\
                "VALUES({},'{}','{}','{}');"
            sql = sql.format(data[0],data[1],data[2],data[3])
            self.conn.insert(sql)
            return sql
        except Exception as e:
            print(e)
            
    def insert_order_details(self,data):
        try:
            sql = "INSERT INTO `mydb`.`order_details`" \
                  "(`order_id`,`product_id`,`unit_price`," \
                    "`quantity`,`discount`)"\
                  "VALUES({},{},{},{},{});" 
            sql = sql.format(int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4]))
            self.conn.insert(sql)
        except Exception as e:
            print(e)
# Query().insert_order_details()