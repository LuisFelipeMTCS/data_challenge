from pathlib import Path
from datetime import date

class CheckFolder:
    
    def check_folder_csv(self,file):
       time = date.today()
       path = Path('data/csv/'+ str(time))
       path.mkdir(parents=True, exist_ok=True)
       str_date = 'data/csv/'+ str(time) + '/' + str(file)
       return str_date