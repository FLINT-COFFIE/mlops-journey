class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = list(set(nums))
        return len(unique) != len(nums) 