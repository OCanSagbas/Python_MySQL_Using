import mysql.connector
from ibookdb import IBOOKDB
from queryresult import QueryResult

class BOOKDB(IBOOKDB):

    def __init__(self,user,password,host,database,port):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.connection = None

    def initialize(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database,
            port=self.port
        )

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def createTables(self):
        table_count = 0
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS authors (
                       author_id INT PRIMARY KEY,
                       author_name VARCHAR(60)
                       )""") 
        table_count += 1
        cursor.execute("""CREATE TABLE IF NOT EXISTS publishers (
                       publisher_id INT PRIMARY KEY,
                       publisher_name VARCHAR(50)
                       )""")
        table_count += 1
        cursor.execute("""CREATE TABLE IF NOT EXISTS books (
                       isbn CHAR(13) PRIMARY KEY,
                       book_name VARCHAR(120),
                       publisher_id INT,
                       first_publish_year CHAR(4),
                       page_count INT,
                       category VARCHAR(25),
                       rating FLOAT,
                       FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
                       )""")
        table_count += 1
        cursor.execute("""CREATE TABLE IF NOT EXISTS phw1 (
                       isbn CHAR(13),
                       book_name VARCHAR(120),
                       rating FLOAT
                       )""")
        table_count += 1
        cursor.execute("""CREATE TABLE IF NOT EXISTS author_ofs (
                       isbn CHAR(13),
                       author_id INT,
                       PRIMARY KEY (isbn, author_id),
                       FOREIGN KEY (isbn) REFERENCES books(isbn),
                       FOREIGN KEY (author_id) REFERENCES authors(author_id)
                       )""")
        table_count += 1
        cursor.close()
        return table_count
    def dropTables(self):
        table_count = 0
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS author_ofs;")
        table_count += 1
        cursor.execute("DROP TABLE IF EXISTS books;")
        table_count += 1
        cursor.execute("DROP TABLE IF EXISTS phw1;")
        table_count += 1
        cursor.execute("DROP TABLE IF EXISTS authors;")
        table_count += 1
        cursor.execute("DROP TABLE IF EXISTS publishers;")
        table_count += 1
        cursor.close()
        return table_count

    def insertAuthor(self,authors):
        cursor = self.connection.cursor()
        inserted_count = 0
        if not self.connection:
            raise Exception("Database connection is not initialized.")
        for author in authors:
            sql= "INSERT INTO authors (author_id, author_name) VALUES (%s,%s)"
            values= (author.author_id,author.author_name)
            cursor.execute(sql,values)
            self.connection.commit()
            inserted_count += 1
        cursor.close()
        return inserted_count
    def insertBook(self,books):
        cursor = self.connection.cursor()
        inserted_count = 0
        for book in books:
            sql= "INSERT INTO books (isbn, book_name, publisher_id, first_publish_year, page_count, category, rating) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values= (book.isbn, book.book_name, book.publisher_id, book.first_publish_year, book.page_count, book.category, book.rating)
            cursor.execute(sql,values)
            self.connection.commit()
            inserted_count += 1
        cursor.close()
        return inserted_count
    def insertPublisher(self,publishers):
        cursor = self.connection.cursor()
        inserted_count = 0
        for publisher in publishers:
            sql= "INSERT INTO publishers (publisher_id, publisher_name) VALUES (%s,%s)"
            values= (publisher.publisher_id, publisher.publisher_name)
            cursor.execute(sql,values)
            self.connection.commit()
            inserted_count += 1
        cursor.close()
        return inserted_count
    def insertAuthor_of(self,author_ofs):
        cursor = self.connection.cursor()
        inserted_count = 0
        for author_of in author_ofs:
            sql= "INSERT INTO author_ofs (isbn, author_id) VALUES (%s,%s)"
            values= (author_of.isbn, author_of.author_id)
            cursor.execute(sql,values)
            self.connection.commit()
            inserted_count += 1
        cursor.close()
        return inserted_count
    def functionQ1(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT MAX(page_count) FROM books;")
        max_page_count = cursor.fetchone()[0]
        cursor.execute("""
                       SELECT b.isbn, b.first_publish_year, b.page_count, p.publisher_name
                       FROM books b
                       JOIN publishers p ON b.publisher_id = p.publisher_id
                       WHERE b.page_count = %s
                       ORDER BY b.isbn;
                       """, (max_page_count,))
        results = []
        for (isbn, first_publish_year,page_count, publisher_name) in cursor:
            results.append(QueryResult.ResultQ1(isbn, first_publish_year, page_count, publisher_name))
        cursor.close()
        return results    
    def functionQ2(self,author_id1, author_id2):
        # İlk olarak, iki yazar tarafından ortak yazılan kitapları yayımlayan yayınevleri bul
        # Bulunan yayınevlerinin ID'lerini bir listeye al
        # Bu yayınevlerinin yayımladığı tüm kitapların ortalama sayfa sayısını hesapla

        cursor = self.connection.cursor()
        cursor.execute("""
                        SELECT p.publisher_id
                        FROM books b
                        JOIN publishers p ON p.publisher_id = b.publisher_id
                        JOIN author_ofs ao ON ao.isbn = b.isbn
                        WHERE ao.author_id IN (%s, %s)
                        GROUP BY p.publisher_id, b.isbn
                        HAVING COUNT(DISTINCT ao.author_id) = 2
                        """, (author_id1, author_id2))
        publisher_ids = []
        for row in cursor.fetchall():
            publisher_ids.append(row[0])
        results = []
        for publisher_id in publisher_id:
            cursor.execute("""
                           SELECT AVG(b.page_count)
                           FROM books b
                           WHERE b.publisher_id = %s
                           """,(publisher_id,))
            avg_page_count = cursor.fetchone()[0]
            result = QueryResult.ResultQ2(publisher_id, avg_page_count)
            results.append(result)
        cursor.close()
        return results
    def functionQ3(self,author_name):
        cursor = self.connection.cursor()
        sql =   """
                SELECT b.book_name, b.category, b.first_publish_year
                FROM books b
                JOIN author_ofs ao ON  b.isbn = ao.isbn 
                JOIN authors a ON a.author_id = ao.author_id
                WHERE a.author_name = (%s) AND b.first_publish_year =
                    (SELECT MIN(b2.first_publish_year)
                    FROM books b2
                    JOIN author_ofs ao2 ON b2.isbn = ao2.isbn
                    JOIN authors a2 ON a2.author_id = ao2.author_id
                    WHERE a2.author_name = %s
                    )
                ORDER BY b.book_name, b.category, b.first_publish_year
                """
        cursor.execute(sql,(author_name,author_name))
        rows = cursor.fetchall()
        results = [QueryResult.ResultQ3(book_name=row[0], category=row[1], first_publish_year=row[2]) for row in rows]
        cursor.close()
        return results
    def functionQ4(self):
        cursor = self.connection.cursor()
        cursor.execute("""
                SELECT p.publisher_id, b.category
                FROM publishers p
                JOIN books b ON p.publisher_id = b.publisher_id
                WHERE p.publisher_name LIKE '% % %'
                GROUP BY p.publisher_id, b.category
                HAVING COUNT(DISTINCT b.isbn) >= 3 AND AVG(b.rating) > 3
                ORDER BY p.publisher_id, b.category
                """)
        results=[]
        for (publisher_id, category) in cursor:
            results.append(QueryResult.ResultQ4(publisher_id,category))
        cursor.close()
        return results
    def functionQ5(self,author_id):
        cursor = self.connection.cursor()
        cursor.execute("""
                       SELECT DISTINCT a.author_id, a.author_name
                       FROM authors a
                       WHERE author_id = %s
                        ORDER BY a.author_id
                       """)
        cursor.close()

        # """
        # SELECT DISTINCT a.author_id, a.author_name
        # FROM authors a
        # JOIN author_of ao ON a.author_id = ao.author_id
        # JOIN books b ON ao.isbn = b.isbn
        # WHERE b.publisher_id IN (
        #     SELECT DISTINCT b2.publisher_id
        #     FROM books b2
        #     JOIN author_of ao2 ON b2.isbn = ao2.isbn
        #     WHERE ao2.author_id = %s
        # )
        # AND a.author_id != %s
        # ORDER BY a.author_id;
        # """
    def functionQ6(self):
        pass
    def functionQ7(self,rating):
        pass
    def functionQ8(self):
        pass
    def functionQ9(self,keyword):
        pass
    def function10(self):
        pass