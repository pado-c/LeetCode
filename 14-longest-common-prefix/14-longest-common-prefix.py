class Solution:
    def longestCommonPrefix(self, strs):
        output = ""
        
        for i in range(len(strs[0])):   #strs[0]을 기준으로 비교
            for j in strs[1:]:    #j에 기준인 strs[0] 뒤에 위치한 문자열 대입
                #i가 j의 길이랑 같거나 더 클 때 or strs[0]과 j의 i번째 원소가 다를 때
                if i >= len(j) or strs[0][i] != j[i]:
                    return output
            #if에 해당하지 않을 때
            output += strs[0][i]

        return output