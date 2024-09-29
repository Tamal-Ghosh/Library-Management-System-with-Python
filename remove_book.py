import search_book
import print_book
import csv
import books_to_file
def remove_book(books):
    flag=search_book.search_book(books)
    if flag==False:
        isbn=input("Enter the ISBN of the book: ")
        for index,book in enumerate(books): 
            if isbn==str(book["ISBN"]):
                books.pop(index)
                print("Removed successfully!")
                books_to_file.books_to_file(books)
               
                # return books
                    
                    
                    
                
                
                

        
        