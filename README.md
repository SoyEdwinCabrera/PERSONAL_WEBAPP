# Proyecto Flask: Aplicaciones Web con Múltiples Funcionalidades

Este proyecto es una colección de aplicaciones web desarrolladas con Flask que implementan diversas funcionalidades, desde un sistema de gestión de libros hasta un chat en tiempo real y una herramienta para descargar videos de YouTube.

## Tecnologías Utilizadas

- **Framework:** Flask
- **Base de Datos:** SQLite
- **Bibliotecas:** Flask-SQLAlchemy, pytube, Flask-SocketIO
- **Frontend:** HTML, CSS
- **Backend:** Python

## Instalaciones Necesarias

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

1. **Python:** Versión 3.7 o superior.
2. **pip:** Administrador de paquetes de Python.
3. Instala las siguientes bibliotecas:
   ```bash
   pip install flask flask-sqlalchemy pytube flask-socketio
   ```

## Funcionalidades del Proyecto

### **1. Hola Mundo**
#### Archivos:
- `hola_mundo.py`: Genera una página HTML directamente desde un string en Python.
- `hola_flask.py` y `templates/holaflask.html`: Genera una página HTML utilizando una plantilla.

#### Descripción:
- Muestra un mensaje de "Hola Mundo" en una página web.
- Ejemplo básico de cómo usar Flask para renderizar contenido HTML.

---

### **2. Gestión de Libros**
#### Archivos:
- `libros.py`: Código principal para la gestión de libros.
- `templates/libros.html`: Interfaz de usuario para agregar y visualizar libros.

#### Descripción:
- Permite agregar libros a una base de datos SQLite.
- Muestra una lista de libros almacenados.
- Incluye un formulario para ingresar el título y el autor de un libro.

---

### **3. Descarga de Videos de YouTube**
#### Archivos:
- `youtube.py`: Código principal para descargar videos de YouTube.
- `templates/youtube.html`: Interfaz de usuario para ingresar la URL del video.

#### Descripción:
- Permite descargar videos de YouTube en la resolución más alta disponible.
- Utiliza la biblioteca `pytube` para procesar y descargar videos.
- Incluye manejo de errores para garantizar que las solicitudes fallidas no interrumpan la aplicación.

---

### **4. Chat Simple**
#### Archivos:
- `chat.py`: Código principal para un chat básico.
- `templates/chat.html`: Interfaz de usuario para enviar y recibir mensajes.
- `static/chat.css`: Estilos para el chat.

#### Descripción:
- Permite enviar mensajes entre usuarios.
- Los mensajes se almacenan en una lista en memoria y se muestran en tiempo real.
- Utiliza sesiones para recordar el nombre del usuario.

---

### **5. Chat en Tiempo Real**
#### Archivos:
- `realtime.py`: Código principal para un chat avanzado en tiempo real.
- `templates/realtime.html`: Interfaz de usuario para enviar y recibir mensajes en tiempo real.
- `static/chat.css`: Estilos para el chat.

#### Descripción:
- Implementa un chat en tiempo real utilizando `Flask-SocketIO`.
- Los mensajes se transmiten instantáneamente a todos los usuarios conectados.
- Incluye manejo de eventos para actualizar la lista de mensajes en tiempo real.

---

### **6. Gestión de Tareas**
#### Archivos:
- `tareas.py`: Código principal para la gestión de tareas.
- `templates/tareas.html`: Interfaz de usuario para agregar y visualizar tareas.

#### Descripción:
- Permite agregar tareas a una lista en memoria.
- Muestra una lista de tareas pendientes.
- Incluye un formulario para ingresar nuevas tareas.

---

## Ejecución

Sigue estos pasos para ejecutar cualquiera de las aplicaciones incluidas en el proyecto:

1. Abre una terminal en el directorio del proyecto.
2. Asegúrate de que las bibliotecas necesarias estén instaladas:
   ```bash
   pip install flask flask-sqlalchemy pytube flask-socketio
   ```
3. Si estás utilizando un entorno virtual, actívalo:
   ```bash
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```
4. Ejecuta el archivo correspondiente a la funcionalidad que deseas probar. Por ejemplo:
   ```bash
   python hola_mundo.py       # Hola Mundo
   python libros.py           # Gestión de Libros
   python youtube.py          # Descarga de Videos de YouTube
   python chat.py             # Chat Simple
   python realtime.py         # Chat en Tiempo Real
   python tareas.py           # Gestión de Tareas
   ```
5. Abre tu navegador y ve a `http://127.0.0.1:500

---

## Solución de Problemas

### Error: HTTP Error 400: Bad Request
- Asegúrate de que la URL ingresada sea válida y accesible.
- Actualiza la biblioteca `pytube` con:
  ```bash
  pip install --upgrade pytube
  ```

## Estructura del Proyecto

```
python_flask/
├── app/
│   ├── __init__.py
│   ├── chat.py
│   ├── libros.py
│   ├── tareas.py
│   ├── youtube.py
│   ├── realtime.py
│   ├── hola_mundo.py
│   ├── hola_flask.py
├── templates/
│   ├── chat.html
│   ├── libros.html
│   ├── tareas.html
│   ├── youtube.html
│   ├── realtime.html
│   ├── holaflask.html
├── static/
│   ├── css/
│   │   ├── chat.css
├── README.md
├── requirements.txt
```

## Instalación de Dependencias

Este proyecto utiliza un archivo `requirements.txt` para gestionar las dependencias necesarias. Esto facilita la instalación de todas las bibliotecas requeridas con un solo comando.

### ¿Cómo instalar las dependencias?

1. Asegúrate de tener Python y pip instalados en tu sistema.
2. Abre una terminal en el directorio del proyecto.
3. Ejecuta el siguiente comando:
   ```bash
   pip install -r requirements.txt
   ```

--- 
## Solución de Problemas Comunes

### Error en la descarga de videos
- Verifica que el servidor Flask tenga permisos para escribir en el directorio actual.
- Especifica un directorio de descarga explícito en el código:
  ```python
  stream.download(output_path="/ruta/a/directorio/de/descarga")
  ```

### Problemas con SocketIO
- Asegúrate de que la biblioteca `Flask-SocketIO` esté instalada correctamente.
- Verifica que el puerto utilizado no esté bloqueado por un firewall.

---

## Créditos

- **Framework:** Flask
- **Bibliotecas utilizadas:** Flask-SQLAlchemy, pytube, Flask-SocketIO
- **Diseño de interfaz:** HTML y CSS