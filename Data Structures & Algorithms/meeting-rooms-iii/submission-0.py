class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if len(meetings) <= n:
            return 0

        # sort the meetings
        meetings.sort(key = lambda x: x[0])

        # create a hash map of the rooms 
        rooms = {i: [] for i in range(n)}

        for i in range(len(meetings)):
            start, end = meetings[i][0], meetings[i][1]
            meeting_placed = False
            earliest_available_room = 0
            earliest_available_time = float('inf')
            for j in range(n):
                if len(rooms[j]) > 0:
                    prev_start, prev_end = rooms[j][-1][0], rooms[j][-1][1]
                    if prev_end <= start:
                        rooms[j].append(meetings[i])
                        meeting_placed = True
                        break
                    else:
                        if prev_end < earliest_available_time:
                            earliest_available_time = prev_end
                            earliest_available_room = j
                else:
                    rooms[j].append(meetings[i])
                    meeting_placed = True
                    break 
            
            if not meeting_placed:
                rooms[earliest_available_room].append([earliest_available_time, earliest_available_time + (end - start)])
        
        max_meetings = 0
        max_meeting_room = 0
        for j in rooms:
            if len(rooms[j]) > max_meetings:
                max_meetings = len(rooms[j])
                max_meeting_room = j
        
        return max_meeting_room

                

