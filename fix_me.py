import numbers


def calculate_average(nums):
    total = sum(nums)
    count = len(numbers)
    return total / count

nums = [10, 15, 20]
print("The average is:", calculate_average(nums))
