from flask import Blueprint, jsonify

hello_bp = Blueprint('hello', __name__, url_prefix='/hello')

know_languages = {
    'french': 'Salut',
    'english': 'Hello'
}

@hello_bp.route('<language>', methods=['GET'])
def say_hello_in(language: str):
    language = language.lower()
    if not language or language not in know_languages.keys():
        return jsonify({
            "success": False,
            "error": f"Language param not ok"
        }), 400

    return jsonify({
        "message": know_languages.get(language),
        "language": language
    }), 200