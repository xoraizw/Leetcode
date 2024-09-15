def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqOfDigits(n):
            temp = str(n)
            total = 0
            for x in temp:
                total += int(x) * int(x)
            return total
        if n > 1 and n < 10: return False
        seen = []        
        def helper(n):
            if n == 1:
                print("here") 
                return True
            new = sqOfDigits(n)
            if new in seen: 
                return False
            else:
                seen.append(new)
            helper(new)
        print(helper(n))
        return helper(n)