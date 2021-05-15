def twosum(nums,target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if i != j and nums[i] + nums[j]== target: # x != yは　xとyが等しくない
                return i,j

from random import randint
long_list= []
for _ in range(10000):
    long_list.append(randint(0, 500))
target= max(long_list)
def n_of_two_in(num_list, n):
    for i in range(len(num_list)):
        if num_list[i] < n:
            comp_val= n -num_list[i]
            if comp_val in num_list:
                return i, num_list.index(comp_val, i)
if __name__== '__main__':
    print(n_of_two_in(long_list, target))

def twosum(nums,target):
    values = set(nums).intersection(target-n for n in nums) # matching values
    v1,v2  = min(values),max(values)           # complementary values
    i1     = nums.index(v1)                    # indexes of 1st value
    i2     = nums.index(v2,(i1+1)*(v1==v2))    # index of second value
    return i1,i2    
