def sortNumbers(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


numbers = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
print(sortNumbers(numbers))
