
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        #return [name for name in Author.all if Contract.author == Author.name]
        this_authors_contracts = []
        for cur_contract in Contract.all:
            if cur_contract.author == self:
                this_authors_contracts.append(cur_contract)
        return this_authors_contracts
    
    def books(self):
        this_authors_books = []
        for contract in Contract.all:
            if contract.author == self:
                this_authors_books.append(contract.book)
        return this_authors_books

    # To-Do
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    # To-Do
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total = total + contract.royalties
        return total

class Book:
    
    all = []

    def __init__(self, title):
        self.title = title

    def contracts(self):
        this_books_contracts = []
        for cur_contract in Contract.all:
            if cur_contract.book == self:
                this_books_contracts.append(cur_contract)
        return this_books_contracts

    def authors(self):
        this_books_authors = []
        for contract in Contract.all:
            if contract.book == self:
                this_books_authors.append(contract.author)
        return this_books_authors

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date,  str):
            raise Exception("Date must be a string")
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, (int, float)):
            raise Exception("Royalties must be a number")
        self._royalties = royalties

    # To-Do
    @classmethod
    def contracts_by_date(cls, date):
        '''for contract in cls.all: # assuming all_contracts() returns all contracts
            if contract.date == date:
                all = contract
        return all'''
        return [contract for contract in cls.all if contract.date == date]