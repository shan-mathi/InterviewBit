def letter_phone(s):
    ans=[]
    dic= {'1':'1',
          '2':'abc',
          '3':'def',
          '4':'ghi',
          '5':'jkl',
          '6':'mno',
          '7':'pqrs',
          '8':'tuv',
          '9':'wxyz',
          '0':'0'}
    def back_tracking(pos=0,sub_Set=''):

        if len(sub_Set)==len(s):      #GOAL
            ans.append(sub_Set)
            return

        for i in dic[s[pos]]:         #CHOICES
            sub_Set+=i
            if pos<len(s):     #CONSTRAINT
                back_tracking(pos+1,sub_Set)

            #pos-=1
            sub_Set = sub_Set[:-1]

    back_tracking()
    return ans

if __name__ =="__main__":
    s = str(input())
    print(letter_phone(s))
