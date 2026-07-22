class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sorted_letters = sorted(word)
            sorted_word = ''.join(sorted_letters)
            if sorted_word in dict:
                dict[sorted_word].append(word)
            else:
                dict[sorted_word] = [word]

        res = []
        for key in dict.keys():
            res.append(dict[key])

        return res

            