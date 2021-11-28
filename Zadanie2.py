word = input("Введите слово:")
def reverse(word):
    return word[::-1]

def Palindrome(word):
    reverseWord = reverse(word)
    if word == reverseWord:
        print("Слово является палиндромом\n",
              word, " = ", reverseWord)
    else:
        print("Слово не являеться палиндромом\n",
              word, " != ", reverseWord)


print(Palindrome(word))