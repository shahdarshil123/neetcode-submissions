class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for word in strs:
            n = len(word)
            s = str(n)+"#"+word
            encoded_string.append(s)
        
        return "".join(encoded_string)
            

    def decode(self, s: str) -> List[str]:

        decoded_string = []
        i = 0
        while i < len(s):
            num = 0
            while i < len(s) and s[i] != "#":
                num = num*10 + int(s[i])
                i += 1
            decoded_string.append(s[i+1:i+num+1])
            i = i+num+1
        return decoded_string
