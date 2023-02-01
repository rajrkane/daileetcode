class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        '''
        Approach:   two queues
        Time:       O(n)
        Space:      O(delay+forget)
        '''
        mod = 10**9 + 7
        # track number of people delayed on each day
        dq = collections.deque([1])
        # track number of people holding the secret (i.e. waiting to forget) on each day 
        fq = collections.deque([1])
        # track number of people who share the secret that day 
        sharing = 0
        for i in range(1, n):
            # people who are no longer delayed can now share the secret
            if len(dq) >= delay:
                sharing += dq.popleft() % mod
            # people who forget the secret can no longer share it 
            if len(fq) >= forget:
                sharing -= fq.popleft() % mod 
            # each person who can share the secret does so to one more person 
            dq.append(sharing)
            fq.append(sharing)
        return sum(fq) % mod
