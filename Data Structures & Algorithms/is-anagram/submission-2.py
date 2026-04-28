class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        a={}
        b={}
        for i in range(0, len(s)):
            if s[i] in a.keys():
                a[s[i]]=a[s[i]]+1
            else:
                a[s[i]]=1

            if t[i] in b.keys():
                b[t[i]]=b[t[i]]+1
            else:
                b[t[i]]=1
        

        
        if a==b:
            return True
        else:
            return False