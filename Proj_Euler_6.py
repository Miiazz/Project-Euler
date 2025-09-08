#Prob 6

num_range = range(1,101)
nat_numbers = list(num_range)

x = sum(nat_numbers)
X = x **2

squared_list = [n **2 for n in nat_numbers]
nat_numbers_sqr = (squared_list)
y = sum(nat_numbers_sqr)

z = X-y
print(X)
print(y)
print(z)
