class Author_of:
    def __init__(self, isbn, author_id):
        self.isbn = isbn
        self.author_id = author_id

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_author_id(self):
        return self.author_id

    def set_author_id(self, author_id):
        self.author_id = author_id

    def __str__(self):
        return str(self.isbn) + "\t" + str(self.author_id)
