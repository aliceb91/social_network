class Post():
    def __init__(self, title, content, view_count, user_id, id = None):
        # Creates a new Post object using the nessecary data for the post.
        #
        # Parameters:
        #   title: string
        #   content: string
        #   view_count: int
        #   user_id: int
        self.title = title
        self.content = content
        self.view_count = view_count
        self.user_id = user_id
        self.id = id

    def __eq__(self, other):
        # Compares the instance variables of two Post objects.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Returns the instance variables as a string when called.
        return f"{self. title}, {self.content}, {self.view_count}, {self.user_id}, {self.id}"
