def longestCommonPrefix(a):
    size = len(a)

    a.sort()

    # find the minimum length from
    # first and last string
    end = min(len(a[0]), len(a[size - 1]))

    i = 0
    while (i < end and a[0][i] == a[size - 1][i]):
        i += 1

    pre = a[0][0: i]
    return pre

if __name__ == "__main__":
    text = input("Enter some text: ").split(' ')
    print("The longest Common Prefix is :",
          longestCommonPrefix(text))



