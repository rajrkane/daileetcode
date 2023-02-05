class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Time:   O(n^2*log(n)) or something 
        Space:  O(n)
        """
        # inorder = sorted(words, key=lambda word: [order.index(char) for char in word])
        # return inorder == words

        """
        Time:   O(n) to O(n*k), where n is len(words) and k is average len(words[i]) 
        Space:  O(1), since limited to 26 character alphabet
        """
        index = collections.defaultdict()
        for i, char in enumerate(order):
            index[char] = i
        for i in range(len(words)-1):
            if index[words[i][0]] < index[words[i+1][0]]:
                continue 
            elif index[words[i][0]] > index[words[i+1][0]]:
                return False 
            else:
                # letters are equal, so we need to find the first mismatch if one exists
                # key: only need to find FIRST mismatch. subsequent mismatches don't affect ordering 
                for j in range(len(words[i])):
                    # former word should not be longer than the latter word 
                    if j == len(words[i+1]):
                        return False 
                    if words[i][j] != words[i+1][j]:
                        if index[words[i][j]] > index[words[i+1][j]]:
                            return False 
                        # found the first mismatch, and the ordering is good, so move on to next pair of words 
                        break             

        return True 
