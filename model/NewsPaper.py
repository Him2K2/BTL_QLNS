import BookDocument
class Book(BookDocument):
    def __init__(self, id, publisher, inventory, quantitySale, price, publishDate):
        super().__init__(id, publisher, inventory, quantitySale, price)
        self.__publishDate = publishDate #ngày phát hành

    #getter & setter of release date
    def get_Publish_Date(self): return self.__releaseDate
    def set_Publish_Date(self, publishDate): self.__publishDate = publishDate
