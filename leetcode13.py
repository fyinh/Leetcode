class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = "MCMXCIV"
        roman_result = []
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4,
                         'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        i = 0
        while(i < len(s)):
            if (i == len(s) - 1):
                roman_result.append(s[i])
                i += 1
            else:
                if (s[i] == 'I'):
                    if (s[i+1] == 'V'):
                        roman_result.append('IV')
                        i += 2
                    elif (s[i+1] == 'X'):
                        roman_result.append('IX')
                        i += 2
                    else:
                        roman_result.append('I')
                        i += 1
                elif (s[i] == 'X'):
                    if (s[i+1] == 'L'):
                        roman_result.append('XL')
                        i += 2
                    elif (s[i+1] == 'C'):
                        roman_result.append('XC')
                        i += 2
                    else:
                        roman_result.append('X')
                        i += 1
                elif (s[i] == 'C'):
                    if (s[i+1] == 'D'):
                        roman_result.append('CD')
                        i += 2
                    elif (s[i+1] == 'M'):
                        roman_result.append('CM')
                        i += 2
                    else:
                        roman_result.append('C')
                        i += 1
                else:
                    roman_result.append(s[i])
                    i += 1
        sum = 0
        for i in roman_result:
            sum += roman_numerals[i]
        return sum