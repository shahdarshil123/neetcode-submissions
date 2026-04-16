class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        p1 = 0
        p2 = 0

        while p1 < len(slots1) and p2 < len(slots2):
            s1, e1 = slots1[p1][0], slots1[p1][1]
            s2, e2 = slots2[p2][0], slots2[p2][1]

            if s1 <= s2 <= e1 or s2 <= s1 <= e2:
                s,e = max(s1,s2), min(e1,e2)
                if e - s >= duration:
                    return [s, s+duration]
            
            if e1 <= e2:
                p1 += 1
            else:
                p2 += 1
        
        return []

                
