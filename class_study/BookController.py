from BookService import BookService
from BookEntity import Book


class BookController:

    @classmethod
    def addBookRequest(cls):
        book = Book(
            bookName="테스트 도서명",
            authorName="테스트 저자명",
            publisher="테스트 출판사명",
            isbn="테스트 isbn"
        )
        BookService.addBook(book)
