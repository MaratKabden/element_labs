from typing import List, Optional
from hashlib import sha256

from Models.Account import Account
from Models.BankAccount import BankAccount

class User:
    name: str
    surname: str
    _password: str
    user_accounts: List[BankAccount] = []

    def __init__(self, name: str, surname: str, password: str):
        self.name = name
        self.surname = surname
        self._password = self._hash_pwd(password)

    def check_password(self, password: str) -> bool:
        return self._password == self._hash_pwd(password)

    def create_account(self, cur: Account):
        acc = BankAccount(cur)
        self.user_accounts.append(acc)

    def list_accounts(self):
        for i in range(len(self.user_accounts)):
            print(f"{i}: {self.user_accounts[i]}")

    def get_account(self, cur: Account) -> Optional[BankAccount]:
        acc = next(
            (a for a in self.user_accounts if a.account == cur), None
        )
        if not acc:
            print('Account is not found')
            return

        return acc

    def __repr__(self) -> str:
        return f"Имя: {self.name}, Фамилия {self.surname}"

    @staticmethod
    def _hash_pwd(password: str):
        return sha256(password.encode(encoding='utf-8')).hexdigest()