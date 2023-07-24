import mysql.connector
class BancoDados:
    _host     = '127.0.0.1'
    _base     = 'test'
    _user     = 'root'
    _password = ''
    _conexao  = None 
    _table    = None
    _cursor   = None


    def __init__(self, table):       
        self._conexao = self.connect()
        self._table   = table
        

    def connect(self):
        con = mysql.connector.connect(
            host=self._host,
            database=self._base,
            user=self._user,
            password=self._password
        )

        if not con.is_connected:
            print("Erro ao conectar")
            exit
        else:        
            print("sucesso")  
            self._cursor = con
            return con
    
    def select(self, query):
        cursor = self._cursor.cursor()
        # print(query)
        cursor.execute(query)
        dados = cursor.fetchall()[0]
        cursor.close()
        return dados

    def insert(self, time, temporada):
        cursor = self._cursor.cursor()

        query = f'INSERT INTO {self._table} (time, temporada) VALUES ("{time}", "{temporada}")'     
        # print(query)  
        cursor.execute(query)
        self._conexao.commit()
        cursor.close()

    def newInsert(self, query):
        cursor  = self._cursor.cursor()
        # print(query)
        cursor.execute(query)
        self._conexao.commit()
        cursor.close()             
              
       
    def setTable(self, table):
        self._table = table
   

    @property
    def conexao(self):
        return self._conexao

    # comando = 'INSERT INTO '
