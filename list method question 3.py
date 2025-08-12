#find the greatest element and print its index too
a=[23,56,98,89,67]
largest = a[0]
index = 0
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i


print(f'your largest number is{largest}a inex {index}')