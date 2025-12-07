from user import User


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        if not self.privileges:
            print("Привілеї відсутні")
        else:
            print("Привілеї адміністратора:")
            for p in self.privileges:
                print("-", p)


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter):
        super().__init__(first_name, last_name, email, nickname, newsletter)
        self.priv = Privileges(
            [
                "Дозволено додавати повідомлення",
                "Дозволено видаляти користувачів",
                "Дозволено блокувати користувачів",
                "Дозволено редагувати публікації",
            ]
        )
