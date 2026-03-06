
# Core Template

# Pattern: Nested Loops (Most Common)


def brute_force_search(arr,target):
    """
    Try every possible combination.

    Templete structure:
    - Outer loop: First choice
    - Inner loop: Second choice
    - check: Does this combination works?
    """
    n=len(arr)

    # Try every element
    for i in range(n):
        # with every other element
        for j in range(i+1,n):
            # check if this pair works
            if arr[i] + arr[j] == target:
                return [i,j] # if found return them
    

    # No solution found
    return None

"""
# Time Complexity: O(n²)
- Outer loop: n times
- Inner loop: n times
- Total: n x n = n²

# Space Complexity: O(1)
- only using few variables
- No extra data structures
"""
