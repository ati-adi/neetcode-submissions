class Solution:
    def encode(self, strs):
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
        return result
    
    def decode(self, s):
        output = []
        i = 0 
        while i < len(s):
            index = int(s.find("#", i))
            length = int(s[i:index])
            start = index + 1
            output.append(s[start:length+start])
            i = length + start
        return output