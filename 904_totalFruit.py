class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Time:   O(n)
        Space:  O(n), due to last dictionary (can be optimized further)
        """
        picked = set([fruits[0]])
        last = {fruits[0]:0}
        emptyBaskets = 1
        l, r, total = 0, 1, 1
        while r < len(fruits):
            if fruits[r] in picked:
                # fruit is one of the one/two type(s) in baskets, EXPAND the window
                last[fruits[r]] = r 
                r += 1
            else:
                if emptyBaskets == 1:
                    # fruit is put in second basket, EXPAND the window 
                    last[fruits[r]] = r
                    picked.add(fruits[r])
                    r += 1
                    emptyBaskets -= 1
                else:
                    # fruit is a third type, CONTRACT the window 
                    if fruits[r-1] == fruits[l]:
                        toRemove = [f for f in picked if f != fruits[l]][0]
                    else:
                        toRemove = fruits[l]
                    picked.remove(toRemove)
                    l = last[toRemove] + 1
                    emptyBaskets = 1
            total = max(total, r - l)
        return total 
