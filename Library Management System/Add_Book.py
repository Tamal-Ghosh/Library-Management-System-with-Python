import csv
import books_to_file

def add_book(books):
    title = input("Enter the book name: ")
    author = input("Enter the author name: ")
    isbn = int(input("Enter a unique number: "))  # Treat ISBN as a string
    publishing_year = int(input("Enter the publishing year: "))
    price = float(input("Enter the book price: "))
    quantity = int(input("Enter the book's quantity: "))
    
    
    book = {
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Publishing_Year": publishing_year,
        "Price": price,
        "Quantity": quantity,
        "Book_status":"Added",
    }
    isNotChanged = True
    
    for pbook in books:
        if pbook['ISBN'] == str(book['ISBN']):
            pbook['Quantity'] = int(pbook['Quantity']) + quantity
            print("Book quantity updated successfully!")
            books_to_file.books_to_file(books)
            isNotChanged = False
            break
    
    if isNotChanged:
        books.append(book)
        books_to_file.books_to_file(books)
        print("Book added successfully!")
    
    return books
