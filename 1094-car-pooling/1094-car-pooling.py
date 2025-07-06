from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_capacity = 0
        trips.sort(key=lambda x: x[1])  # sort by start time

        drop_off = defaultdict(int)
        pick_up = defaultdict(int)

        for num_passengers, start, end in trips:
            drop_off[end] += num_passengers
            pick_up[start] += num_passengers

        for i in range(trips[-1][2] + 1):  # go up to the last drop-off point
            if i in drop_off:
                curr_capacity -= drop_off[i]

            if i in pick_up:
                curr_capacity += pick_up[i]

            if curr_capacity > capacity:
                return False

        return True
