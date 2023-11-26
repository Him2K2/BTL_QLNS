import ManageDocument


while True:
    print('''
    1. Thêm sách
    2. Thêm Tạp chí
    3. Thêm Báo
    4. Hiển thị danh sách Sách
    5. Thoát
    ''')
    choice = int(input("Nhập lựa chọn: "))
    if choice == 1:
        ManageDocument.insertBook()
    elif choice == 2:
        ManageDocument.insertMagazine()
    elif choice == 3:
        ManageDocument.insertNewsPaper()
    elif choice == 4:
        print("Số lượng sách hiện có: {}".format(ManageDocument.quantityBook()))
        ManageDocument.displayBook()
