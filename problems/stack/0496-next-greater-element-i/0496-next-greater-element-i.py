class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        st = []
        n = len(nums2)
        ans = [-1]*n

        for i in range(n-1,-1,-1):
            A = nums2[i]
            while st and st[-1] <= A:
                st.pop()
            if st:
                ans[i]=st[-1]

            st.append(A)

        d = dict(zip(nums2,ans))

        return [d[num] for num in nums1]

        