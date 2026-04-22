class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        unique = list(set(nums))
        return len(unique) != len(nums)