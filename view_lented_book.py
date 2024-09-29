import csv
def view_lented_book(lent_book_list):
    if len(lent_book_list)==0:
        print("No book lented!")
    else:
        for book in lent_book_list:
            print(
            book['Name'],
            book['Name'],
            book["Title"],
            book["Author"],
            book["ISBN"],
            book["Publishing_Year"],
            book["Price"],
            book['Book_status'],
            sep=" --- ",
        )
