str = input("Введите номер карты: ")
def numCard(str):
    return "*" * (len(str) - 4) + str[-4:]


print(numCard(str))