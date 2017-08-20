def bitLenCount(num):

    length = 0
    count = 0
    while (num):
        count += (num & 1)
        length += 1
        num >>= 1
    return(length, count)

def valid(num):
    length, setBits = bitLenCount(num)

    if (setBits) % 2 == 0:
        #print(num, '--->', bin(num), length, setBits, 'Valid')
        return True
    else:
        #print(num, '--->', bin(num), length, setBits, 'Not Valid')
        return False

def checkio(msg):
    #print(msg)
    retval = [chr(m>>1) for m in msg if valid(m)]
    return ''.join(retval)
    #print(retval)


if __name__ == '__main__':

    print(checkio([144, 16, 210, 214]))


    assert checkio([135, 134, 124, 233, 209, 81,
             42, 202, 198, 194, 229, 215,
             230, 146, 28, 210, 145, 137,
             222, 158, 49, 81, 214, 157]) == "Checkio"
