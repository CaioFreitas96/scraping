import sys
sys.path.insert(1, './classe')
from bd import BancoDados

class crud:
    _db = None
    def __init__(self):       
        self._db = BancoDados("times")  

    def select(self):
        dados = self._db.select()       
        print(dados)

    def inserir(self, time, temporada):
        self._db.insert(time, temporada)

    def newInsert(self, arrays):
        self._db.newInsert(arrays)

    
    
        




    

    