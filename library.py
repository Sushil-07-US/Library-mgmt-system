#Code for library to store books, to borrow books by checking the numbers of books in the library.

def main():

    books ={}
    def store_book():

        while True:
            book_name = input('\n\nEnter the name of books and type "done" after book added:  ').capitalize().strip()
            if book_name == "Done":
                break
            
            try:
                quantity = int(input(f"Enter the quantity for {book_name}: "))
                if quantity < 1:
                    print("Number must be greater than zero'.")
                    
                    books[book_name] = quantity
                    continue
                
                

            except ValueError:
                print("Invalid input! Please enter valid number.")



    def show_books():
        print("Books available at this movement in US library.")

        for index, book in enumerate(books, start =1):
            print(f"{index}. Book name:{book}       Quantity:{books[book]}")
            

 

    def borrow_books():
      
        show_books()
        
        name_of_book = input("Enter the name of book: ").capitalize().strip()

        if books[name_of_book] > 0:
            print("Here is your book, Thank you for choosing us.")
            books[name_of_book] -= 1

            if books[name_of_book] == 0:
                del books[name_of_book]

            else:
                print(f"{name_of_book} is out of stock.")
                

        else:
            print("This book is not available at a movement.")
                
    

    def exit():
        print("Thanks for your great time with us.")
                
    
    print("Welcome to US library.\n\nPlease choose one of the following options.\n1. store books\n2. book list\n3. borrow book\n4. exit ")

    
    while True:

        option = input("Which number you want to choose: ")
            
        if option == "1":
            store_book()

        elif option == "2":
            show_books()

        elif option == "3":
            borrow_books()

        elif option == "4":

            exit()
            break

        else:
            print("Please choose option between 1 to 4: ")
            continue

 
main()




