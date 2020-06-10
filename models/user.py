from database.connection import Conexion
from bcrypt import checkpw

conn = Conexion()
Model = conn.model()

class users(Model):
    __table__ = 'usuarios'
    __primary_key__ = 'id_usuario'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id_uduario']

    __fillable__ = ['username', 'pwd', 'nombre', 'apellido', 'edad', 'cargo']

    __casts__ = {
        'username': 'str',
        'pwd': 'str',
        'name': 'str',
        'last_name': 'str',
        'age': 'int',
        'cargo' : 'str'
    }

    __hidden__ = ['pwd']

    def password_valid(self, pwd):
        return checkpw(pwd.encode('utf-8'), self.pwd.encode('utf-8'))
