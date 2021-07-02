def iteration_by_list():
    some_list = [1, 4, 7, 5, 8, 9, 6, 3, 2, 1, 4]
    iters = iter(some_list)
    while True:
        try:
            print(next(iters), end=' ')
        except StopIteration as stop:
            break


iteration_by_list()





