import BookDocument
class Book(BookDocument):
    def __init__(self, id, publisher, quantity, soldPerDay, price, issueNumber, publishMonth):
        super().__init__(id, publisher, quantity, soldPerDay, price)
        self.__issueNumber = issueNumber #số phát hành
        self.__publishMonth = publishMonth #tháng phát hành

    #getter & setter of author
    def get_Issue_Number(self): return self.__issueNumber
    def set_Issue_Number(self, issueNumber): self.__issueNumber = issueNumber

    #getter & setter of pages
    def get_Publish_Month(self): return self.__publishMonth
    def set_Publish_Month(self, publishMonth): self.__publishMonth = publishMonth