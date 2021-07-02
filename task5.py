def cleardublicates():
    user_digits = input("Enter some nums: ").split(' ')
    for i in range(0, len(user_digits)):
        user_digits[i] = int(user_digits[i])
    import collections
    dublicates = [item for item, count in collections.Counter(user_digits).items() if count > 1]
    outdigits = []
    for i in user_digits:
        if i not in dublicates:
            outdigits.append(i)
    print(f"Output: {outdigits}")


cleardublicates()










