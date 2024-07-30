'''
1109. Corporate Flight Bookings

There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.
'''


'''
差分
'''
def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    result = [0] * (n+1)
    #mark the range with the deltas (head and tail)
    for f, t, s in bookings:
        result[f-1] += s
        result[t] -= s
        # print(result)
    #cumulative sum processing
    tmp = 0
    for i in range(n):
        tmp += result[i]
        result[i] = tmp
    return result[:n]