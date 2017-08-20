def flatten(dictionary):
    print("-" * 80)
    stack = [((), dictionary)]
    #print(stack)

    result = {}

    while stack:

        #print("*-*"*50)

        #print(stack)
        #print("*-" * 50)

        path, current = stack.pop()

        if len(current.items()) == 0:
            result["/".join((path))] =
        else:
            #print("-->" , "Path->",path, "| Current->", current)
            for k, v in current.items():
                #print("---->Key:",k,"Value:",v)
                if isinstance(v, dict):
                    stack.append((path + (k,), v))
                else:
                    result["/".join((path + (k,)))] = v

    return result



print(flatten({"root": {"deeper": {"more": {"enough": "value"}}}}))

print(flatten({"empty": {}}))
