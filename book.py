class Book:
    def __init__(self, isbn, book_name, publisher_id, first_publish_year, page_count, category, rating):
        self.isbn = isbn
        self.book_name = book_name
        self.publisher_id = publisher_id
        self.first_publish_year = first_publish_year
        self.page_count = page_count
        self.category = category
        self.rating = rating

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_book_name(self):
        return self.book_name

    def set_book_name(self, book_name):
        self.book_name = book_name

    def get_publisher_id(self):
        return self.publisher_id

    def set_publisher_id(self, publisher_id):
        self.publisher_id = publisher_id

    def get_first_publish_year(self):
        return self.first_publish_year

    def set_first_publish_year(self, first_publish_year):
        self.first_publish_year = first_publish_year

    def get_page_count(self):
        return self.page_count

    def set_page_count(self, page_count):
        self.page_count = page_count

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    def __str__(self):
        return f"{self.isbn}\t{self.book_name}\t{self.publisher_id}\t{self.first_publish_year}\t{self.page_count}\t{self.category}\t{self.rating}"
