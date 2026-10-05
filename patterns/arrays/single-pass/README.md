# Single pass traversal

## Table of contents
1. What is Single pass traversal?
2. When to use it?
3. What is mindset/approach to solve this pattern?
4. Core Template
5. Examples
6. Problems Solved 
7. My Understanding 
8. Key Takeaways

## What is Single pass traversal?
- Single pass traversal is a process of going through the array once**(One Loop)** and Keeping track of information as we looping through.
- Use Variables to remember important Values in the array.

## When to use it?
We use single pass traversal when,
1. **Finding Min/Max**
  - Finding the minimum or maximum element in whole array.
2. **Counting Elements**
  - Take count of size of array  
3. **Checking conditions**
  - conditions like elements greater/smaller  than a number.
  - elements perfectly divisble by another numbers.
4.  Building Results while iterating
  - Use current iterating element and stored element to build result

## Solving Mindset
- Scan the array **once while keeping the needed information updated** (like sum,max,index, or hashmap).
- At each step **use the current element + stored information to decide the result**, so you never need to revisit elements

## Example Thought process
**Problem.** Find max element in the given array

**Single pass traversal**
---
Q. What I am looking for?
A. The Largest number in the array
 
Q. How did I get the maximum element?
A. On comparing every element

Q. How did I compare all elements in array only by single loop?
A. Store the max value in a variable Updating the max value in variable in each comparision(Usually we store first element in array as max,then updating it on comparision in traversal)
