
class Library:
    '''
    This class represents a library that offers book for customers to borrow.
    '''

    def __init__(self, books):
        '''
        INPUT:
            - books: an iterable of str
        Initialize our new library with a list of books
        that this library owns.
        '''
        self.books = {book: None for book in books}

    def all_books(self):
        '''
        Return a list of all the books that this library owns.
        '''
        return sorted(self.books)

    def add_book(self, book):
        '''
        INPUT:
            - book: str
        Add this book to the list of books this library ownsself.
        '''
        if book not in self.books:
            self.books[book] = None

    def book_holder(self, book):
        '''
        INPUT:
            - book: str
        Return the name of the customer who has this book. If no customer
        has this book, return None
        '''
        if book in self.books:
            return self.books[book]
        return None

    def checkout(self, book, customer):
        '''
        INPUT:
            - book: str
            - customer: str
        If the given book isn't currently checked out, then check it
        out to the given customer and return True.
        If the given book is currently checked out, do nothing and
        return False.
        '''
        if book in self.books and not self.books[book]:
            self.books[book] = customer
            return True
        return False

    def checkin(self, book):
        '''
        INPUT:
            - book: str
        Check this book back in.
        '''
        if book in self.books:
            self.books[book] = None
