
## BRUTE FORCE - The Foundation of Problem Solving

## Table of Contents
1. What is Brute Force?
2. When to Use Brute Force
3. The Brute Force Mindset
4. Core Templete
5. Examples
6. Problems solved
7. My Understanding

## What is Brute Force?

Brute Force is the first ans straight-forward approach to solve a Problem.
**We try every possible solution** Untill we find the right one.

### Simple Analogy

Imagine you lost your key somewhere in your house. The Brute Force apporach 
is to check the **every single room,drawer,and corner** untill find it.It
is NOT efficient, but guaranteed to work if key is there!

### Why Learn This First?

- **Always works**(If solution exists)
- **Easy to understand** and Implement
- **Starting point for Optimization**
- **Build's problem solving intution**
- **Better than no solution**

## When to use Brute Force

### Use Brute Force When:

1.**Problem input size is small**
  - Input size: n<=1000
  - Time limits are generous

2.**First approach in Interview**
  - Write something work first, then optimise
  - something is better than nothing

3. **Learning a new problem type**
  - Understand the problem
  - See all cases clearly

4. **Correctness is priority**
  - Need to verify edge cases
  - Want to be absolutely sure

### Caution When:
- Input size is large(n > 10,000)
- Time complexity matter's
- Multiple test cases(amplifies sloness)

-------

## The Brute Force mindset

### The Thinking Process:

STEP 1: Understand what we're looking for 
"What is the question asking?"

STEP 2: Identify all possibilities
"What is the way to check all possible possibility?"

STEP 3: Check each one
"Let me try each possibility and compare with answer we need"

STEP 4: Return the answer
"Found it! or "Doesn't exist"

-------

### Example Thought Process:

**Problem.** Find two number's in array that sum to target

**Brute Force Thinking**
---
Q. What am I looking for?
A. Any two numbers add up equal's to target 

Q. What are all possiblilities?
A. Every pair of numbers in the array

Q. How to check all pairs?
A. Try first element with all other elements, then second element
   with all other elements and so on...

---

