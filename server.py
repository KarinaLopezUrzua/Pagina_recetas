from tarea14 import app
from tarea14.controladores import controlador_usuarios, controlador_recetas
#importamos todos los controladores que usamos en la aplicacion

app.secret_key = 'mantener en secreto'

if __name__=="__main__":
    app.run(debug=True)  