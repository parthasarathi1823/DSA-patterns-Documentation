class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while(k and stack and int(stack[-1])>int(digit)):
                stack.pop()
                k-=1

            stack.append(digit)

        # if any digit is not removed, if it is already in order
        while(k):
            stack.pop()
            k-=1

        result = ''.join(stack).lstrip('0')

        return result if result else '0'            