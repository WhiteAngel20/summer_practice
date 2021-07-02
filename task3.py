def get_len(text):
    return 0 if text[-1] == ' ' else len(text.split(' ')[-1])

print("Len of the last item: ", get_len(input("Enter some text: ")))




