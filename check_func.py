def checkio(f,g):

    # Replace with your code
    print('running checkio')
    def h(*args,**kwargs):
        print(f())
        print('running h')
        print(*args, *kwargs)
        print('ended h')

    return h


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # (x+y)(x-y)/(x-y)
    f = checkio(lambda x, y: x + y,
            lambda x, y: (x ** 2 - y ** 2) / (x - y)
            )

    f()