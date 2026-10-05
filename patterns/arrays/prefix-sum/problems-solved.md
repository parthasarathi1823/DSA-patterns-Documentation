# Problems Solved

### Problems where I used single pass traversal:

| Problem | Difficulty | Time Complexity | Space Complexity |
|---------|------------|-----------------|------------------|
| Running Sum of 1D Array | Easy | O(n) | O(1) |
| Find Pivot Index | Easy | O(n) | O(n) |



##  Leetcode Problems
- [1480](https://leetcode.com/problems/running-sum-of-1d-array/) - Running sum of 1D array
- [724](https://leetcode.com/problems/find-pivot-index/) - Find Pivot index


## Key Takeaways for the Prefix Sum Technique

1. **Preprocessing Advantage**:  
   - **Efficient Querying**: Precomputing the prefix sum allows for constant time O(1) querying for subarray sums after an initial O(n) preprocessing step.
  
2. **Time-Saving**:  
   - **O(n) Preprocessing + O(1) Queries**: The technique reduces repetitive calculations by storing cumulative sums, making it highly efficient for multiple range sum queries.

3. **Space Complexity Considerations**:  
   - **O(n) Space**: Requires additional space to store the prefix sums array, proportional to the input size. While space complexity increases, it provides fast querying.

4. **Improves Over Brute Force**:  
   - **Avoids Redundant Calculations**: Instead of recalculating sums from scratch for every query, the prefix sum array allows you to retrieve the sum of any subarray efficiently.

5. **Ideal for Range Sum Problems**:  
   - **Efficient Range Queries**: Especially useful in problems where multiple range sum queries are needed, such as in 2D matrix sum queries or finding the sum of subarrays.

6. **Flexibility**:  
   - **Can be Extended**: The technique can be extended to other aggregate operations like finding the sum of products or maximum/minimum values in a range with slight modifications.

7. **Optimal for Static Arrays**:  
   - **Works Best When the Data Doesn’t Change**: Prefix sum works efficiently when the input data remains static because any updates to the array require recalculating the prefix sum.

8. **Early Termination for Specific Queries**:  
   - **Direct Access**: Once the prefix sum array is built, querying becomes instant, saving time in cases where a quick lookup is needed for specific ranges.
---

part of DSA-patterns-Documentation-Arrays Next: [Two-Pointers](../two-pointers/README.md)

## Changelog

**v1.0**-Initial documentation
- Core concept explained
- 2 examples added 


---

**Prefix Sum**: A preprocessing technique that computes cumulative sums of elements to enable efficient range sum queries in constant time (O(1)) after an O(n) preprocessing step.

---

**Questions?Found an error? Want to improve this?**
Open an issue or submit a pull request!

---

**Tags:** #DSA #prefix_sum #patterns #fundementals
