import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        [[1,10],[2,10],[3,10],[4,10]]
        [0,1]
        Sort the meetings with the key to be the start time. 
        key for the heap would be (end_time, room)

        we would peek and check if the currStartTime > end_time of the top element. If it is then we are chilling. We just assign that room. 
        Otherwise we would just need to wait till that room becomes empty. So increase the time to that start tiem. Cause that is when the first meeting room would be free. 
        Would there be any case were there is a better room at this point? i dont think so 
        '''
        rooms = [(0, room) for room in range(n)]
        heapq.heapify(rooms)
        meetings.sort()
        # keep track of rooms
        usages = [0] * n 
        for meeting in meetings:
            st, et = meeting[0], meeting[1]
            # fixes it 
            while rooms and rooms[0][0] < st:
                ret, room = heapq.heappop(rooms)
                heapq.heappush(rooms, (st, room))
            ret, room = heapq.heappop(rooms)
            usages[room] += 1 
            if st >= ret: 
                # room is available 
                heapq.heappush(rooms, (et, room))
            else:
                # need to wait for the room to be free. 
                heapq.heappush(rooms, (ret + et - st, room))
        print(usages)
        return usages.index(max(usages))