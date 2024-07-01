# Importo el conector a la base de datos
from app.database import get_db
#Creo una clase usuario
class Usuario:
    def __init__(self):
        self.id_usuario
        self.apellido
        self.nombre
        self.email
        self.fecha_nacimiento
        self.clave
        self.genero
    #Sirve tanto para guardar los cambios de una actualizacion de datos como para crear un nuevo usuario
    def grabar(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_usuario:
            cursor.execute("""
            UPDATE usuarios SET apellido = %s, nombre = %s, email = %s, fecha_nacimiento = %s, clave = %s, genero =%s
            WHERE id_usuario = %s
            """, (self.apellido,
                self.nombre,
                self.email,
                self.fecha_nacimiento,
                self.clave,
                self.genero))
        else:
            cursor.execute("""
            INSERT INTO usuarios (apellido, nombre, email, fecha_nacimiento, clave, genero) VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.apellido, 
                  self.nombre,
                self.email,
                self.fecha_nacimiento,
                self.clave,
                self.genero))
            self.id_usuario = cursor.lastrowid
        db.commit()
        cursor.close()
    #Borrar un un usario por si id
    def borrar(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (self.id_usuario,))
        db.commit()
        cursor.close()
    #Traigo un usuario por su ID
    def perfil(usuario_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario= %s", (usuario_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], email=row[3], fecha_nacimiento=row[4], clave=row[5], genero=row[6])
        return None
    # Metodo para traer todos los usuarios
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [Usuario(id_usuario=row[0], apellido=row[1], nombre=row[2], email=row[3], fecha_nacimiento=row[4], clave=row[5], genero=row[6])
        for row in rows]
        cursor.close()
        return usuarios
    # creo un metodo que devuelva los atributos de la instancia de usuario en formato json usando como clave los nombres de las columnas en la base de datos
    def serialize(self):
        return {
        'id_usuario': self.id_usuario,
        'apellido': self.apellido,
        'nombre': self.nombre,
        'email': self.email,
        'fecha_nacimiento': self.fecha_nacimiento,
        'clave': self.clave,
        'genero': self.genero,
        }