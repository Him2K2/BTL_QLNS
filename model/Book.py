from model.BookDocument import BookDocument
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
    def show_Book(self):
        print("-" * 30)
        print(f"Mã sách: {self.get_Id()}")
        print(f"Nhà xuất bản: {self.get_Publisher()}")
        print(f"Số lượng tồn kho: {self.get_Quantity()}")
        print(f"Số lượng bán theo ngày: {self.get_Sold_Per_Day()}")
        print(f"Giá tiền: {self.get_Price()}")
        print(f"Tác giả: {self.get_Author()}")
        print(f"Số trang: {self.get_Num_Page()}")
        print("-" * 30)
