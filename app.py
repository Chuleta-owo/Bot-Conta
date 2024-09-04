
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    # Extraer el mensaje y el número de teléfono del mensaje entrante
    from_number = request.values.get('From')
    body = request.values.get('Body')
    
    # Aquí puedes procesar el mensaje usando tu IA
    response_message = f"Recibido: {body}"  # Ejemplo de respuesta, personalízala según tus necesidades

    # Crear una respuesta usando Twilio
    response = MessagingResponse()
    response.message(response_message)
    
    return str(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
