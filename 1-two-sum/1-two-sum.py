class Solution:
    def twoSum(self, nums, target):
        for i in nums[0:len(nums)-1]:    #nums에서 마지막 숫자를 제외한 숫자를 i에 차례대로 대입
            for add in range(nums.index(i)+1,len(nums)):    #i 뒤에 오는 숫자들의 위치값을 add에 대입
                if i + nums[add] == target:    #i에 i 뒤에 오는 숫자들을 더했을 때 target과 같다면
                    output = []
                    output = [nums.index(i)] + [add]    #output = i의 위치값 + 더한 값의 위치값(add)
            
                    return output
        
