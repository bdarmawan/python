def simplify(path:str) -> str:
    stack = []
    cur = ""

    for c in path + "/":   # to make it uniform, add / at the end
        if c == "/":
            if cur == "..":
                if stack:  stack.pop()   # if stack is not empty, pop it
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""           # Tricky!!!
        else:
            cur += c

    return "/" +  "/".join(stack)



###
###TEST
path = "/../abc//./def/"
print(simplify(path))           # /abc/def

path = "/a/b/c/../.."
print(simplify(path))           # /a
