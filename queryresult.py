class QueryResult:
    class ResultQ1:
        def __init__(self, isbn, first_publish_year, page_count, publisher_name):
            self.isbn = isbn
            self.first_publish_year = first_publish_year
            self.page_count = page_count
            self.publisher_name = publisher_name

        def __str__(self):
            return f"{self.isbn}\t{self.first_publish_year}\t{self.page_count}\t{self.publisher_name}"

    class ResultQ2:
        def __init__(self, publisher_id, average_page_count):
            self.publisher_id = publisher_id
            self.average_page_count = average_page_count

        def __str__(self):
            return f"{self.publisher_id}\t{self.average_page_count}"

    class ResultQ3:
        def __init__(self, book_name, category, first_publish_year):
            self.book_name = book_name
            self.category = category
            self.first_publish_year = first_publish_year

        def __str__(self):
            return f"{self.book_name}\t{self.category}\t{self.first_publish_year}"

    class ResultQ4:
        def __init__(self, publisher_id, category):
            self.publisher_id = publisher_id
            self.category = category

        def __str__(self):
            return f"{self.publisher_id}\t{self.category}"

    class ResultQ5:
        def __init__(self, author_id, author_name):
            self.author_id = author_id
            self.author_name = author_name

        def __str__(self):
            return f"{self.author_id}\t{self.author_name}"

    class ResultQ6:
        def __init__(self, author_id, isbn):
            self.author_id = author_id
            self.isbn = isbn

        def __str__(self):
            return f"{self.author_id}\t{self.isbn}"

    class ResultQ7:
        def __init__(self, publisher_id, publisher_name):
            self.publisher_id = publisher_id
            self.publisher_name = publisher_name

        def __str__(self):
            return f"{self.publisher_id}\t{self.publisher_name}"

    class ResultQ8:
        def __init__(self, isbn, book_name, rating):
            self.isbn = isbn
            self.book_name = book_name
            self.rating = rating

        def __str__(self):
            return f"{self.isbn}\t{self.book_name}\t{self.rating}"
