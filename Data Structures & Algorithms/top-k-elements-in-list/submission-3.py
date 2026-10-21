class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hash map to find the freq of the elements and track the max freq
        max_freq = -1

        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
            max_freq = max(max_freq, num_map[num])
        
        freq_map = defaultdict(list)
        for num in num_map:
            key = num_map[num]
            freq_map[key].append(num)
        
        # create result from the max_freq
        result = []
        freq = max_freq
        while k > 0:
            if freq in freq_map and len(freq_map[freq]) > 0 and k > 0:
                num = freq_map[freq].pop()
                result.append(num)
                k -= 1
            else:
                freq -= 1
        
        return result



