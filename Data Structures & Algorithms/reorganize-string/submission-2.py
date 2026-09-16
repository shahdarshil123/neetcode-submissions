class Solution:
    def reorganizeString(self, s: str) -> str:
        # Check the length of the string
        if len(s) == 1:
            return s
        
        # create a character map containing the freq of each elements
        charMap = {}
        for char in s:
            charMap[char] = charMap.get(char,0) + 1
        
        # create a maxheap for the characters
        heap = []  # -freq, char
        for char, freq in charMap.items():
            heap.append((-1*freq, char))

        heapq.heapify(heap)

        prev = None
        result = []

        while heap or prev:
            if prev and len(heap) == 0:
                return ""
            # pop max from heap
            if heap:
                freq, char = heapq.heappop(heap)
                result.append(char)
                freq += 1

                # check if prev exist:
                if prev:
                    heapq.heappush(heap, prev)
                    prev = None
                
                if freq < 0:
                    prev = (freq,char)     
            
        return "".join(result)
            


        
