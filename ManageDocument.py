from model.Book import Book
from model.Magazine import Magazine
from model.NewsPaper import NewsPaper

listNewsPaper = []
listMagazine = []
listBook = []

def insertBook():
    idBook = input("Nhập mã sách: ")
    publisher = input("Nhập tên nhà xuất bản: ")
    quantity = int(input("Nhập số lượng tồn kho: "))
    soldPerDay = int(input("Nhập số lượng bán theo ngày: "))
    price = int(input("Nhập giá: "))
    author = input("Nhập tên tác giả: ")
    numPage = int(input("Nhập số trang: "))

    book = Book(idBook, publisher, quantity, soldPerDay, price, author, numPage)
    listBook.append(book)

def insertMagazine():
    idMagazine = input("Nhập mã tạp chí: ")
    publisher = input("Nhập tên nhà xuất bản: ")
    quantity = int(input("Nhập số lượng tồn kho: "))
    soldPerDay = int(input("Nhập số lượng bán theo ngày: "))
    price = int(input("Nhập giá: "))
    issueNumber = int(input("Nhập số phát hành: "))
    publishMonth = input("Nhập tháng phát hành: ")

    magazine = Magazine(idMagazine, publisher, quantity, soldPerDay, price, issueNumber, publishMonth)
    listMagazine.append(magazine)

def insertNewsPaper():
    idNewsPaper = input("Nhập mã báo: ")
    publisher = input("Nhập tên nhà xuất bản: ")
    inventory = int(input("Nhập số lượng tồn kho: "))
    quantitySale = int(input("Nhập số lượng bán theo ngày: "))
    price = int(input("Nhập giá: "))
    publishDate = input("Nhập ngày phát hành: ")

    newspaper = NewsPaper(idNewsPaper, publisher, inventory, quantitySale, price, publishDate)
    listNewsPaper.append(newspaper)

def displayBook():
    for book in listBook:
        book.show_Book()

def displayMagazine():
    for magazine in listMagazine:
        magazine.showMagazine()

def displayNewsPaper():
    for newspaper in listNewsPaper:
        newspaper.showNewPaper()

def quantityBook():
    return len(listBook)

def quantityMagazine():
    return len(listMagazine)

def quantityNewsPaper():
    return len(listNewsPaper)
