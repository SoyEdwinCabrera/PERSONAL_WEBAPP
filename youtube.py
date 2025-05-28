from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(f"Datos recibidos: {request.form}")  # Imprime todos los datos enviados por el formulario
        url = request.form.get('url')  # Usa .get() para evitar errores si el campo no existe
        
        if not url:  # Validar si el campo está vacío
            mensaje = "Por favor, ingresa una URL válida."
            return render_template('youtube.html', mensaje=mensaje)
        
        try: 
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            stream.download()
            
            mensaje = f"Descarga Completa!! Video guardado como {video.title}.mp4"
            return render_template('youtube.html', mensaje=mensaje)
            
        except Exception as e:
            mensaje = f"Error al descargar el video: {str(e)}"
            return render_template('youtube.html', mensaje=mensaje)
            
    return render_template('youtube.html')

            
if __name__ == '__main__':
    app.run(debug=True)

