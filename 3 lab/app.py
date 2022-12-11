from repositories import Repositories
from Models.User import User
from Models.Account import Account
from Models.BankAccount import BankAccount
from servises import Servises
from handlers import Handler


def signup_in(handler: Handler) -> User:
    while True:
        print("Наберите 1 чтобы зарегистрироваться, \n"
              "Наберите 2, чтобы войти")
        try:
            cmd = int(input())
            match cmd:
                case 1:
                    name = input("Введите имя: ")
                    surname = input("Введите фамилию: ")
                    while True:
                        pwd = input("Введите пароль: ")
                        pwd1 = input("Повторите пароль: ")
                        if pwd != pwd1:
                            print("Пароли не совпадают")
                        break
                    handler.sign_up(name=name, surname=surname, passrword=pwd)
                    return handler.sign_in(name, password=pwd)
                case 2:
                    name = input("Введите имя ")
                    pwd = input("Введите пароль ")
                    return handler.sign_in(name, password=pwd)
                case _:
                    print("incorrect input")
        except:
            print("Incorrect input")


def init():
    repo = Repositories()
    serv = Servises(repositories=repo)
    handler = Handler(serv)
    user_acc: BankAccount
    user = signup_in(handler)
    print(f"Hello, {user.name}! How can I help you?")
    while True:
        try:
            cmd = int(input("Введите 1 чтобы выбрать счет, \n"
                            "Введите 2 чтобы создать счет\n"
                            "Введите 0 чтобы выйти "))
            if cmd == 1:
                user.list_accounts()
                acc = int(input("Введите номер счета "))
                if (acc < 0 or acc > len(user.user_accounts)):
                    raise ValueError
                user_acc = user.user_accounts[acc]
                oper = int(input("Введите 1 чтобы внести деньги\n"
                                 "Введите 2 чтобы снять \n"
                                 "Введите 3 чтобы перевести между своими счетами "))
                match oper:
                    case 1:
                        amount = int(input("Введите сумму: "))
                        print(
                            f"Ваш остаток {handler.add_amount(acc=user_acc, amount=amount)}")
                    case 2:
                        amount = int(input("Введите сумму: "))
                        print(
                            f"Ваш остаток {handler.sub_amount(acc=user_acc, amount=amount)}")
                    case 3:
                        if len(user.user_accounts) < 2:
                            print("Откройте еще один счет для этой операции ")
                        else:
                            user.list_accounts(ex=user_acc)
                            to_id = int(input("Куда вам перевести? "))
                            if (to_id < 0 or to_id > len(user.user_accounts)):
                                raise ValueError
                            to_acc = user.user_accounts[to_id]
                            amount = int(input("Введите сумму: "))
                            print(
                                f"Ваш остаток {handler.transfer(fr=user_acc, to=to_acc, amount=amount)}")
                    case _:
                        raise ValueError
            if cmd == 2:
                cur_id = int(input("Введите 1 чтобы открыть счет в тенге \n"
                                   "Введите 2 чтобы открыть счет в рублях \n"
                                   "Введите 3 чтобы открыть счет в долларах \n"
                                   "Введите 4 чтобы открыть счет в евро "))
                match cur_id:
                    case 1:
                        cur = Account.KZT
                    case 2:
                        cur = Account.RUB
                    case 3:
                        cur = Account.USD
                    case 4:
                        cur = Account.EUR
                    case _:
                        raise ValueError
                handler.create_acc(user=user, acc=cur)
            if cmd == 0:
                print("Hasta la vista ")
                exit(0)
            elif cmd not in range(1, 3):
                raise ValueError
            cmd = int(
                input("Оперция прошла успешно, хотите продолжить? 1 - да, 2 - нет "))
            if cmd != 1:
                print("Hasta la vista ")
                exit(0)
        except ValueError:
            print("Incorrect Input!")
        except EOFError:
            print("Hasta la vista")
            exit(0)


if __name__ == '__main__':
    init()