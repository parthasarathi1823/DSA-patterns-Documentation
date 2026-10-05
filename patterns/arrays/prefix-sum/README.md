# Prefix Sum
---

## Table of contents
1. What is Prefix sum?
2. Real-life Analogy
3. Core Template
4. Examples
5. Problems Solved
6. Complexity Analysis
7. Practice Problems

---

## What is Prefix sum?
A prefix sum is the running total of all elements from the start, upto the current position.
**Here Every element in the prefix sum array is the sum of all elements from start to this position(including current)**

## Real life Analogy
Imagine you are saving money each month:

Month: Jan   Feb   Mar   Apr   

Saved: 100   50    200   150

Total by end of each month(Prefix sum):

Jan: 100   (just Jan)
Feb: 150   (Jan + Feb)
Mar: 350   (Jan + Feb + Mar)
Apr: 150   (Jan + Feb + Mar + Apr)

---
Given Array: [a0, a1, a2, a3, a4]
Prefix Sum : [p0, p1, p2, p3, p4]

prefix[0] = array[0]
prefix[1] = array[0] + array[1]
prefix[2] = array[0] + array[1] + array[2] 
.... 
....
....

**General Form:**
*prefix[n] = prefix[n-1] + array[n]* [for n >= 1] 
 
---
## Range sum Query:
Range sum is the prefix sum of specific part of elements in the array

**Example:** Prefix sum for Range[left,right] where left , right are indices of an array (where left < right)

so,

**Sum = prefix[right] - prefix[left-1]**

Edge Case: if left = 0

**Sum = prefix[right]

---

 
   
