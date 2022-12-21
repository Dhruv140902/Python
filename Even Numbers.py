# for x in range(1,101): 
# 	if (x%2 == 0): 
# 	       print(x) 

# for i in range(0, 101, 2): 
# 	print(i) 

# for i in range(1, 101, 2): 
#     print(i)

# for i in range(1, 101, 3):
#     	print(i)

def even_numbers(number): 
	for i in range(number): 
		if i == 0: 
			continue 
		elif i%2 == 0: 
			print (i)
		else: 
			continue 
even_numbers(101)



