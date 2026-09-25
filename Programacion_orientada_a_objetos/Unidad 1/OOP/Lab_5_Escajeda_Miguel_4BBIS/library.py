class library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_users(self, user):
        self.users.append(user)
    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())
            
# 1. ADD USER TO SYSTEM
    def add_users(self, user):
        self.users.append(user)
        
    # 2. ADD BOOK TO SYSTEM
    def add_book(self, book):
        self.books.append(book)

    # 3. SHOW ALL BOOKS
    def show_books(self):
        print("\n--- BOOKS IN LIBRARY ---")
        for book in self.books:
            print(book.show_book_info())
            
    # 4. SHOW ALL USERS (This functionality was missing)
    def show_users(self):
        print("\n--- REGISTERED USERS ---")
        for user in self.users:
            print(user.show_user_info())