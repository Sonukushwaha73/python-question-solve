#print the sum of all even and odd number is a range separately 
n = int(input("Enter the number: "))
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += i
    else: 
        odd += i

print(f"The sum of even numbers is {even} and odd numbers is {odd}")
