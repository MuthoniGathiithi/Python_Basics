def check_palidrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(check_palidrome("madam"))
print(check_palidrome("jupiter"))