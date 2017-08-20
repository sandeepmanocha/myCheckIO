import re

def checkio(text):
    regex = re.compile('\$[,.\d]+')


    nums = regex.findall(text)

    print(nums)
    print('--------')
    nums = [n[0:len(n)-1] if n[-1]=='.' or n[-1]==',' else n for n in nums]
    nums2 = [n for n in nums]
    print(nums2)

    for idx, c in enumerate(nums2):

        num = nums2[idx]
        num = num.replace('.',',')

        cnt = num.count(',')
        print('all . to ,:', num, '  cnt:', cnt)

        if cnt > 1:
            tp = num.split(',')
            print('last part:',tp[-1])
            if len(tp[-1]) < 3:
                num = num[::-1]
                num = num.replace(',','.',1)
                num = num[::-1]
        elif cnt == 1:
            tp = num.split(',')
            if len(tp[1]) == 2:
                num = num.replace(',', '.', 1)

        print(nums2[idx], 'to', num)
        nums2[idx] = num

    print(text)
    for idx,e in enumerate(nums2):
        #print('replace-->',nums[idx], 'with', e)
        text = text.replace(nums[idx],e)

    return text

if __name__ == '__main__':
    #print(checkio('$,34 is whar, $123,122.23   $3.344.344.34  $5 ddd $454,344  $3,444,344.45.  $34.343,'))
    #print(checkio('$222,100.455'))
    print(checkio('$4.545,45 is less than $5,454.54.'))