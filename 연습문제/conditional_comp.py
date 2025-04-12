n_list = [1,2,3,4,5,6,7,8,9,10]
new_list = [n**2 if n % 2 == 0 else n for n in n_list]
print(new_list)