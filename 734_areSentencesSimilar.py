class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        """
        Time:   O(n+m), where n is len(sentence1) and m is len(similarPairs)
        Space:  O(m)
        """
        if len(sentence1) != len(sentence2):
            return False 
        
        sim = collections.defaultdict(list)
        for word1, word2 in similarPairs:
            sim[word1].append(word2) 
            sim[word2].append(word1)
        for i, word1 in enumerate(sentence1):
            word2 = sentence2[i]
            if word1 == word2:
                continue 
            if (word1 in sim and word2 not in sim[word1]) or (word2 in sim and word1 not in sim[word2]):
                return False
            if (word1 not in sim) and (word2 not in sim):
                return False 

        return True 

