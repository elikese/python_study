class Book:

    def __init__(self, bookId = 0, bookName = "", authorName = "", publisher = "", isbn = ""): # 필드값은 생성자로 정의함
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.publisherName = publisher
        self.isbn = isbn
    def setAuthor(self, author): # setter로 필드값을 정의함
        self.author = author

    def __str__(self) -> str:
        return f"""Book[
bookId: {self.bookId}, 
bookName: {self.bookName}
authorName: {self.authorName}
publisherName: {self.publisherName}]"""
        # return "Book[bookId: {0}, bookName: {1}]".format(self.bookId, self.bookName)
        # return "Book[bookId: {bookId}, bookName: {bookName}]".format(bookId = self.bookId, bookName = self.bookName)