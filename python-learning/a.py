import textwrap
class Solution:
    def gcdOfStrings(str1: str, str2: str) -> str:
        
 
        a=len(str1)
        b=len(str2)
        while b:
            a, b = b, a % b
            c=a

        if a > b:
            max_str = str1
            min_str = str2
        else:
            max_str = str2
            min_str = str1
            
        same = True
        print(len(max_str)//2+1)
        while same:            
            for i in range(len(max_str)//2+1):
                if len(set(textwrap.wrap(max_str, i+1))) ==1 and len(set(textwrap.wrap(min_str, i+1))) ==1  and set(textwrap.wrap(max_str, i+1))==set(textwrap.wrap(min_str, i+1)): 
                    out=min_str[:c]
                    print(len(out))
                    same=False
                    break
                else: out=""
            same=False
            return out



print(Solution.gcdOfStrings("A","AA"))

