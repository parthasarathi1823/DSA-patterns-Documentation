class Solution:
    def solve(self, nums):
        stack = []

        for i in range(len(nums)):

            # Modify this condition depending on the problem
            while stack and CONDITION:
                # Process popped element
                stack.pop()

            stack.append(i)   # or nums[i], depending on the problem

        # Optional: Process remaining elements
        while stack:
            stack.pop()

'''
----------------
Increasing Stack
----------------
while stack and Top > Current:
    pop()

Decreasing Stack
----------------
while stack and Top < Current:
    pop()

Previous Problems
-----------------
Answer before push()

Next Problems
-------------
Answer while popping()

Store Indices
-------------
Preferred in most problems

Store Values
------------
Only when indices are unnecessary
----------------
'''
