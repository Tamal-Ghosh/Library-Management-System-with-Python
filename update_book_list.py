import csv
def update_book_list(books):
    with open("Library.csv",'r') as fp:
        book_reader=csv.DictReader(fp)
        # next(book_reader)
        for book in book_reader:
            books.append(book)