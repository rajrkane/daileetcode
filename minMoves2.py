class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        Approach:   Sort to find median
        Time:       O(n*log(n))
        Space:      O(1)
        '''
        l = len(nums)
        if l == 1:
            return 0
        nums.sort()
        if l % 1 == 0:
            med = nums[l // 2]
        else:
            med = nums[(l - 1) // 2]
        moves = 0
        for num in nums:
            moves += abs(med - num)
        return moves
      
        '''
        Approach:   Quickselect to find median 
        Time:       O(n) average case, O(n^2) worst case 
        Space:      O(n) due to recursive call stack and new list allocated on each call
        '''
        def quickselect(arr: List[int], k: int) -> int:
            pivot = random.choice(arr)
            smaller = []
            bigger = []
            for num in arr:
                if num < pivot:
                    smaller.append(num)
                elif num > pivot:
                    bigger.append(num)
            if k <= len(smaller):
                return quickselect(smaller, k)
            elif k > len(arr) - len(bigger):
                return quickselect(bigger, k - (len(arr) - len(bigger)))
            else:
                return pivot 
            
        l = len(nums)
        if l == 1:
            return 0
        med = quickselect(nums, l // 2 + 1)
        moves = 0
        for num in nums:
            moves += abs(med - num)
        return moves 

