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
