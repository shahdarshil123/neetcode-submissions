class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1

        boats = 0
        while left < right:
            if people[right] + people[left] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            boats += 1
        if left == right:
            boats += 1
        
        return boats
