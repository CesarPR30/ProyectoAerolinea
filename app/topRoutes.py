#importamos nuestra app
from app import app
#para manipular fechas
from datetime import datetime
#para manipular regular expressions
import re
from flask_login import login_user
#importamos render_template y request para usarlos en nuestras rutas
from flask import render_template, request,  redirect, url_for
#importamos los modelos que vamos a usar en nuestras rutas
from app.models import User, Boleto, Avion
#importamos la db para mandar solicitudes
from app import db
#estos modulos son utiles para manejar APIs
import requests
import json
from flask_cors import CORS, cross_origin

from werkzeug.security import generate_password_hash, check_password_hash

#varias rutas pueden estar definidas por la misma funcion
@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET','POST'])
def register():
 if request.method == 'POST':
    mensaje = None
    nombre = request.form.get('nombre','')
    email = request.form.get('email','')
    apellidos = request.form.get('apellidos','')
    telefono = request.form.get('telefono','')
    password = request.form.get('password','')
    #se verifica si existen usuarios con ese email
    usuario = User.query.filter_by(email_du=email).first()
    if usuario is not None:
        mensaje = 'El correo ingresado ya esta asociado a una cuenta'
        return render_template('register.html',mensaje = mensaje)
    if len(str(password)) < 8 and len(str(telefono)) <9 or (len(str(telefono)) >10) :
        mensaje = 'La clave debe tener al menos 8 caracteres y el telefono entre 9 y 10'
        return render_template('register.html',mensaje = mensaje)
    elif len(str(password)) < 8:
        mensaje = 'La clave de tener al menos 8 caracteres'
        return render_template('register.html',mensaje = mensaje)
    elif len(str(telefono)) < 9 or len(str(telefono)) > 10:
        mensaje = 'El telefono debe tener al menos 9 digitos y no mas de 10'
        return render_template('register.html',mensaje = mensaje)
    datos_usuario = Datos_User(nombres=nombre,email=email,apellidos=apellidos,telefono=telefono,password=password)
    db.session.add(datos_usuario)
    db.session.commit()
    nuevo_usuario = User(id_du=datos_usuario.id,email_du=email,password_du=generate_password_hash(password, method='sha256'))
    db.session.add(nuevo_usuario)
    db.session.commit()
    mensaje = 'Se creo su cuenta correctamente'
    return render_template('register.html',mensaje = mensaje)
 return render_template('register.html')

@app.route('/login', methods = ['GET','POST'])
def login():
 if request.method == 'GET':
    mensaje = None
    return render_template('login.html')
 else:
    du_email = request.form.get('du_email')
    du_password = request.form.get('du_password')
    data = User.query.filter_by(email_du=du_email).first()
    if not data or not check_password_hash(data.password_du, du_password):
     mensaje = 'Verifique los datos ingresados'
     return render_template('login.html',mensaje = mensaje)
    login_user(data)
    return redirect(url_for('profile'))

@app.route('/vuelos',methods=['GET'])
def vuelos():
    return render_template('vuelos.html')

@app.route('/vuelos/procesar', methods = ['GET','POST'])
def vuelos_procesar():
 if request.method == 'POST':
    asientos = request.form.get('nombre','')
    clase_vuelos = request.form.get('email','')
    registro_boletos = request.form.get('apellidos','')

    datos_usuario = Boleto(asiento=asientos,clase_vuelo=clase_vuelos,registro_boleto=registro_boletos)
    db.session.add(datos_usuario)
    db.session.commit()
    mensaje = 'Se añadio su vuelo correctamente'
    return render_template('procesar.html',mensaje = mensaje)
 return render_template('procesar.html')

@app.route('/mi_cuenta', methods=['GET'])
def profile():
    return render_template('mi_cuenta.html')

@app.route('/hoteles', methods=['GET'])
def hoteles():
    return render_template('hoteles.html')
    

#@app.route('/options', methods=['GET', 'POST'])
#def home():
		#if request.method == 'POST':
			#return render_template('option.html') 
		#return render_template('option.html')