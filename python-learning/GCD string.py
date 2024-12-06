
class Solution:
    def gcdOfStrings(str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
print(Solution.gcdOfStrings("A","AA"))
