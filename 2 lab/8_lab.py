# 8 Реализуйте следующие функции для банковского счета

def addToBankAccount(bank_account, a):
    bank_account += a
    return bank_account

def substractFromAccount(bank_account, a):
    bank_account -= a
    return bank_account

def moneyConversion(money, ex_form, ex_to):
    match ex_form, ex_to:
        case 'USD', 'KZT':
            return money * 470
        case 'KZT', 'USD':
            return money / 470        
        case 'EUR', 'KZT':
            return money * 480
        case 'KZT', 'EUR':
            return money / 480 

money = float(input())

print(moneyConversion('Денег на счету:', money, 'USD', 'KZT'))
print(moneyConversion('Денег на счету:', money, 'EUR', 'KZT'))
print(moneyConversion('Денег на счету:', money, 'KZT', 'USD'))
print(moneyConversion('Денег на счету:', money, 'KZT', 'EUR'))