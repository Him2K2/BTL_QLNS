class BookDocument():
    def __init__(self, id, publisher, inventory, quantitySale, price):
        self.__id = id #mã tài liệu
        self.__publisher = publisher #tên nhà xuất bản
        self.__inventory = inventory # số lượng tồn kho
        self.__quantitySale = quantitySale #số lượng bán (theo ngày)
        self.__price = price #giá bán

    #getter & setter of id
    def get_Id(self): return self.__id
    def set_Id(self, value): self.__id = value

    # getter & setter of publisher
    def get_Publisher(self): return self.__id
    def set_Publisher(self, value): self.__publisher = value

    #getter & setter of inventory
    def get_Inventory(self): return self.__inventory
    def set_Inventory(self, value): self.__inventory = value

    # getter & setter of quantitySale
    def get_QuantitySale(self): return self.__quantitySale
    def set_QuantitySale(self, value): self.__quantitySale = value

    # getter & setter of price
    def get_Price(self): return self.__price
    def set_Price(self, value): self.__price = value