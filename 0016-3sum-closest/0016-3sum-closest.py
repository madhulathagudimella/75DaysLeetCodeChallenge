class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                curr = nums[i] + nums[left] + nums[right]

                if curr == target:
                    return curr

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target:
                    left += 1
                else:
                    right -= 1

        return closest