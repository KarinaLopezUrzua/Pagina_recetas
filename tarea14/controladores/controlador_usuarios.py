from tarea14 import app
from flask import render_template, redirect, session, request 
from tarea14.modelos.clases_usuarios import Usuarios
from tarea14.modelos.clases_recetas import Recetas #importamos la clase de recetas para obtener todas las recetas
from flask import jsonify

from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

#RUTAS FORMULARIO READ
@app.route("/") 
def formulario_raiz():
    return render_template("formulario.html") #Pagina inicio se dirige a html hijo

#RUTA CREAD
@app.route("/crear", methods=["POST"]) #ruta que se redigire action del formulario
def crear_usuario():
    contrasena_encriptada = bcrypt.generate_password_hash(request.form['contraseña'])
    print(contrasena_encriptada)
    datos = { #creamos un diccionario que obtendra la informacion de nuestro formulario
        "nombre":request.form["nombre"], #["nombre"] es el name que se coloco en el imput del formulario
        "apellido":request.form["apellido"],
        "fecha_nacimiento":request.form["fnacimiento"],
        "email":request.form["email"],
        "contraseña": contrasena_encriptada, 
    }
    print(datos)
    if not Usuarios.validar_formulario(request.form): #validacion
        print(datos)
        # redirigir a la ruta donde se renderiza el formulario 
        return redirect('/')
    id_usuario = Usuarios.registro_usuario(datos) #le agregamos una variable para poder retornar un numero y asi traquear al usuario para darle seguimiento con session. se llama al metodo para guardar la informacion en la base de datos
    print(id_usuario)
    session["id_usuario"] = id_usuario #estamos almacenando la variable en una clave llamada id_usuario. esta llave va a contener el numero del usuario creado
    return redirect(f"/usuario/{session['id_usuario']}") #se redirige a la pagina donde se muestra la informacion del usuario con su id a traves de id_usuario
#tenemos que concatenar, con formart y comillas simples

#ruta para ingresar usuario registrado ##revisar min 0.35.36
@app.route("/ingresar", methods=["POST"])
def ingreso_usuario():
    datos = {"email":request.form["email"]}
    usuario = Usuarios.obtener_por_email(datos) #le agregamos una variable para poder retornar un numero y asi traquear al usuario para darle seguimiento con session. se llama al metodo para guardar la informacion en la base de datos
    if not usuario: #si no encuentra un mail compatible no se loguea
        flash("ATENCIÓN: Email/Contraseña Invalidos") #se debe colocar asi para que sea generico
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.contraseña, request.form['contraseña']):
        # si obtenemos False después de verificar la contraseña
        flash("ATENCIÓN: Email/Contraseña Invalidos")
        return redirect('/')
    #flash("FELICIDADES: ¡Te has logueado satisfactoriamente!")
    session["id_usuario"] = usuario.id #estamos almacenando la variable en una clave llamada id_usuario. esta llave va a contener el numero del usuario creado
    return redirect(f"/usuario/{session['id_usuario']}") #se redirige a la pagina donde se muestra la informacion del usuario

#ruta read para mostrar la informacion de un usuario
@app.route("/usuario/<int:id_usuario>")
def ver_usuario(id_usuario):
    if "id_usuario" not in session:
        return redirect("/")
    if id_usuario != session["id_usuario"]: #si alguien coloca otro id en la url se va a rediriguir
        return redirect("/")
    datos = {
        "id_usuario": id_usuario
    }
    ver_usuario = Usuarios.obtener_un_usuario(datos)
    session["nombre_usuario"] = ver_usuario.nombre
    #todas_las_recetas = Recetas.obtener_todas_recetas() lo teniamos antes para obtener solo las recetas, no estaban ligadas al usuario
    todas_las_recetas_con_usuario = Recetas.obtener_recetas_con_usuario()
    return render_template("info_recetas.html", lista_recetas=todas_las_recetas_con_usuario, id_usuario=session["id_usuario"])

@app.errorhandler(404)
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

@app.route("/borrar_sesion") #elimina el contenido almacenado en todas las sesiones
def eliminar_sesion():
    session.clear()
    return redirect("/")
