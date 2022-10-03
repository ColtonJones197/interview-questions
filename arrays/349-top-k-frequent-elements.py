# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given nums, return the k most frequent elements
        # for sure need to iterate through the whole array
        # order of the array doesn't matter
        # so iterate through the list once and crunch it down to frequencies
        counts = {}
        frequencies = [[] for i in range(0, len(nums) + 1)]
        for num in nums:
            counts[num] = 1 if num not in counts else counts[num] + 1
        # now I have a big list of frequencies, so let's make a list
        for num, count in counts.items():
            frequencies[count].append(num)
            
        output = []
        for i in range(len(frequencies) - 1, 0, -1): #invert frequncies and start iterating through it
            for num in frequencies[i]:
                output.append(num)
                if len(output) == k:
                    return output