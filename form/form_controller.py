from flask import Blueprint, jsonify, request

from form.validator import validate_user

form_bp = Blueprint('form', __name__, url_prefix='/register')

@form_bp.route('', methods=['POST'])
def say_hello_in():

    data = request.get_json()

    errors = validate_user(data)
    
    if errors:
        return jsonify({
            "success": False,
            "errors": errors
        }), 400

    return jsonify({
        "succes": True,
    }), 200