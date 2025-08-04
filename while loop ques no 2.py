
#accept a number and check if it is a palilindromic number (if number and it revers are equal) 121
 
a=int(input("tell you number:-"))
copy = a
rev = 0
while a > 0:
    rev = rev * 10 +a % 10
    a = a // 10
if copy == rev:
       print("it is a polindromic number")
else:
        print("it is  not a polindromic number")