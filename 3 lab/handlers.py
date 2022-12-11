from typing import Optional

from Models.BankAccount import BankAccount
from Models.User import User
from Models.Account import Account
from servises import Servises


class Handler:
    serv: Servises

    def __init__(self, serv) -> None:
        self.serv = serv

    def sign_up(self, name: str, surname: str, passrword: str) -> Optional[User]:
        name.strip().lower()
        surname.strip().lower()
        passrword.strip()
        self.serv.create_user(name, surname, password=passrword)
        return self.serv.find_user(name, password=passrword)

    def sign_in(self, name: str, password: str) -> Optional[User]:
        name.strip().lower()
        password.strip()
        return self.serv.find_user(name=name, password=password)

    def create_acc(self, user: User, acc: Account):
        self.serv.create_user_acc(user=user, cur=acc)

    def choose_acc(self, user: User, cur: Account) -> Optional[BankAccount]:
        return self.serv.get_user_acc(user=user, cur=cur)

    def add_amount(self, acc: BankAccount, amount) -> float:
        self.serv.addToBankAccount(acc=acc, amount=amount)
        return self.serv.get_ramainder(acc)

    def sub_amount(self, acc: BankAccount, amount) -> float:
        self.serv.substractFromBankAccount(acc=acc, amount=amount)
        return self.serv.get_ramainder(acc)

    def transfer(self, fr: BankAccount, to: BankAccount, amount) -> float:
        if fr.get_account() != Account.KZT or to.get_account() != Account.KZT:
            fr.substract(amount)
            amount *= fr.get_account().value
        self.serv.tranfer(fr, to, amount)
        return self.serv.get_ramainder(fr)