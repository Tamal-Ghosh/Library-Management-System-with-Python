import print_book
def search_book(books):
    search_item = input("Enter the title or ISBN number or author name: ")
    isNotFound=True
    for book in books:
        if search_item.lower() in  book["Author"].lower():
            print_book.show(book)
            isNotFound=False
        elif search_item.lower() in  book["Title"].lower():
             print_book.show(book)
             isNotFound=False
    if isNotFound:
        for book in books:
            if search_item == str(book["ISBN"]):
                print_book.show(book)
                isNotFound=False
    
    if isNotFound:
        print("Book not found!")
        
    return isNotFound
        
        
