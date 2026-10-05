# There are Two approach's for prefix sum

# Approach 1: Using Formula

def build_prefixSum(arr):

    # length of the given array
    n = len(arr)

    # building prefix sum array with all Zeroes initially
    prefix = [0]*n

    # assigning first element to build sum
    prefix[0] = arr[0]

    # loop to traverse the array
    for i in range(1,n): # as we have already assigned first element, loop start from second element (index = 1)
        prefix[i] = prefix[i-1] + nums[i] # Formula
    

    # Prefix array
    return prefix

# -----------------------------------------------------------------------------------------------------------------

# Approach 2: In-place modification 

def build_prefixSum_inplace(arr):
    """
    Changing the given array to prefix by adding the sum of previous all elements to current position 

    Input : [1, 2, 3, 4, 5]
    Output: [1, 3, 6, 10, 15]

    Explaination: [1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5]

    """
    for i in range(1,len(arr)):
        
        # adding the sum of all previous elements to current element 
        arr[i] += arr[i-1]
    
    return arr 

"""
# Time Complexity
    
    For building prefix sum: O(n)
    For Range Queries: O(1) - simple substration

# Space Complexit
    
    For building prefix_sum: O(n) (for new array, O(1) if in-place modification)
    For Range Queries: Just Arithemetic
"""
