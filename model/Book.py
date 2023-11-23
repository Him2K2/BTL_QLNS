import BookDocument
class Book(BookDocument):
    def __init__(self, id, publisher, quantity, soldPerDay, price, author, numPage):
        super().__init__(id, publisher, quantity, soldPerDay, price)
        self.__author = author #tên tác giả
        self.__numPage = numPage #số trang

    #getter & setter of author
    def get_Author(self): return self.__author
    def set_Author(self, author): self.__author = author

    #getter & setter of pages
    def get_Num_Page(self): return self.__numPage
    def set_Num_Page(self, numPage): self.__numPage = numPage