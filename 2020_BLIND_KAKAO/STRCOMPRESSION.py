def solution(s):
    answer = 1000
    for i in range(len(s)):
        copy_s = s
        stack = []
        zip_str = ""
        cnt = int(len(s)/(i+1))
        stack.append(copy_s[:i+1])
        copy_s = copy_s[i+1:]
        for j in range(cnt):
            if j == cnt-1:
                zip_str += copy_s
            if stack[0] != copy_s[:i+1]:
                if len(stack) == 1:
                    zip_str = zip_str + stack[0]
                else:
                    zip_str = zip_str + str(len(stack)) + stack[0]
                stack = []
            stack.append(copy_s[:i+1])
            copy_s = copy_s[i+1:]
        answer = min(len(zip_str), answer)
    return answer