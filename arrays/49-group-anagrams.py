# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I want to sort a string (basically) or come up with an efficient way to count each letter in a string
        # I will just do this by converting this string to an array and then sorting the array. This could have a helper method
        # Next, I need to iterate through the array and compare the output of that helper function to the output of the function for the key word.
        #   If a word fits an anagram, add it to that list, otherwise, make a new list and it to the collection.
        def sortString(s: str) -> str:
            # would look up how to do this in one line in python
            # but I don't have that resource at the moment...
            output = ''
            for letter in sorted(s):
                output += letter
            return output #every string that IS an anagram will have the same output in this list.
        anagrams = {} # going to return just the values of this after iterating through the list.
        for word in strs:
            sortedWord = sortString(word)
            if sortedWord in anagrams: # in anagrams -> in anagrams.keys()
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]
        
        return anagrams.values()