import print_book
import csv
def view_all_book(books):
  if len(books)==0:
    print("No book found!")
  else:
    for book in books:
      print_book.show(book)  
