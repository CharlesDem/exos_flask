from blog.blog_repository import repo_get_posts, repo_get_post, repo_create_post, repo_update_post, repo_delete_post



def get_posts():
    return repo_get_posts()


def get_post(post_id):
    return repo_get_post(post_id)


def create_post(data):
    return repo_create_post(data)


def update_post(post_id, data):
    return repo_update_post(post_id, data)


def delete_post(post_id):
    return repo_delete_post(post_id)