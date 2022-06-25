int_roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

class Solution:
    def intToRoman(self, num: int):
        output = ''
        unit = []
        for i in range(len(str(num))):
            unit += [str(num)[i] + '0'*(len(str(num))-1-i)]

        unit = list(map(int,unit))
        keys = list(int_roman.keys())
        for i in unit:
            keys += [i]
            keys.sort()

            if str(i)[0] == '1' or str(i)[0] == '5':
                output += int_roman[i]

            elif str(i)[0] == '4' or str(i)[0] == '9':
                minus = keys[keys.index(i)+1] - i
                output += int_roman[minus] + int_roman[keys[keys.index(i)+1]]

            elif str(i)[0] == '2' or str(i)[0] == '3':
                iik = keys.index(i)
                q = i // keys[iik -1]
                output += ( int_roman[keys[iik-1]] * q )

            elif str(i)[0] == '6' or str(i)[0] == '7' or str(i)[0] == '8':
                iik = keys.index(i)
                r = str(i % keys[iik -1])
                output += int_roman[keys[iik-1]] + (int_roman[keys[iik-2]] * int(r[0]))

            elif str(i)[0] == '0':
                continue

            keys.remove(i)

        return output