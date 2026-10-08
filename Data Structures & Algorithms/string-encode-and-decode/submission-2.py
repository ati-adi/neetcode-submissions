class Solution:
    def encode(self, strs):
        encoded_string = ""
        for word in strs:
            encoded_string += f"{len(word)}#{word}"
        return encoded_string
    
    def decode(self, s):
        decoded_strs = []

        i = 0
        
        while i < len(s):
            index = int(s.find("#", i))
            length = int(s[i:index])
            start = index + 1
            decoded_strs.append(s[start:start+length])
            i = start + length
        
        return decoded_strs