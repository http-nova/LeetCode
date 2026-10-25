# Last updated: 10/25/2026, 4:40:41 PM
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        seen = {}  # value -> index
4        for i, num in enumerate(nums):
5            complement = target - num
6            if complement in seen:
7                return [seen[complement], i]
8            seen[num] = i
9        
10
11# Synced seamlessly with LeetHub Pro
12# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
13# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna