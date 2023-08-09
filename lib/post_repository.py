from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        # Stores the connection object for the database
        #
        # Parameters:
        #   connection: a connection object
        self._connection = connection

    def all(self):
        # Pulls all data from the posts table.
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row["title"], row["content"], row["view_count"], row["user_id"], row["id"])
            posts.append(item)
        return posts

    def create(self, post):
        # Creates a new post.
        self._connection.execute(
            'INSERT INTO posts (title, content, view_count, user_id) VALUES (%s, %s, %s, %s)',
            [post.title, post.content, post.view_count, post.user_id]
        )
