def checkio(data):
    roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 0: ''}
    converted = ''

    remainder = 1
    div = 1000

    remainder = data % (div)
    num = data - data % div

    # print(data, num, remainder)

    while remainder == data:
        div = int(div / 10)
        remainder = data % (div)
        num = data - data % div

    # print(data, num, remainder)
    """
    if remainder == data:
        #print('100s')
        num = data - data % 100
        remainder = data%100

    if remainder == data:
        #print('10s')
        num = data - data % 10
        remainder = data%10

    if remainder == data:
        # print('10s')
        num = data
        remainder = data % 10
    """

    if remainder > 0 and remainder != data:
        # print('Calling with ', remainder)
        converted = checkio(remainder)

    if num > 0 and num <= 9:
        if num == 9:
            converted = roman[1] + roman[10] + converted
        elif num == 4:
            converted = roman[1] + roman[5] + converted
        else:
            five = num - num % 5
            ones = num - five
            converted = roman[five] + roman[1] * ones + converted
    elif num > 9 and num <= 99:
        if num == 90:
            converted = roman[10] + roman[100] + converted
        elif num == 40:
            converted = roman[10] + roman[50] + converted
        else:
            fiftys = num - num % 50
            tens = int((num - fiftys) / 10)
            converted = roman[fiftys] + roman[10] * tens + converted
    elif num > 99 and num <= 999:
        if num == 900:
            converted = roman[100] + roman[1000] + converted
        elif num == 400:
            converted = roman[100] + roman[500] + converted
        else:
            five_hunds = num - num % 500
            hunds = int((num - five_hunds) / 100)
            converted = roman[five_hunds] + roman[100] * hunds + converted
    elif num > 999:
        count_of_thousnds = int((num) / 1000)
        converted = roman[1000] * count_of_thousnds + converted

    # print(str(data),converted)

    # replace this for solution
    return converted


print(checkio(3889))  # == 'MMMDCCCLXXXVIII', '3888'
print(checkio(3999))  # == 'MMMDCCCLXXXVIII', '3888'
print(checkio(1))  # == 'I', '1'
print("Output:", checkio(44))  # == 'MMMDCCCLXXXVIII', '3888'
print("Output:", checkio(4))  # == 'MMMDCCCLXXXVIII', '3888'
