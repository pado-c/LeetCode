class Solution:
    def permute(self, nums: List[int]):
        from itertools import permutations  #permutations는 순서 고려, combination는 순서 고려X
        res = permutations(nums, len(nums))   #nums리스트에서 len(nums)개의 원소를 골라 나열
        return res