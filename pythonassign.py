#Week 2


#1
# a = int(input())
# if a%2 == 0:
#     print("even")
# else: print("odd")

#2
# a = int(input())
# if a < 0:print("-")
# elif a > 0:print("+")
# else:print("zero") 

#3
# a = int(input())
# if a>=0 & a<=100:
#     if a<=100 & a>= 85:
#         print("A")
#     elif a<85 & a>= 75:
#         print("B")
#     elif a<75 & a>= 65:
#         print("C")
#     elif a<65 & a>= 45:
#         print("D")
#     elif a<45 & a>= 0:
#         print("F")

#4
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a,b,c))   

#5
# for i in range(1,11):
#     print(i)

#6
# a = int(input())
# b = 0
# for i in range(a+1):
#     b += i
# print(b)

#7
s = input()
letters = 0
digits = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
print( letters)
print( digits)

#Assignment 1


