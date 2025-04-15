class Solution:
    def getSum(self, a: int, b: int) -> int:
        count = []
        if a > 0 and b > 0:
            for i in range(a):
                count.append(1)    
            for j in range(b):
                count.append(1)
            return sum(count)
        elif a == 0:
            return b
        elif b == 0:
            return a
        elif a < 0 and b > 0:
            for i in range(abs(a)):
                count.append(-1)
            for i in range(b):
                count.append(1)
            return sum(count)
        elif a > 0 and b < 0:
            for i in range(a):
                count.append(1)
            for i in range(abs(b)):
                count.append(-1)
            return sum(count)
        elif a < 0 and b < 0:
            for i in range(abs(a)):
                count.append(-1)
            for i in range(abs(b)):
                count.append(-1)
            return sum(count)
        else:
            return 0
