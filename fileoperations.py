import os
from author import Author
from author_of import Author_of
from publisher import Publisher
from book import Book



class FileOperations:
    @staticmethod
    def create_file_writer(path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        file_writer = open(path, "w")
        return file_writer

    @staticmethod
    def read_author_file(path_to_file):
        author_list = []

        try:
            with open(path_to_file, "r") as file_reader:
                for line in file_reader:
                    words = line.strip().split("\t")
                    if len(words) >= 2:
                        author_list.append(Author(int(words[0]), words[1]))
                    else:
                        print("There is a problem in Author File Reading phase")

        except IOError as e:
            print("Error reading file:", e)

        return author_list

    @staticmethod
    def read_publisher_file(path_to_file):
        publisher_list = []

        try:
            with open(path_to_file, "r") as file_reader:
                for line in file_reader:
                    words = line.strip().split("\t")
                    if len(words) >= 2:
                        publisher_list.append(Publisher(int(words[0]), words[1]))
                    else:
                        print("There is a problem in Publisher File Reading phase")

        except IOError as e:
            print("Error reading file:", e)

        return publisher_list

    @staticmethod
    def read_book_file(path_to_file):
        book_list = []

        try:
            with open(path_to_file, "r") as file_reader:
                for line in file_reader:
                    words = line.strip().split("\t")
                    if len(words) >= 7:
                        book_list.append(Book(words[0], words[1], int(words[2]), words[3], int(words[4]), words[5], float(words[6])))
                    else:
                        print("There is a problem in Book File Reading phase")

        except IOError as e:
            print("Error reading file:", e)

        return book_list

    @staticmethod
    def read_author_of_file(path_to_file):
        author_of_list = []

        try:
            with open(path_to_file, "r") as file_reader:
                for line in file_reader:
                    words = line.strip().split("\t")
                    if len(words) >= 2:
                        author_of_list.append(Author_of(words[0], int(words[1])))
                    else:
                        print("There is a problem in Author_of File Reading phase")

        except IOError as e:
            print("Error reading file:", e)

        return author_of_list
