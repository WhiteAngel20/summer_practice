def ispalindrom(text = input("enter some text: ")):
    return True if text == text[::-1] else False #[::-1] revers

print("Palindrom!") if ispalindrom() == True else print("Isn't palindrom")
