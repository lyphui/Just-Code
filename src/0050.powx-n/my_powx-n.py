class Solution:
    def myPow(self, x: float, n: int) -> float:
        p,result=abs(n),1

        while p>0:
            if p&1==1:
                result*=x
            x*=x
            p>>=1
        return result if n>0 else 1.0/result

s=Solution()
print(s.myPow(2.00000, -2))
