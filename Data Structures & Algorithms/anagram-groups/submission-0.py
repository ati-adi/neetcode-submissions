class Solution:
    def groupAnagrams(self, strs):
        dict_s = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in dict_s:
                dict_s[sorted_word] = [word]
            else:
                dict_s[sorted_word].append(word)
        
        return list(dict_s.values())