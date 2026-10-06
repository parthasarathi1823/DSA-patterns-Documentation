class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        present = set(nums)
        ans = []

        for i in range(1,len(nums)+1):
            if i not in present:   
                ans.append(i)


        return ans        