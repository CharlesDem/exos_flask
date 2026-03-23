from flask import Blueprint, jsonify, request
from convert.convert_service import celsius_to_fahrenheit, fahrenheit_to_celsius

convert_bp = Blueprint('convert', __name__, url_prefix='/convert/temp')

temps = {'c2f': 'fahrenheit', 'f2c': 'celius'}

@convert_bp.route('', methods=['GET'])
def convert():

    try:
        value = float(request.args.get('value', ''))
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Value must be float"
        }), 400
    
    convert = request.args.get('convert', '').lower()

    if convert  not in temps:
        return jsonify({
            "success": False,
            "error": "c2f not valid"
        }), 400
    
    result = 0.0

    if convert == 'c2f':
        result = celsius_to_fahrenheit(value)
    else:
        result = fahrenheit_to_celsius(value)

    return jsonify({
            f"{temps.get(convert)}": result,
        }), 400