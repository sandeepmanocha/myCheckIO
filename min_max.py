def min(*args, **kwargs):

    key = kwargs.get("key",None)

    print(key)

    order_as = ""

    print("str",isinstance(key, str), "int", isinstance(key,int))

    if isinstance(key,str):
        order_as = "str"
    elif isinstance(key,int):
        order_as = "int"

    vals_list = []



    arg_list = []

    print(order_as)

    if order_as == "str":
        print("list(args)", list(*args))
        arg_list = arg_list + list(*args)
    else:
        arg_list = args

    for val in arg_list:
        if isinstance(val, list):
            vals_list = vals_list + val
        else:
            vals_list.append(val)

    print("print(vals_list)",vals_list)
    for key in kwargs:
        vals_list.append(kwargs[key])



    min_val = None
    if len(vals_list) > 0:
        min_val = vals_list.pop(0)
    else:
        return None

    for val in vals_list:
        if val < min_val:
            min_val = val

    return min_val


def max(*args, **kwargs):
    vals_list = []
    keys = kwargs.keys()

    for val in args:
        if isinstance(val, list):
            vals_list = vals_list+val
        else:
            vals_list.append(val)

    for key in kwargs:
        vals_list.append(kwargs[key])

    max_val = 0
    if len(vals_list) > 0:
        max_val = vals_list.pop(0)
    else:
        return None

    for val in vals_list:
        if val > max_val:
            max_val = val

    return max_val

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    #print(min(3,2,my=8,your=9))
    #print(max(3, 2, my=8, your=9))
    #print(max([1, 2, 0, 3, 4]))
    print(min("hello", key=str))

    #print(max(1,29292,[1, 2, 0, 3, 4],key={a:10,b:999999}))
    """
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    """