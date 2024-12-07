# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[i for i in s if i in "aeiouAEIOU"]
        result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
        return "".join(result)


        result=[]
        for i in s:
            if i not in "aeiouAEIOU":
                result.append(i)
            else:
                # vowels.pop() removes and returns the last item from the vowels
                result.append(vowels.pop()) 