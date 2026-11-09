#Cis 3120 Exam 1 Book
class Book:
    def __init__(self, title, author, price, page_count):
        self.title = title
        self.author = author
        self.price = price
        self.page_count = page_count

#Get the book's description
    def get_description(self):
        return f"{self.title} by {self.author}"
    

#Check if the book's price is expensive
    def is_expensive(self):
        if self.price > 50:
            return True
        else:
            return False


#Check if the book has more than 300 pages
    def is_long_book(self):
        if self.page_count > 300:
            return True
        else:
            return False

#defind the main function
def main():
    books = []
#enter the details of three books from the user
    for i in range(3):
        print(f"\nEnter details for book {i + 1}:")
        title = input("Enter the title of book: ")
        author = input("Enter the author of book: ")
        price = float(input("Enter the price of book: "))
        page_count = int(input("Enter the page count of book: "))

        book = Book(title, author, price, page_count)
        books.append(book)


# Display the information of each book
    for book in books:
        print("\nBook description:", book.get_description())
        print("Is expensive?", book.is_expensive())
        print("Is long book?", book.is_long_book())

main()