import csv
def update_book_list(books):
    with open("Lent_book.csv",'r') as fp:
        book_reader=csv.DictReader(fp)
        for book in book_reader:
            books.append(book)