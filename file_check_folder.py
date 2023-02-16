from pathlib import Path
from datetime import date
import os

class CheckFolder:
   
   def __init__(self):
      self.time = date.today()

    
   def check_folder_csv(self,file):
       path = Path('data/csv/'+ str(self.time))
       path.mkdir(parents=True, exist_ok=True)
       str_date = 'data/csv/'+ str(self.time) + '/' + str(file)
       return str_date
   
   def check_folder_db(self,filename):
      path = os.path.join('data/csv/'+ str(self.time) + "/", filename)
      if  (os.path.exists(path)):
         return path
      else:
         return False
     
# CheckFolder().check_folder_db("customer_demographics.csv")
      
        
        