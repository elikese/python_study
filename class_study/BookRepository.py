import pymysql

class BookRepository:

    host = "mysql-db.c9o4cegsgfvy.ap-northeast-2.rds.amazonaws.com"
    port = 3306
    user = "aws"
    password = "thldtkd12!"
    database = "library_db"

    @classmethod
    def saveBook(cls, book=None):
        connection = pymysql.connect(
            host=cls.host,
            port=cls.port,
            user=cls.user,
            password=cls.password,
            database=cls.database
        )
        cursor = connection.cursor()
        sql = 'insert into book_tb values (0, %s, %s, %s, %s, 1, 1, 0, now(), now())'
        cursor.execute(sql, (book.bookName, book.authorName, book.publisherName, book.isbn))
        connection.commit()
        return book