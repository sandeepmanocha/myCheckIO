o = 113
n = o

nums = []
while n>0:
    r = n%10
    n= n//10
    nums.append(r)

letters = {
    1:"One",
    2:"Two",
    3:"Three",
    13:"Thirteen",
    100:"Hundred"
}

mp = 10
n=o
print(nums)
if n <= 20:
    print(letters[n])
else:
    for i in range(1, len(nums)):
        if i==1:
            print(letters[nums[i-1] + nums[i]*10])
        else:
            print(nums[i])

        mp = mp*10