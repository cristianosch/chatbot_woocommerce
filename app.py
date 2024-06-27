from flask import Flask, request, jsonify
from flask_cors import CORS
from intents import get_response

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/chatbot', methods=['POST'])
def chatbot():    
    data = request.json
    user_message = data.get('message', '').lower()
    response_message = get_response(user_message)
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
