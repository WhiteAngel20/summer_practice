def basenums():
    nums = input("enter some nums(1 3 8 4): ").split(' ')
    target = int(input("target sum is "))

    # perform conversion from str to int
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])

    for i in nums:
        for j in nums:
             if i + j == target:
                 index1, index2 = nums.index(i), nums.index(j)
                 return [index1, index2, target]


ends = basenums()
print(None) if ends == None else print(f"output: nums[{ends[0]}] + nums[{ends[1]}] = {ends[2]}, we return [{ends[0], ends[1]}]")



