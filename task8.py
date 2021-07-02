def missing_poss():
    nums = list(input("enter some nums: ").split(' '))
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])
    missing_index = nums.index(sorted(nums)[0])
    print(missing_index)


missing_poss()




