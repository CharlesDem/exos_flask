from flask import Blueprint, Flask, request, jsonify
from blog.blog_service import get_posts,get_post,create_post,update_post,delete_post

blog_bp = Blueprint('blog', __name__, url_prefix='/posts')

@blog_bp.route("", methods=["GET"])
def route_get_posts():
    return jsonify(get_posts()), 200


@blog_bp.route("<int:post_id>", methods=["GET"])
def route_get_post(post_id):
    post = get_post(post_id)
    if not post:
        return jsonify({"error": "not found"}), 404
    return jsonify(post), 200


@blog_bp.route("", methods=["POST"])
def route_create_post():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content") or not data.get("author"):
        return jsonify({"error": "missing fields"}), 400

    post = create_post(data)
    return jsonify(post), 201


@blog_bp.route("<int:post_id>", methods=["PUT"])
def route_update_post(post_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "invalid body"}), 400

    post = update_post(post_id, data)

    if not post:
        return jsonify({"error": "not found"}), 404

    return jsonify(post), 200


@blog_bp.route("<int:post_id>", methods=["DELETE"])
def route_delete_post(post_id):
    success = delete_post(post_id)

    if not success:
        return jsonify({"error": "not found"}), 404

    return jsonify({"message": "deleted"}), 200