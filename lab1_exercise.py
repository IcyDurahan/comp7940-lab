# Find all the factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10 % 3 = 1
print('exercise 1')
x = 52633
for i in range(2, x):
	if x%i ==0:
		print(i)


# Write a function that prints all factors of the given parameter x
print('exercise 2')
def print_factor(x):
	for i in range(2, x):
		if x % i == 0:
			print(i)
print_factor(52633)
# Write a program to find all factors of the numbers in the list l
print('exercise 3')
l = [52633, 8137, 1024, 999]

for x in l:
    print("Factors of", x)
    print_factor(x)
    print("-" * 20)