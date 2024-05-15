nums = [4, 2, 19, 11, 20, 2, 6, 4, 10]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print('Duplicate:', nums[i])
