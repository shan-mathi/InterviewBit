s = Stack()
strr = str(input())
def parant_check(strr,s):
    map = {']':'[','}':'{',')':'('}
    for i in strr:
        if i in ['[','{','(']:
            s.push(i)
        elif i in [']','}',')']:
            if not s.is_empty() and s.peek() == map[i]:
                s.pop()
            else:
                return False
    if s.size()==0:
        return True
    else:
        return False

print(parant_check(strr,s))
