class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):    #i에 nums 길이만큼의 숫자 대입
            tar = target - nums[i]    #tar = taget - nums에서 위치값이 i인 숫자
            if tar in nums[i+1:]:    #nums에서 i+1번째~마지막에 위치한 숫자 중 tar과 같은 게 있다면
                return  [i,nums.index(tar,i+1,)]    #a.index(b,c,d) => a에서 c~d번째 위치에서 b의 위치찾기
