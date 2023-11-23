class BookDocument():
    def __init__(self, id, publisher, quantity, soldPerDay, price):
        self.__id = id #mã tài liệu
        self.__publisher = publisher #tên nhà xuất bản
        self.__quantity = quantity # số lượng tồn kho
        self.__soldPerDay = soldPerDay #số lượng bán (theo ngày)
        self.__price = price #giá bán

    #getter & setter of id
    def get_Id(self): return self.__id
    def set_Id(self, id): self.__id = id

    # getter & setter of publisher
    def get_Publisher(self): return self.__publisher
    def set_Publisher(self, publisher): self.__publisher = publisher

    #getter & setter of quantity
    def get_Quantity(self): return self.__quantity
    def set_Quantity(self, quantity): self.__quantity = quantity

    # getter & setter of quantitySale
    def get_Sold_Per_Day(self): return self.__soldPerDay
    def set_Sold_Per_Day(self, soldPerDay): self.__soldPerDay= soldPerDay

    # getter & setter of price
    def get_Price(self): return self.__price
    def set_Price(self, price): self.__price = price