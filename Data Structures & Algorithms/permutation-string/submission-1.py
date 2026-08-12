class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        hash_map1 = {}

        for char in s1:
            hash_map1[char] = hash_map1.get(char,0) + 1
        for i in range(len(s2) - len(s1) + 1):
            hash_map2 = {}
            substring = s2[i:i+len(s1)]
            for char in substring:
                hash_map2[char] = hash_map2.get(char, 0) + 1
        
            #verify if the permutation exists:
            match = True
            for char in hash_map1.keys():
                if char not in hash_map2 or hash_map1[char] != hash_map2[char]:
                    match = False
                    break
            if match:
                return True
        
        return False