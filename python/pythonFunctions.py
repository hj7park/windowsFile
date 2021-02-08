##Part1
#1
def pokemon_contains(incoming_letter):
	if incoming_letter in "pokemon":
		return True
	else:
		return False
result1 = pokemon_contains("k")
print(result1)
result1 =pokemon_contains("o")
print(result1)

#2
def sum_two(a,b):
	answer = a + b
	return answer
	
result3 = sum_two(999,1)
print(result3)
result4 = sum_two(5,6)
print(result4)

#3
def multiply(num1,num2):
	return num1 * num2

result5 = multiply(10,10)
print(result5)
result6 = multiply(5,6)
print(result6)


#4
def multiplication(a,b):
	my_answer = a*b
	print("Calculating...")
	return my_answer

print("Let's Multiply stuff...")
answer = multiplication(5,6)
answer = str(answer)
print("The answer is..." + answer)

#5
def subtract(a,b):
    return a-b
result7 = subtract(1,0)
result8 = subtract(20,20)
print(result7)
print(result8)

#6
def greater_than_5(num):
    if num >5:
        return True
    else:
        return False

result9 = greater_than_5(5)
result10 = greater_than_5(6)
print(result9)
print(result10)



##part2
#1
def sum_to(num):
    if num == 0:
        return num
    else:
        return num + sum_to(num-1)
print(sum_to(6))
print(sum_to(10))

#2
def largest(arr):
    high = 0
    for a in arr:
        if high < a:
            high = a
    return high

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231


#3
def occurances(long,short):
    if short not in long:
        return 0
    else:
        count = 0
        for idx,l in enumerate(long):
            if l == short[0]:
                valid = True
                for idx2,s in enumerate(short):
                    if s != long[idx+idx2]:
                        valid = False
                if valid:
                    count = count +1
        return count

print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))  # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0


#4
def product(*args):
    mult =1
    for arg in args:
        mult *= arg
    return mult

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0