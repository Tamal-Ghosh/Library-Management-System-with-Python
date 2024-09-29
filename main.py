import Add_Book
import View_all_book_list
import search_book
import remove_book
import lent_book
import return_book
import print_book
import update_book_list
import update_lent_book_list
import view_lented_book

try:
    books = []
    lent_book_list=[]
    update_book_list.update_book_list(books)
    update_lent_book_list.update_book_list(lent_book_list)

    print("\nWelcome to the library!\nThe option for you below:")
    while(True):
        print("1.Add book.\n2.View all books.\n3.Search book.\n4.Remove book.\n5.Lent book.\n6.Return book.\n7.View lented books.\n0.Exit\n\n")
        choice=int(input("Enter choice: "))
        if choice==1:
            Add_Book.add_book(books)
        elif choice==2:
            View_all_book_list.view_all_book(books)
        elif choice==3: 
            search_book.search_book(books)
        elif choice==4:
            remove_book.remove_book(books)
        elif choice==5:
            lent_book.lent_book(books,lent_book_list)
        elif choice==6:
            return_book.return_book(books,lent_book_list)
        elif choice==7:
            view_lented_book.view_lented_book(lent_book_list)
        elif choice==0:
            break
    

except ValueError:
    print("Please give the inputs in right formate.")
except FileNotFoundError:
    print("Your expected file is not found.")
except KeyError:
    print("Key is not found in the dictionary")
except PermissionError:
    print("Permission denied")
