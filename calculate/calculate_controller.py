from flask import Blueprint, jsonify, request
from calculate.calculate_service import add, divide, multiply, substract

operations = {"add": add, "substract": substract, "multiply": multiply, "divide": divide}


calculate_bp = Blueprint('calculate', __name__, url_prefix='/calculate')

know_languages = {
    'french': 'Salut',
    'english': 'Hello'
}

@calculate_bp.route('', methods=['GET'])
def calculate():
    
    a = request.args.get('a', '')
    b = request.args.get('b', '')
    op = request.args.get('operation', '')

    try:
        a = convert_number_to_float(a)
        b = convert_number_to_float(b)
    except:
        return jsonify({
            "success": False,
            "error": "a and b must be numbers"
        }), 400
    
    if op not in operations:
        return jsonify({
            "success": False,
            "error": "operation must be 'add', 'substract', 'multiply', 'divide'"
        }), 400
    
    if op == "divide"and b == 0:
        return jsonify({
            "success": False,
            "error": "can't divide by zeroed"
        }), 400

    calculation = operations.get(op)        

    return jsonify({
        "result": calculation(a, b)
    }), 200


def convert_number_to_float(number):
    return float(number)
        
