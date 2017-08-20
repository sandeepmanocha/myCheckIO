import types

def min(*args, **kwargs):

    key = kwargs.get("key", None)
    #print(key, ", Type is ",type(key), key == int)
    print(args, kwargs)

    convert_type = ""
    if key != None and not type(key) is types.LambdaType:
        if key == int:
            convert_type = "int"
        elif key == str:
            convert_type = "str"
        elif key == float:
            convert_type = "float"

    print(convert_type)

    if type(key) is types.LambdaType:
        print("callable()")

    return None

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    print(key)
    return None


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( min(3, 2))# == 3, "Simple case max"
    print( min(3, 2))# == 2, "Simple case min"
    print( min([1, 2, 0, 3, 4]))# == 4, "From a list"
    print( min("hello"))# == "e", "From string"
    print( min(2.2, 5.6, 5.9, key=int))# == 5.6, "Two maximal items"
    print( min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))# == [9, 0], "lambda key"

    """
    print( max(3, 2))# == 3, "Simple case max"
    print( min(3, 2))# == 2, "Simple case min"
    print( max([1, 2, 0, 3, 4]))# == 4, "From a list"
    print( min("hello"))# == "e", "From string"
    print( max(2.2, 5.6, 5.9, key=int))# == 5.6, "Two maximal items"
    print( min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))# == [9, 0], "lambda key"
    """