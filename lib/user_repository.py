from lib.user import User

class UserRepository():
    def __init__(self, connection):
        # Stores the connection data to the database
        #
        # Parameters
        #   connection: a connection object
        self._connection = connection

    def all(self):
        # Given a database of users
        # It retreives a list of all current users.
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["username"], row["email_address"], row["id"])
            users.append(item)
        return users

    def create(self, user):
        # Given a User object
        # It adds the object to the users table.
        self._connection.execute(
            'INSERT INTO users (username, email_address) VALUES (%s, %s)',
            [user.username, user.email_address]
            )

    def find(self, user_id):
        # Returns the relevent User object for the specified user_id.
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["username"], row["email_address"], row["id"])
