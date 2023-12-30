# https://leetcode.com/problems/top-k-frequent-elements/submissions/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # probably stupid way of solving it
        elements = {}
        for num in nums:
            elements[num] = 1 if elements.get(num) is None else elements.get(num) + 1
        
        # make a sorted list using the frequencies
        sorted_by_frequency = sorted(elements, key=elements.get, reverse=True)

        # get the top k elements from the sorted dictionary
        return sorted_by_frequency[:k]