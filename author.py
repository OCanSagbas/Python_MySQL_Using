class Author:
    def __init__(self, author_id, author_name):
        self.author_id = author_id
        self.author_name = author_name

    def get_author_id(self):
        return self.author_id

    def set_author_id(self, author_id):
        self.author_id = author_id

    def get_author_name(self):
        return self.author_name

    def set_author_name(self, author_name):
        self.author_name = author_name

    def __str__(self):
        return str(self.author_id) + "\t" + self.author_name