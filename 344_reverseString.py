class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        Time:   O(n)
        Space:  O(1)
        '''
        # Python comma swapping simply rebinds names to existing values
        # In a different language, you would declare a tmp var before the loop and reassign it on each iteration
        for i in range(len(s) // 2): 
            s[i], s[-i-1] = s[-i-1], s[i]
            
