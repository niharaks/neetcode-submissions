class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        a=[]
        b=[]
        for i in range(0, len(s)):
            a.append(s[i])
            b.append(t[i])
        

        a=sorted(a)
        b=sorted(b)

        if a==b:
            return True
        else:
            return False