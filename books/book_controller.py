from flask import Blueprint, jsonify, request
from books.book_service import add_book, get_book, get_books

books_bp = Blueprint('books', __name__, url_prefix='/books')


@books_bp.route('', methods=['GET'])
def books():
    return jsonify([book.to_dict() for book in get_books()]), 200

@books_bp.route('/<id>', methods=['GET'])
def book(id):
    if (not id.isdigit() or int(id) < 1):
        return jsonify({
            "success": False,
            "error": "id must at least be 1 or greater"
        }), 400
    try:
        return jsonify(get_book(id).to_dict()), 200
    except:
        return jsonify({
            "success": False,
            "error": "Wrong book index"
        }), 400

@books_bp.route('', methods=['POST'])
def controller_add_book():

    data = request.get_json()

    if not data.get('name') or not data.get('author'):
        return jsonify({
            "success": False,
            "error": "Missing required fields: name, author"
        }), 400
    

    return jsonify(add_book(data['author'], data['name']).to_dict()), 201