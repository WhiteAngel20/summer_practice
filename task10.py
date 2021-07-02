def get_target_value():
    some_list = [1, 4, 7, 5, 8, 9, 6, 3, 2, 1, 4]
    some_list = sorted(some_list)
    target_value = int(input("Input target: "))
    print(some_list.index(target_value)) if target_value in some_list else print(None)


get_target_value()