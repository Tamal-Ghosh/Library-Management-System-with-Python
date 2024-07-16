import csv
def books_to_file(books):
    with open("Library.csv",'w',newline='') as fp:
        fieldNames=['Title','Author','ISBN','Publishing_Year','Price','Quantity','Book_status']
        book_writer=csv.DictWriter(fp,fieldnames=fieldNames,delimiter=',')
        book_writer.writeheader()
        for book in books:
            book_writer.writerow(book)