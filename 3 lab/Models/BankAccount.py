from Models.Account import Account


class BankAccount:

    account: Account
    _amount: float

    def __init__(self, acc):
        self.account = acc
        self._amount = 0

    def add(self, amount):
        self._amount += amount

    def substract(self, amount):
        if amount > self._amount:
            print("Недостаточно средств")
        else:
            self._amount -= amount

    def get_remainder(self) -> float:
        return self._amount

    def get_account(self) -> Account:
        return self.account

    def __repr__(self) -> str:
        return f"Счет {self.account}, Oстаток {self._amount}"