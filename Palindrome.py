def single_check_palindrom(single_word):
    print((single_word))
    re_single_word=single_word[::-1]
    if re_single_word==single_word:
        print("True")
        return True
    else:
        print("False")
        return False
single_check_palindrom("kajak")

"""

Zgodne z poleceniem
funkcja sprawdza czy wprowadzony argument to plaindrom,
można wprowadzić jeden argument,
każdy argument zostanie wypisany, a w kolejnej linijce zostanie określony czy jest palindromem
funkcja zwraca wrtość boolen True/False

"""

def check_palindrome(*args):
    for word in args:
        print(word)
        re_word= word[::-1]
        if re_word == word:
            print("True")
        else:
            print("False")

check_palindrome("kajak","niepalindrom")
"""

funkcja sprawdza czy wprowadzony argument to plaindrom,
można wprowadzić dowolną ilość argumentów,
każdy argument zostanie wypisany, a w kolejnej linijce zostanie określony czy jest palindromem

"""
