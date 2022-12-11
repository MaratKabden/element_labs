from typing import List, Optional
from Models.User import User
from Models.BankAccount import BankAccount
from Models.Account import Account


class Repositories:
    users: List[User] = []

    def create_user(self, name, surname, password):
        user = User(name, surname, password)
        self.users.append(user)

    def get_user(self, username: str, password: str) -> Optional[User]:
        user = next(
            (u for u in self.users if username ==
             u.name and u.check_password(password)),
            None
        )

        if not user:
            print('User not found')
            return

        return user

    def create_user_acc(self, user: User, cur: Account):
        user.create_account(cur)

    def get_user_acc(self, user: User, cur: Account) -> Optional[BankAccount]:
        return user.get_account(cur=cur)