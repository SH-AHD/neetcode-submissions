class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr=[0]*26
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')]+=1
            arr[ord(t[i])-ord('a')]-=1
        return all(a ==0 for a in arr)