class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.s = s

        # First reverse the whole string
        self.reverse(0, len(self.s)-1)

        # find the "" and reverse the word as well
        l = 0 
        for r in range(len(self.s)):
            if self.s[r] == " ":
                self.reverse(l,r-1)
                l = r+1
        
        self.reverse(l,len(s)-1)
        
    def reverse(self,l, r):
        while l < r:
            t = self.s[l]
            self.s[l] = self.s[r]
            self.s[r] = t

            l += 1
            r -= 1
        

