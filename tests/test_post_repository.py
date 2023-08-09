from lib.post_repository import PostRepository
from lib.post import Post
from lib.user_repository import UserRepository
from lib.user import User

def test_return_all_posts(db_connection):
    # Given a table of posts
    # It returns a list of all entries in the table.
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post('Test title 1', 'Test content 1', 8, 1, 1),
        Post('Test title 2', 'Test content 2', 7, 1, 2),
        Post('Test title 3', 'Test content 3', 6, 2, 3),
        Post('Test title 4', 'Test content 4', 5, 2, 4),
        Post('Test title 5', 'Test content 5', 4, 3, 5),
        Post('Test title 6', 'Test content 6', 3, 3, 6),
        Post('Test title 7', 'Test content 7', 2, 4, 7),
        Post('Test title 8', 'Test content 8', 1, 4, 8)
    ]

def test_create_new_post(db_connection):
    # Given a User and Post object
    # It creates a post with the user_id determined by User.
    db_connection.seed("seeds/social_network.sql")
    post_repository = PostRepository(db_connection)
    user_repository = UserRepository(db_connection)
    user = user_repository.find(1)
    post = Post('Test title 9', 'Test content 9', 0, user.id)
    post_repository.create(post)
    posts = post_repository.all()
    assert posts == [
        Post('Test title 1', 'Test content 1', 8, 1, 1),
        Post('Test title 2', 'Test content 2', 7, 1, 2),
        Post('Test title 3', 'Test content 3', 6, 2, 3),
        Post('Test title 4', 'Test content 4', 5, 2, 4),
        Post('Test title 5', 'Test content 5', 4, 3, 5),
        Post('Test title 6', 'Test content 6', 3, 3, 6),
        Post('Test title 7', 'Test content 7', 2, 4, 7),
        Post('Test title 8', 'Test content 8', 1, 4, 8),
        Post('Test title 9', 'Test content 9', 0, 1, 9)
    ]
