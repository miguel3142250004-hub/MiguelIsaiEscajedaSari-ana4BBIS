class User:
    def __init__(self, name, age, modality, is_active=True, is_verified=False):
        self.name = name
        self.age = age
        self.modality = modality
        self.is_active = is_active      
        self.is_verified = is_verified  

    def login(self):
        print(f"--- Login required for {self.name} ---")
        name = input("Name: ")
        modality = input("Modality: ")

        if name == self.name and modality == self.modality:
            print("You are logged!")
            return True
        else:
            print("Something went wrong...")
            return False


class Post:
    def __init__(self, sender, title, content, description):
        self.sender = sender  
        self.title = title
        self.content = content
        self.description = description

    def like(self):
        if self.sender.login():
            print(f"\nPost by {self.sender.name}:")
            print(f"{self.title} \n {self.content} \n {self.description}")
            like_input = input("Like this post? (Y/N): ").strip().upper()
            while like_input != "Y" and like_input != "N":
                like_input = input("Do you want to like this post? (Y/N): ").strip().upper()
            if like_input == "Y":
                print("OK")
            else:
                print("OK :( ")


class Comments:
    def __init__(self, sender, receiver, text, hashtags, like=False):
        self.sender = sender      
        self.receiver = receiver  
        self.text = text
        self.hashtags = hashtags
        self.like = like

    def comment(self):
        if self.sender.login():
            print(f"\nComment from {self.sender.name} to {self.receiver.name}:")
            print(f"Text: {self.text} with hashtags {self.hashtags}")


class Message:
    def __init__(self, sender, receiver, text, color, size):
        self.sender = sender      
        self.receiver = receiver  
        self.text = text
        self.color = color
        self.size = size

    def send_message(self):
        if self.sender.login():
            print(f"\nMessage sent from {self.sender.name} to {self.receiver.name}:")
            print(f"(Color: {self.color}, Size: {self.size}): {self.text}")



user1 = User("Juan", "18", "clasica")
user2 = User("Dulce", "19", "Bis")


chat = Message(sender=user1, receiver=user2, text="Hola, ¿cómo estás?", color="blue", size="12")
chat.send_message()