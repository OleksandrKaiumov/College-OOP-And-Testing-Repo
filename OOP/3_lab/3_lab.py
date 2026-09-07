class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        if any(ch.isdigit() for ch in name):
            ValueError("Ім'я може містити лише літери!")
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        self.name = self.name.capitalize()
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Instance method
        """
        return f"{self.name}@{domain}"
    
    def get_name_letters_count(self) -> int:
        return len(self.name)

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"
    
    def save_to_file(self, filename="users.txt"):
        with open(filename, "a") as f:
            f.write(self.full_name + "\n")


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None, "oleksandr")
all_names = {name: MyName(name) for name in names if name is not None}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
Amount of letters in name: {me.get_name_letters_count()}
Full name: {me.full_name}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")