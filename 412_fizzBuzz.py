class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Time:   O(n)
        Space:  O(1), excluding return array 
        """
        ans = ["" for _ in range(n)]
        for i in range(n):
            div3 = (i+1) % 3 == 0
            div5 = (i+1) % 5 == 0
            if div3:
                ans[i] = "Fizz"
            if div5:
                ans[i] += "Buzz"
            if len(ans[i]) == 0:
                ans[i] = str(i+1)
        return ans 

        """
        more generalizable solution
        Time:   O(n)
        Space:  O(1), excluding return array 
        """
        fizzbuzz = {3: "Fizz", 5: "Buzz"}
        ans = ["" for _ in range(n)]
        for i in range(n):
            for k in fizzbuzz:
                if (i+1) % k == 0:
                    ans[i] += fizzbuzz[k]
            if ans[i] == "":
                ans[i] = str(i+1)
        return ans
