from datetime import datetime
#importamos la base de datos definida en app
from app import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_du = db.Column(db.Integer, nullable=False)
    email_du = db.Column(db.String(200), nullable = False)
    password_du = db.Column(db.String(200), nullable = False)
    users = db.relationship('Boleto', backref='boleto', lazy=True)

class Boleto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_u = db.Column(db.Integer, db.ForeignKey('users.id'))
    u_nombres = db.Column(db.String(200), nullable = False)

    a_salida = db.Column(db.String(10), nullable = False, default = 'Peru')
    a_destino = db.Column(db.String(100), nullable = False)
    a_hora_embarque = db.Column(db.String())
    a_fecha_vuelo = db.Column(db.String(10), nullable = False)

    asiento = db.Column(db.String(3), nullable = False)
    clase_vuelo = db.Column(db.Integer, nullable = False)

    registro_boleto = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)

class Avion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salida = db.Column(db.String(10),nullable = False, default = 'Peru')
    destino = db.Column(db.String(100), nullable = False)
    fecha_vuelo = db.Column(db.String(10), nullable = False)
    hora_embarque = db.Column(db.String(10), nullable = False)
    activo=db.Column(db.Boolean, nullable=False)

class Datos_User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    nombres = db.Column(db.String(200), nullable = False)
    apellidos = db.Column(db.String(200), nullable = False)
    telefono = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    fecha_registro = db.Column(db.DateTime, default = datetime.datetime.utcnow)

#--------------------------------------------------