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
# s = input()
# letters = 0
# digits = 0
# for ch in s:
#     if ch.isalpha():
#         letters += 1
#     elif ch.isdigit():
#         digits += 1
# print( letters)
# print( digits)





#Assignment 1
#1
# a = int(input())
# b = int(input())

# print(abs(a - b))

# 2
# a = int(input())

# for i in range(a+1):
#     if i%2 == 0:
#         print(i)

# 3
# a = int(input())
# for i in range(a):
    
#     print(a-1)
#     a = a - 1


# 4
# p = float(input())

# if p > 500:
#     total = p * 0.9
# else:
#     total = p

# print("TOTAL:", total, "USD Thank you!")


# 5
# n = input()

# f = int(n[0]) + int(n[1]) + int(n[2])
# l = int(n[3]) + int(n[4]) + int(n[5])

# if f == l:
#     print("Yes")
# else:
#     print("No")


# 6
# d = int(input())
# t1 = int(input())
# t2 = int(input())

# before = 15 / t1
# after = (d - 15) / t2

# if before > after:
#     print("Before")
# elif after > before:
#     print("After")
# else:
#     print("Equal")


# 7
# a = int(input())
# i = 0
# sum = 0
# total = 0
# while a != 0:
#     if a == 0:
#         break
#     sum += a
#     i += 1
#     total += a
#     a = int(input())
# avg = float(total / i)
# print(sum)
# print(avg)    

# 8
# num = int(input())

# max_num = num
# min_num = num

# while num != 0:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
#     num = int(input())

# print(max_num)
# print(min_num)


#9 
# s = 0
# n = int(input())
# while n != 0:
#     if n % 2 != 0:
#         s += n
#     num = int(input())
# print(s)


# 10
# num = int(input())

# sum = 0
# c = 0
# odd_sum = 0
# max_num = num
# min_num = num

# while num != 0:
#     sum += num
#     c +=  1

#     if num % 2 != 0:
#         odd_sum += num

#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

#     num = int(input())
# avg = sum / c
# print("Sum:", sum)
# print("Average:", avg)
# print("Min:", min_num)
# print("Max:", max_num)
# print("Odd Sum:", odd_sum)

b = input()

print((b[::-1]))


