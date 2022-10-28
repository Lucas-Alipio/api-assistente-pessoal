import os
import json

from flask import Blueprint, request, jsonify

from flask_cors import CORS

from config import app, auth
from services.user import create_user



blueprint = Blueprint('app', __name__, url_prefix='/assistente-pessoal')

CORS(app)

'''----------------------------- USER -----------------------------'''
@blueprint.route('/user', methods=['POST', 'PUT'])
def create_user_route():
    response = json.dumps(request.json)
    return create_user(response)
    

@blueprint.route('/user', methods=['GET'])
@auth.login_required
def login_user_route():
    
    return auth.current_user()


'''--------------------------------------------------------------------------------'''
@app.route('/')
def status():
    return jsonify({
        "message": "Back-end Assistente Pessoal: Aplicação rodando!!!!!!"
    })


app.register_blueprint(blueprint)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)


#att requirements.txt
#pip freeze > requirements.txt