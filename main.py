def isValid(s):
    map={
        '}':'{',
        ")":"(",
        ']':'('
    }
    stack=[]

    for i in s:
        if i not in map:
            stack.append(i)
        else:
            if stack and stack[-1] ==map[i]:
                stack.pop()
            else:
                print (False)
    if not stack: print (True)

isValid("((}))")

