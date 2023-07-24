import sys
sys.path.insert(1, './')
from crud import crud

class algoritmoModel:
    db    = None
    table = None
    def __init__(self):
        self.db    = crud()
        self.table = self.db._table
    

    def getTimes(self, time):
        query = "SELECT * FROM " + self.table
        if(time):
            query += " WHERE time = '"+time+"'" 

        return self.db.select(query)
       
    def setTable(self, table):
        self.table = table
        print("set table")
        print(self.table)
