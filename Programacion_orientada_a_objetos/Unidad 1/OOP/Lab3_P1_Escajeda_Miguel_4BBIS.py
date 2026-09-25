class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def show_post(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author.name}")
        print(f"Content: {self.content}")

user1 = User("Carlos", "carlos@email.com")

post1 = Post(
    "My first post",
    "I am learning Python!",
    user1
)

post1.show_post()
