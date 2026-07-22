class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False

        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            if s[i] not in dict:
                dict[s[i]] = 1
            if t[i] in dict:
                dict[t[i]] -= 1
            if t[i] not in dict:
                dict[t[i]] = -1

        for key in dict.keys():
            if dict[key] != 0:
                return False
            return True 

    
        

        

        