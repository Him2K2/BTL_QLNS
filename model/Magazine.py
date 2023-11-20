import BookDocument
class Book(BookDocument):
    def __init__(self, id, publisher, inventory, quantitySale, price, issueNumber, releaseMonth):
        super().__init__(id, publisher, inventory, quantitySale, price)
        self.__issueNumber = issueNumber #số phát hành
        self.__releaseMonth = releaseMonth #tháng phát hành

    #getter & setter of author
    def get_Issue_Number(self): return self.__issueNumber
    def set_Issue_Number(self, value): self.__issueNumber = value

    #getter & setter of pages
    def get_Release_Month(self): return self.__releaseMonth
    def set_Release_Month(self, value): self.__releaseMonth = value