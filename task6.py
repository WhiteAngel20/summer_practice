def receive_median():
    nums1 = list(input("enter some nums: ").split(' '))
    nums2 = list(input("enter some nums: ").split(' '))

    def convertlist_str_to_int(_list):
        for i in range(0, len(_list)):
            _list[i] = int(_list[i])
        return _list

    nums1 = convertlist_str_to_int(nums1)
    nums2 = convertlist_str_to_int(nums2)
    list_merge = sorted(nums1 + nums2)
    median = sum(list_merge) / len(list_merge)
    print("median: ", median)


receive_median()



