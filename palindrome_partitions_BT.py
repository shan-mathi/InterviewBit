def palindrom_part(s):
    ans=[]

    def all_pallindromes(A):
        """
        using the most optimal method i.e O(sqrt(n))

        :param A: a number
        :return: list of all its factors
        """
        ans = []
        for i in range(len(A)):
            for j in range(i + 1, len(A) + 1):
                if A[i:j] == A[i:j][::-1]:
                    ans.append(A[i:j])
        return ans

    all = all_pallindromes(s)

    def back_track( subset=[], booll=[0]*len(all)):
        ss = "".join(subset)

        if ss ==s:
            if subset not in ans:
                ans.append(subset[:])
            return

        for i in range(len(all)):
            if not booll[i]:
                subset.append(all[i])
                booll[i]=1
            else:
                continue
            if len("".join(subset))<=len(s):
                back_track(subset, booll)

            booll[i]=0
            subset.pop()
    back_track()
    return (ans)

if __name__ =="__main__":
    s = str(input())
    print(palindrom_part(s))




