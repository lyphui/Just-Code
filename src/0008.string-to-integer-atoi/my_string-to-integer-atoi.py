class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s[0]=='-':
            symbol=-1
            s=s[1:]
        elif s[0]=='+':
            symbol=1
            s=s[1:]
        result=0
        for alpha in s:
            if alpha.isdigit():
                result=result*10+int(alpha)
            else:
                break
        return min(2**31-1, max(result*symbol, -2**31))

    def myAtoi_ref(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ('+', '-'):
            s = s[1:]
        ret = i = 0
        while i < len(s) and s[i].isdigit():
            ret = ret * 10 + ord(s[i]) - ord('0')
            i += 1
        return min(2**31-1, max(sign*ret, -2**31))


nums = [2, 90,3,65,7, 12, 15]
target = "   -42"
s=Solution()
print(s.myAtoi(target))
print(s.myAtoi_ref(target))