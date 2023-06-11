from conftest import get_all_posts, get_my_posts, create_post


def test_get_posts(token):
	posts = get_all_posts(token)
	assert posts


def test_post_creation(token):
	create_post(token, "NEW TITLE", "NEW DESCRIPTION", "NEW CONTENT")
	posts = get_my_posts(token)
	assert "NEW CONTENT" in posts
	


