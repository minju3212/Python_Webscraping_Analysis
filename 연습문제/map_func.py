a_list = [1,2,3]
b_list = [4,5,6]
def add(a,b):
    return a+b
new_list = map(add,a_list,b_list)
print(list(new_list))