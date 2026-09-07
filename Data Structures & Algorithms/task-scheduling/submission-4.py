class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = {}
        for task in tasks:
            freqMap[task] = freqMap.get(task,0) + 1
        
        maxFreqTaskCount = 0
        for task in freqMap:
            if freqMap[task] > maxFreqTaskCount:
                maxFreqTask = task
                maxFreqTaskCount = freqMap[task]
            
        idle = (maxFreqTaskCount - 1) * n

        for task in freqMap:
            if task != maxFreqTask:
                idle -= min(maxFreqTaskCount - 1, freqMap[task])
        
        if idle > 0:
            return idle + len(tasks)
        return len(tasks)

        