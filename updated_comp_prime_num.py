composite_number = 0
factors = []
comp = False
prime = [2,3,5,7]
for a in prime:
    if number%a == 0:
        comp = True
        composite_number = number
if not comp:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a composite number")

if comp == True:
    for i in prime:
        while composite_number%i == 0 :
            factors.append(i)
            composite_number //= i
    if composite_number > 1:
        factors.append(composite_number)
    else:
        pass
str_of_factors = ''
sum = 0
if composite_number:
    for i in factors:
        i = str(i)
        str_of_factors += i + ' '
    print(f"factors of composite are : {str_of_factors}")
    for q in factors:
        sum += q
    print(f"Sum of factors is {sum}")
