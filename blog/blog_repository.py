from datetime import datetime

posts = []
next_id = 1


def now_iso():
    return datetime.utcnow().isoformat()


def repo_get_posts():
    return posts


def repo_get_post(post_id):
    return next((p for p in posts if p["id"] == post_id), None)


def repo_create_post(data):
    global next_id

    post = {
        "id": next_id,
        "title": data["title"],
        "content": data["content"],
        "author": data["author"],
        "created_at": now_iso(),
        "updated_at": now_iso()
    }

    posts.append(post)
    next_id += 1

    return post


def repo_update_post(post_id, data):
    post = repo_get_post(post_id)
    if not post:
        return None

    if "title" in data:
        post["title"] = data["title"]
    if "content" in data:
        post["content"] = data["content"]
    if "author" in data:
        post["author"] = data["author"]

    post["updated_at"] = now_iso()

    return post


def repo_delete_post(post_id):
    global posts
    post = repo_get_post(post_id)

    if not post:
        return False

    posts = [p for p in posts if p["id"] != post_id]
    return True