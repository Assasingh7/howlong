def smallestDivisor(nums, threshold):

    low = 1
    high = max(nums)

    while low <= high:

        mid = (low + high) // 2

        if possible(mid, threshold, nums):
            # This divisor works.
            # Try a smaller one.
            high = mid - 1

        else:
            # Sum is too large.
            # Need a larger divisor.
            low = mid + 1

    return low
def possible(divisor, threshold, nums):

    total = 0

    for num in nums:
        total += (num + divisor - 1) // divisor

    return total <= threshold