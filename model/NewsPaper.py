from model.BookDocument import BookDocument

class Book(BookDocument):
    def __init__(self, id, publisher, inventory, quantitySale, price, releaseDate):
        super().__init__(id, publisher, inventory, quantitySale, price)
        self.__releaseDate = releaseDate #ngày phát hành

    #getter & setter of release date
    def get_Release_Date(self): return self.__releaseDate
    def set_Release_Date(self, value): self.__releaseDate = value
    def showNewPaper(self):
        super().display()
        print(f"Ngày phát hành: {self.__publishDate}")


