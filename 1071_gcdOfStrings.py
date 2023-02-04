class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Time:   O(min(m, n)*(m+n))
        Space:  O(m+n)
        """
        # if str1 + str2 != str2 + str1:
        #     return ""

        # def divides(pref: str, full: str) -> bool:
        #     return len(full) % len(prefix) == 0 and prefix * (len(full) // len(prefix)) == full

        # if len(str1) <= len(str2):
        #     shorter, longer = str1, str2
        # else:
        #     shorter, longer = str2, str1 
        # ans = ""
 
        # for i in range(1, len(shorter)+1):
        #     prefix = shorter[:i]
        #     if divides(prefix, shorter) and divides(prefix, longer) and len(prefix) > len(ans):
        #         ans = prefix

        # return ans

        """
        Time:   O(log(min(m, n)))
        Space:  O(log(min(m, n)))
        """
        if str1 + str2 != str2 + str1:
            return ""

        # euclidean algorithm for finding gcd of two integers
        def euclid(a: int, b: int) -> int:
            if a == 0:
                return b
            return euclid(b % a, a)

        length = euclid(len(str1), len(str2))
        return str1[:length]

        
