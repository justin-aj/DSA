"""
Steps:
Sorting:
nums = [-4, -1, -1, 0, 1, 2]
Outer Loop:
Start with nums[i] = -4.
Inner loop iterates over remaining elements to find valid triplets.
Example Triplet Formation:
i = 0, nums[i] = -4:

j = 1, nums[j] = -1:
target = -(nums[i] + nums[j]) = 5 (not in nums).
Continue checking other values of j.
i = 1, nums[i] = -1:

j = 2, nums[j] = -1:
target = 2 (found in nums), so triplet [-1, -1, 2] is added.
Continue checking for other triplets.

Why Use count Instead of Removing Elements Directly?
Using count avoids modifying the actual input array nums, which would make it harder to restore the state for future iterations.
It provides an efficient way to check whether the target number exists and is still available for use.

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        cnt = Counter(nums)
        count = defaultdict(int, cnt)

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res