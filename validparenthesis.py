s=input("Enter parentheses: ")
stack=[]
pairs = {'}': '{', ')': '(', ']': '['} 

for char in s:
    if char in '{[(':
        stack.append(char)
    else:
        if not stack or stack[-1]!=pairs[char]:
            print("invalid")
            break
        stack.pop() 
else:
    print("valid" if not stack else "invalid")