# Core Template

# Pattern: Nested Loops (Most Common)



def single_pass_traversal_template(nums):
    """
    Finding Maximum Value in the Array

    Firstly, store first element in array as maximum for reference

    Then: (Here Traversal begins)

    - Iterarte Through Array  
    - Compare Every element with maximum
    - If the given element is greater than Maximum, Update Current value as Maximum
    - Finally display the maximum element
    """
    # if array is empty , no maximum element
    if not nums:
        return None


    # Assigning First element as Maximum 
    max_element=nums[0]
    
    # single loop to traverse the array one time
    for num in nums:
        # condition to check the maximum element
        if num>max_element:
            # Updating the maximum value
            max_element=num
    
    return max_element

"""
# Time Complexity: O(n)
- Only single loop

# Space Complexity: O(1)
- Only one max_element variable
- regardless of array size
"""
