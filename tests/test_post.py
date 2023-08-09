from lib.post import Post

def test_creates_post():
    # Given the required post data
    # It creates a Post object.
    post = Post('Test title 1', 'Test content 1', 8, 1, 1)
    assert post.title == 'Test title 1'
    assert post.content == 'Test content 1'
    assert post.view_count == 8
    assert post.user_id == 1
    assert post.id == 1

def test_compares_contents():
    # Given two instances of Post
    # It compares the contents of these objects.
    post_1 = Post('Test title 1', 'Test content 1', 8, 1, 1)
    post_2 = Post('Test title 1', 'Test content 1', 8, 1, 1)
    assert post_1 == post_2

def test_returns_string():
    # Given a Post object
    # It returns a string containing it's veriables when the object is called.
    post = Post('Test title 1', 'Test content 1', 8, 1, 1)
    assert str(post) == "Test title 1, Test content 1, 8, 1, 1"
