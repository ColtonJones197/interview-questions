# https://leetcode.com/problems/majority-element/submissions/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if count == 0:
                result = num
                count = 1
            else:
                if num == result:
                    count += 1
                else:
                    count -= 1
        return result
        
        
        ''' easy solution
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        n = len(nums)
        for num, count in hashMap.items():
            if count > n / 2:
                return num
        return -1
        '''