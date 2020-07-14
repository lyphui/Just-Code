class Solution:
    def reverse(self, x):
        if x>-10 and x<10:
            return x

        result=0
        if x>0:
            while x>0:
                result=result*10+x%10
                x//=10
            result = 0 if result > pow(2, 31) else result
        else:
            x=-x
            while x>0:
                result=result*10+x%10
                x//=10
            result = 0 if result > pow(2, 31) else result
            result=-result
        return 0 if result > pow(2, 31) else result
    def reverse_ref(self, x):
        result = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        while x:
            result = result * 10 + x % 10
            x //= 10

        return 0 if result > pow(2, 31) else result * symbol

nums = [2, 90,3,65,7, 12, 15]
target = -579
s=Solution()
print(s.reverse(target))
print(s.reverse(target))