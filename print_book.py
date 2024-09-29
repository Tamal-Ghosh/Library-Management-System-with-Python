def show(book):
    print(
        book["Title"],
        book["Author"],
        book["ISBN"],
        book["Publishing_Year"],
        book["Price"],
        book["Quantity"],
        book['Book_status'],
        sep=" --- ",
    )
    return book
