from books import book
from users import user
from library import library

book1 = book("001","OOP Fundamentals","Jhon L","BBC")
book2 = book("002","Python for dummies","Stef Maruzh","For dummies")
user1 = user("001","Escajeda Miguel","1234")
library = library ()
library.add_book(book1)
library.add_book(book2)
library.add_users(user1)
library.show_books()
#Requeriments
#1. The system must allow register books.
#2. The system must allow register users.
#3. The system must allow a book to be borrowed by a user.
#4. A book that has already been borrowed cannot be borrowed again.
#5. The system must allow a book to be returned.

# 1. IMPORT MODULES
from books import book
from users import user
from library import library

# 2. INITIALIZE LIBRARY
my_library = library()

# 3. CREATE BOOK INSTANCES
book1 = book("001", "OOP Fundamentals", "Jhon L", "BBC")
book2 = book("002", "Python for dummies", "Stef Maruzh", "For dummies")

# 4. CREATE USER INSTANCES
user1 = user("001", "Escajeda Miguel", "1234")

# 5. ADD BOOKS TO LIBRARY
my_library.add_book(book1)
my_library.add_book(book2)

# 6. ADD USERS TO LIBRARY
my_library.add_users(user1)

# 7. EXECUTE OUTPUTS (Show all data stored in the system)
my_library.show_books()
my_library.show_users()