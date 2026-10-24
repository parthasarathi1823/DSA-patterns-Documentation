# Difference Between Peaks and Valleys

### Easy

## Problem

Biweekly Contest 194
Biweekly Contest 194

01:01:44

parthasarathiAccess all features with our Premium subscription!

My Lists

Favorites

Notebook

Progress

Points

Try New Features

Orders

My Playgrounds

Settings

Appearance

Appearance

System Default

Light

Dark

Sign Out

System Default

Light

Dark

Description
Description

Accepted
Accepted

Submissions
Submissions

Code
Code

Testcase
Testcase

Test Result
Test Result

Penalty Time

Accepted
a few seconds ago

Python3

--

99
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28

›
⌄
⌄
⌄
⌄
⌄
⌄

class Solution:
def peakValleyDifference(self, nums: list[int]) -> int:
if not nums:
return none

peak = valley = 0

# if nums[0]>nums[1]:
#     peak+=nums[0]
# else:
#     valley+=nums[0]

# if nums[-1]>nums[-2]:
#     peak+=nums[-1]
# else:
# valley+=nums[-1]

for i in range(1,len(nums)-1):

if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
peak+=nums[i]

if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
valley+=nums[i]

return peak-valley

In the editor, Tab inserts indentation. Press Ctrl+M to toggle whether Tab moves focus out of the editor. Press Ctrl+' to run the code. Press Ctrl+Enter to submit.

Restored from localUpgrade to Cloud Saving
Ln 1, Col 1

You must run your code first

All Submissions

Accepted1000 / 1000 testcases passed

parthasarathi
submitted at Oct 24, 2026 20:27

Runtime

2ms

Memory

19.18MB

Code
Python3

1class Solution:
2    def peakValleyDifference(self, nums: list[int]) -> int:
3        if not nums:
4            return none
5
6        peak = valley = 0
7
8        # if nums[0]>nums[1]:
9        #     peak+=nums[0]
10        # else:
11        #     valley+=nums[0]
12
13
14        # if nums[-1]>nums[-2]:
15        #     peak+=nums[-1]
16        # else:
17            # valley+=nums[-1]
18
19
20        for i in range(1,len(nums)-1):
21
22            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
23                peak+=nums[i]
24
25            if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
26                valley+=nums[i]
27
28        return peak-valley

View more

FindHeaderBarSize
FindTabBarSize
FindBorderBarSize

## Problem Link

[Difference Between Peaks and Valleys](https://leetcode.com/problems/difference-between-peaks-and-valleys/)
