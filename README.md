# flask

How WebAPP Works

1. **Initial Load**:
   - When a user visits the site, Flask renders the `realtime.html` template and passes any existing messages
   - The template displays any previous messages stored in the `mensajes` list

2. **Sending Messages**:
   - When a user enters their name and a message, then clicks "Enviar":
     - JavaScript prevents the normal form submission
     - It captures the name and message values
     - It sends this data to the server via a Socket.IO 'mensaje' event
     - It clears the message input field

3. **Server Processing**:
   - The server receives the 'mensaje' event with the name and message
   - It adds the formatted message to the `mensajes` list for history
   - It broadcasts an 'actualizar_mensajes' event to all connected clients

4. **Receiving Messages**:
   - All connected clients receive the 'actualizar_mensajes' event
   - Their JavaScript code creates a new list item with the message
   - This new message is appended to their message list

This cycle continues as users send more messages, creating a real-time chat experience where all connected users can see messages instantly without refreshing the page.