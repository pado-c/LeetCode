int_roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
class Solution:
    def intToRoman(self, num: int):
        output = ''    #return 값
        unit = []    #num을 자릿값으로 구분해 넣을 list(num이 66이라면 unit = ['60','6'])
        for i in range(len(str(num))):    #num의 길이(int는 len함수 적용✕ → str으로 변환)
            unit += [str(num)[i] + '0'*(len(str(num))-1-i)]

        unit = list(map(int,unit))    #num이 66이라면 unit = [60,6]
        keys = list(int_roman.keys())    #int_roman의 keys만 모아서 list
        for i in unit:
            keys += [i]    #keys 리스트에 i 추가
            keys.sort()    #keys 오름차순(1,2,3...) 정렬

            if str(i)[0] in ['1','5']:    #i의 앞자리가 1,5일 때(int는 슬라이싱✕ → str으로 변환)
                output += int_roman[i]

            elif str(i)[0] in ['4','9']:    #i의 앞자리가 4,9일 때
                minus = keys[keys.index(i)+1] - i    #minus = 1000-900 or 50-40
                output += int_roman[minus] + int_roman[keys[keys.index(i)+1]]    #keys.index(i)는 keys 에서 i의 위치

            elif str(i)[0] in ['2','3']:    #i의 앞자리가 2,3
                q = i // keys[keys.index(i) -1]    # i가 20이면 q = 20 // 10
                output += ( int_roman[keys[keys.index(i)-1]] * q )

            elif str(i)[0] in ['6','7','8']:    #i의 앞자리가 6,7,8
                r = str(i % keys[keys.index(i) -1])    #i가 60이면 r = 60 % 50
                output += int_roman[keys[keys.index(i)-1]] + (int_roman[keys[keys.index(i)-2]] * int(r[0]))

            elif str(i)[0] == '0':    #i의 앞자리가 0일 때(0,00,000...)
                continue

            keys.remove(i)    #keys에서 i 제거
        return output    #''를 기준으로 output을 합쳐 str로 반환