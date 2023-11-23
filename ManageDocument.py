import model.BookDocument
import model.Book
import model.Magazine
import model.NewsPaper

def insertBook(self, id, publisher, quantity, soldPerDay, price, author, numPage):
    self.__id = id
    self.__publisher = publisher
    self.__quantity = quantity
    self.__soldPerDay = soldPerDay
    self.__price = price
    self.__author = author
    self.__numPage = numPage

