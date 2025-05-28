from flask import Flask, render_template
from flask_socketio import SocketIO

#TODO: Crear la aplicacion Flask 
app = Flask(__name__)

#TODO: Configuración de la clave secreta para sessiones
app.config["SECRET_KEY"] = "tu_clave_secreta_segura"

#TODO: Inicializar SocketIO con la aplicación Flask
socketIO = SocketIO(app)

mensajes = []

@app.route('/')
def index():
    return render_template('realtime.html', mensajes=mensajes)
    
@socketIO.on('mensaje')
def manejar_mensaje(data):
    #TODO: Obtener el nombre y el nuevo mensaje del dicicionario 'data'
    nombre = data['nombre']
    nuevo_mensaje = data['mensaje']
    
     # Add message to history
    mensajes.append(f"{nombre}: {nuevo_mensaje}")    
#TODO: Emitir un evento actualizar_mensajes a todos los clientes conectados
    socketIO.emit('actualizar_mensajes',{'nombre': nombre, 'mensaje': nuevo_mensaje})
    
#TODO: Ejecutar la aplicación Flask con el servidor SocketIO en modo depuración
if __name__ == '__main__':
    socketIO.run(app, debug=True)
    