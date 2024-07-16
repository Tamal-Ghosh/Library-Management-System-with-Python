import books_to_file
import csv
def return_book(books,lent_books):
    isbn=input("Enter the ISBN of the book: ")
    for book in books:
        if isbn==str(book["ISBN"]):
            book["Quantity"]=int(book["Quantity"])+1
            name=input("The name who lented book: ")
            for index,lent_book in enumerate(lent_books):
                if str(isbn)==book['ISBN']:
                    lent_books.pop(index)
                    books_to_file.books_to_file(books)
                    
                    with open("Lent_book.csv",'w',newline='') as fp:
                        fieldNames=['Name','Title','Author','ISBN','Publishing_Year','Price','Quantity','Book_status']
                        book_writer=csv.DictWriter(fp,fieldnames=fieldNames, delimiter=',')
                        book_writer.writeheader()
                        for lent_book in lent_books:
                            book_writer.writerow(lent_book)
                        print("Book returned successfully!")
                        return
    return books