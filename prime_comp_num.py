number = int(input("Enter number: ")) #To find weather a given number is composite or not
composite_number = 0
factors = []
prime = [2,3,5,7]
comp = False
if number%2 != 0 and number%3 != 0 and number%5 != 0 and number%7 != 0:
    print(f"{number} is a prime number.")
elif number in prime:
    print(f"{number} is prime number.")
else:
    print(f"{number} is a composite number")
    composite_number = number
    comp = True
while composite_number > 1:
    if composite_number%2 == 0:
        composite_number /=2
        factors.append(2)
    elif composite_number%3 == 0:
        composite_number /= 3
        factors.append(3)
    elif composite_number%5 == 0:
        composite_number /= 5
        factors.append(5)
    elif composite_number%7 == 7:
        composite_number /= 7
        factors.append(7)
    else :
        factors.append(composite_number)
        composite_number = 1

str_of_factors = ''
if composite_number:
    for i in factors:
        i = str(i)
        str_of_factors += i + ','
    print(f"factors of composite are : {str_of_factors}")








