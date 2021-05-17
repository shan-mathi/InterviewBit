
def insert(intervals, new_interval):
    ans=[]
    p=0
    for j,i in enumerate(intervals):
        if new_interval[p]<i[1]:
            if p!=1:
                sub_ans=[i[0]]
                p+=1
            elif new_interval[p]<i[0]:
                sub_ans.append(new_interval[p])
                ans.append(sub_ans)
                ans.extend(intervals[j:])
                break
            elif new_interval[p]<i[1]:
                sub_ans.append(i[1])
                ans.append(sub_ans)
                ans.extend(intervals[j+1:])
                break

        elif not p:
            ans.append(i)
    return ans











intervals =[[1,2],[3,5],[6,7],[8,10],[12,16]]
new_intervals=[4,9]
#[[1, 2], [3, 10], [12, 16]]


print(insert(intervals,new_intervals))
