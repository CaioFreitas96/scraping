import sys
sys.path.insert(1, './classe')
from bd import BancoDados

class crud:
    _db    = None
    _table = None
    def __init__(self):       
        self._db    = BancoDados("times")  
        self._table = self._db._table

    def select(self, query):
        return self._db.select(query)       
        

    def inserir(self, time, temporada):
        self._db.insert(time, temporada)

    def newInsert(self, arrays):        
        query    = f'INSERT INTO {self._table} '
        contador = 0
        for array in arrays:   
            if contador == 0:
                query += '('+array  
            else:
                query += ', '+array  

            contador += 1

        query += ') VALUES ('
        
        contador = 0
        for array in arrays:
            if contador == 0:
                query += "'"+str(arrays[array])+"'"
            else:
                query += ", '"+str(arrays[array])+"'"
             
            contador += 1
        
        query += ')'

        self._db.newInsert(query)

    def setTable(self, table):
        self._table = table
       
    
    
        




    

    