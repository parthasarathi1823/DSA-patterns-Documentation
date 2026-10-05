class Solution:
    def smallerNumbersThanCurrent(self, nums):
        freq = [0] * 101

        for num in nums:
            freq[num] += 1

        for i in range(1, 101):
            freq[i] += freq[i - 1]

        return [freq[num - 1] if num > 0 else 0 for num in nums]
