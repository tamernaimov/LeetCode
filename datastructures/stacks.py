from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)
top_el = stack.pop() #removing last element
to_element = stack[-1]
print(stack)
print(top_el)
print(to_element)

strStack = deque("hello,")
reversedStr = ""
while strStack:
    reversedStr += strStack.pop()

print(reversedStr)
