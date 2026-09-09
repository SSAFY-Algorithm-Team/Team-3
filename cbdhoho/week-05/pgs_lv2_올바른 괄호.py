def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
    if stack:
        return False

    return True