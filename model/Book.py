import BookDocument
class Book(BookDocument):
    def __init__(self, id, publisher, inventory, quantitySale, price, author, pages):
        super().__init__(id, publisher, inventory, quantitySale, price)
        self.__author = author
        self.__pages = pages

    #getter & setter of author
    def get_Author(self): return self.__author
    def set_Author(self, value): self.__author = value

    #getter & setter of pages
    def get_Page(self): return self.__pages
    def set_Page(self, value): self.__pages = value