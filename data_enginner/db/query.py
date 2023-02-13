class Query():
            
    def select_categories(self):
        try:
            sql = "SELECT * FROM categories "
            return sql
        except Exception as e:
            print(e)
            