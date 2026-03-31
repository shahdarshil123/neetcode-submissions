class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        arr = []
        result = []

        def backtracking(i):
            if i >= len(s):
                if len(arr) == 4:
                    result.append(".".join(arr))
                return
            for j in range(i+1,len(s)+1):
                if len(s[i:j]) == 1 or (len(s[i:j]) > 1 and len(s[i:j]) <=3 and s[i] != '0' and int(s[i:j]) < 256) :
                    arr.append(s[i:j])
                    backtracking(j)
                    arr.pop()
        
        backtracking(0)
        return result

                
