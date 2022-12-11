from typing import Optional
from repositories import Repositories
from Models.User import User
from Models.Account import Account
from Models.BankAccount import BankAccount


class Servises:

    rep: Repositories

    def __init__(self, repositories: Repositories):
        self.rep = repositories

    def create_user(self, name: str, surname: str, password: str):
        self.rep.create_user(name=name, surname=surname, password=password)

    def find_user(self, name, password) -> Optional[User]:
        return self.rep.get_user(username=name, password=password)

    def create_user_acc(self, user: User, cur: Account):
        self.rep.create_user_acc(user=user, cur=cur)

    def get_user_acc(self, user: User, cur: Account) -> Optional[BankAccount]:
        return self.rep.get_user_acc(user=user, cur=cur)

    def addToBankAccount(self, acc: BankAccount, amount):
        acc.add(amount)

    def substractFromBankAccount(self, acc: BankAccount, amount):
        acc.substract(amount)

    def get_ramainder(self, acc: BankAccount) -> float:
        return acc.get_remainder()

    def get_currency(self, acc: BankAccount) -> Account:
        return acc.get_account()

    def tranfer(self, fr: BankAccount, to: BankAccount, amount):
        if fr.get_account() == to.get_account():
            self.substractFromBankAccount(fr, amount)
            self.addToBankAccount(to, amount)
        else:
            if fr.get_account() == Account.KZT:
                self.substractFromBankAccount(fr, amount)
                amount /= to.get_account().value
                self.addToBankAccount(to, amount)
            elif to.get_account == Account.KZT:
                self.substractFromBankAccount(fr, amount)
                amount *= fr.get_account().value
                self.addToBankAccount(to, amount)
            else:
                amount /= to.get_account().value
                self.addToBankAccount(to, amount)