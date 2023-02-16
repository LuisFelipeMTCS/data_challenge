from pathlib import Path
from datetime import date
import os

class CheckFolder:
   
   def __init__(self):
      self.time = date.today()

    
   def check_folder_csv(self,file,filename):
       path = Path('data/postgres/'+ file + "/" +str(self.time)+"/")
       path.mkdir(parents=True, exist_ok=True)
       str_date = 'data/postgres/'+ file + "/" +str(self.time)+"/" + filename
       return str_date
   
   def check_folder_db(self,file,filename):
      path = os.path.join('data/postgres/'+ file + "/" + str(self.time) + "/", filename)
      if  (os.path.exists(path)):
         return path
      else:
         return False
      
   def check_folder_file(self,filename):
      
      path = Path('data/csv/'+ str(self.time))
      path.mkdir(parents=True, exist_ok=True)
      path = os.path.join('data/csv/'+ str(self.time) + "/", filename)
      if  (os.path.exists(path)):
         return path
      else:
         return False
      
   def check_folder_import_result(self,filename):
      
       path = Path('data/select_result/' +str(self.time)+"/")
       path.mkdir(parents=True, exist_ok=True)
       str_date = 'data/select_result/'+ str(self.time)+"/" + filename
       return str_date


     
# CheckFolder().check_folder_file("order_details.csv")
      
        
        