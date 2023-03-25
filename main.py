def splitArraySameAverage(nums: list[int]) -> bool:
    n = len(nums)  # the length of the input
    _sum = sum(nums)  # the sum of all the integers in the input list.

    dp = [0] * (_sum + 1)  # This creates a list called dp (short for dynamic programming) and initializes it to all zeros,
                           # with length equal to _sum plus 1. The first element of dp is set to 1, as a base case.
    dp[0] = 1

    for num in nums:  # The main loop updates the dp array in reverse order for each number in nums. If it is possible to make
                      # the sum s - num using a subset of nums, dp[s] is updated with a bitwise OR of its current value and
                      # dp[s - num] shifted one bit to the left. The shift avoids overwriting previous values of dp[s].
        for s in range(_sum, num-1, -1):
            if dp[s - num]:
                dp[s] |= (dp[s - num] << 1)

    for length in range(1, n):  # The loop checks all possible subarray lengths to see if any subarray has an average equal to
                                # the overall average of the array. It does this by checking if the sum required to get that
                                # average is a multiple of the array length and if there exists a subset of the array
                                # that can be summed to that value using the dynamic programming list. If such a subset exists,
                                # and its length is valid, then the function returns True.
        if (_sum * length) % n == 0:
            s = (_sum * length) // n
            if dp[s] and (dp[s] & (1 << length)):
                return True

    return False


assert(splitArraySameAverage([2, 4, 5, 7, 10, 14]) == True)  # some tests just to be sure
assert(splitArraySameAverage([1, 3, 4]) == False)
assert(splitArraySameAverage([1, 3, 5]) == True)
assert(splitArraySameAverage([1, 3, 4, 5]) == False)
assert(splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]) == True)
assert(splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True)
assert splitArraySameAverage([1]) == False
assert splitArraySameAverage([1, 2]) == False
assert splitArraySameAverage([1, 2, 3]) == True
assert splitArraySameAverage([1, 2, 3, 4]) == True
assert splitArraySameAverage([3, 1, 2, 5, 4]) == True
assert splitArraySameAverage([10, 20, 30, 40, 50, 60]) == True
assert splitArraySameAverage([5, 7, 2, 4, 9, 10, 6]) == False
assert splitArraySameAverage([8, 3, 1, 7, 2, 6, 5, 4]) == True
assert splitArraySameAverage([2, 3, 5, 8, 7, 4, 6, 10, 9, 1]) == True

print("If it prints this it means that it works")
