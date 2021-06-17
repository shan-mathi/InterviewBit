def subset_dup(arr=[1,2,2]):
    ans = []
    arr.sort()

    def back_tracking(i=0, subset=[]):
        # goal
        if i == len(arr):
            if subset not in ans:
                ans.append(subset[:])
            return

        back_tracking(i + 1, subset)
        subset.append(arr[i])
        back_tracking(i + 1, subset)
        subset.pop()

    # function calling
    back_tracking()

    ans.sort()
    return ans

if __name__ =="__main__":
    print(subset_dup())
