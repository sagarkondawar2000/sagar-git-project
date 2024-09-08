from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Does not return anything. Modifies nums in-place.
        """
        k %= len(nums)  # Adjust k to be within the range of the array's length

        # Reverse the entire array
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Reverse the first k elements
        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Reverse the remaining elements
        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3  # Rotate 3 positions to the right

solution = Solution()
solution.rotate(nums, k)

print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
