class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name

    def get_publisher_id(self):
        return self.publisher_id

    def set_publisher_id(self, publisher_id):
        self.publisher_id = publisher_id

    def get_publisher_name(self):
        return self.publisher_name

    def set_publisher_name(self, publisher_name):
        self.publisher_name = publisher_name

    def __str__(self):
        return f"{self.publisher_id}\t{self.publisher_name}"
