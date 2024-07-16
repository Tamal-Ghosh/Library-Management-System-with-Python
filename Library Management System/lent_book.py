import search_book
import remove_book
import books_to_file
import csv
def lent_book(books,lent_books):
    flag=search_book.search_book(books)
    isNotLent=True
    if flag==False:
        name=input("Enter the name who lent the book: ")
        isbn=input("Enter the ISBN of the book: ")
        for index,book in enumerate(books):
            if isbn==str(book["ISBN"]) and int(book["Quantity"])>0:
                book["Quantity"]=int(book["Quantity"])-1
                print("Book lent successfully!")
                books_to_file.books_to_file(books)
                lbook={
                    'Name':name,
                    'Title':book['Title'],
                    'Author':book['Author'],
                    'ISBN':book['ISBN'],
                    'Publishing_Year':book['Publishing_Year'],
                    'Price':book['Price'],
                    'Quantity':1,
                    'Book_status':"Lented"
                    
                    }
                lent_books.append(lbook)
                with open("Lent_book.csv",'w',newline='') as fp:
                    fieldNames=['Name','Title','Author','ISBN','Publishing_Year','Price','Quantity','Book_status']
                    book_writer=csv.DictWriter(fp,fieldnames=fieldNames, delimiter=',')
                    book_writer.writeheader()
                    for lent_book in lent_books:
                        book_writer.writerow(lent_book)
                    
                isNotLent=False
                return books,lent_books
    
    if isNotLent:
        print("Not enough books available to lend!")
        return books,lent_books
                    
            
        