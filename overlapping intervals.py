# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        ans=[]
        intervals.sort(key = lambda x: x.start)
        
        ans.append(intervals[0])
        #print(intervals[0])
        for i in intervals[1:]:
            prev_interval = ans[-1]
            if prev_interval.end >= i.start:
                #cool overlapping, but partially or fully overlapping? hmm..
                if prev_interval.end>=i.end:
                    #fully overlapping no changes
                    continue
                else:
                    #partial overlapping
                    prev_interval.end = i.end
            else:
                ans.append(i)
        return ans

