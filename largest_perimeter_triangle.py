nums=[1,2,3,4,5]
value = 0
sumval = 0
num = []
for i in range(0,len(nums)-2):
    for j in range(0,len(nums)-1):
        for k in range(0,len(nums)):
            num=[nums[i],nums[j],nums[k]]
            print(num)