import re
# # a = 10
# # b = 10
# # c = 50
# # print('I love {0} and {1}'.format('milk','cornflakes'))
# # print('I love {1} and {0}'.format('milk','cornflakes'))
# # print(1,2,3,4 ,sep = "*")
# # print(1,2,3,4, sep = '##',end = '%')
#
# # print("Hello {name}, {batch}".format(name = 'vignesh', batch = 'DW8'))
#
# # num = input()
# # print(type(num))
#
# # name = input("Enter your name")
# # tamount = int(input("Enter the total amount"))
# # amount = int(input("Enter the amount to be withdrawn"))
# # branch = input("Enter the branch")
# # remamount = tamount - amount
# # # print("Hi {0}, you took  {1} from {2}, Karpakkam branch at 7:46pm on 09/02/2022, available balance is {3}".format(name,amount, branch, remamount ))
# #
# # a = 1
# # b = 2
# # c = 3
# # d = a*(b//c)-a+b
# #
# # print(d)
#
# # for i in range(1,6):
# #     print('*' * i)
#
# # i = int(input("Enter the value of i"))
# # for a in range(0,i):
# #     print(' '* (i-1)+'*'*a)
# # a = {1:2,3:4}
# # print(a[i])
#
# # a = [1,2,3,4]
# # bb = []
# # for i in a:
# #     if i not in bb:
# #         bb.append(a.count(i))
# # print(set(bb))
# num = int(input("Enter a number"))
# c = 0
# for i in range(1,num):
#     if(num%i==0):
#         print("not prime")
#         break
# else:
#     print("prime")
#
#
# # c = lambda a,b,c:((a+b+c)/c**(c//b))
# # print(c(1,2,3))
# #
# # print(list(filter(lambda a : type(a)==str, a)))
#
# i = range(2,num)
# print(list(filter(lambda num : num%i==0,i)))
# from functools import reduce
# a = [1,2,3,4,5,6,98,94,95,5]
# print(reduce(lambda a,b : str(a)+str(b),a))
#
# print({i:i**2 for i in a})

# Print the first negative integer in that window.If all the numbers are positive print 0
# n = int(input())
# l = input()
# k = int(input())
# b = list(map(lambda a: int(a), l.split()))
# c = []
# d = 1
# for j in range(k - 1, len(b)):
#     i = j - (k - 1)
#     while i <= j:
#         if b[i] < 0:
#             c.append(str(b[i]))
#             d = len(c)
#             break
#         i = i + 1
#     if (len(c) < d):
#         c.append('0')
#         d = d + 1
#
# print(" ".join(c))

# codekata question 3
# n = int(input())
# l = input()
# b = list(map(lambda a: int(a), l.split()))
# c = int(b[0])
# d = []
# a = 0
# for i in range(1, n):
#     if int(b[i]) < c:
#         d.append(str(b[i]))
#         c = int(b[i])
#     else:
#         a = a + 1
#     if a == (n-i):
#         d.append('-1')
#
# print(" ".join(d))

#first problem
# a = 1322456987
# d = 0
# sum1 = 0
# while a != 0:
#     d = a % 10
#     a = a//10
#     sum1 = sum1 + d
# print(sum1)

# sum = 0
# for i in range(1,11):
#     sum = sum + (a%(10**i)//(10**(i-1)))
# print(sum)

# ----------------------------------------------------------------
#fifth problem
#
# a = [1,1,1,2,2,2,3,3,3,4,4,4,10,9,8]
# d = {}
# maxi = 0
# maxi_ele = 0
# mini = 100
# mini_ele = 100
# for i in a:
#     d[i] = a.count(i)
# print(d)
# for key, value in d.items():
#     if value >= maxi and maxi_ele < key:
#         maxi = value
#         maxi_ele = key
#     if value <= mini:
#         mini = value
#         mini_ele = key
# print(maxi_ele, maxi)
# print(mini_ele, mini)



# # a = [9,5,3,2,4,6,5]
# # print([i*3 for i in a if i % 2 ==0])
# a = [1,3,4]
# def ier(a):
#     return [i for i in a if i % 3 == 0]
# print(ier(a))
#
# n = int(input())

#
# a = ['22-02-2022', '21-02-2022', 'malayalam']
# print(list([i for i in a if "".join(reversed(i.split())) == i.split()]))

# m = input()
# m = m.rstrip()
# c = 0
# for i in m:
#     print(m.count(i))
#     # if m.count(i)%2==0:
#     #     c = 1
#     # else:
#     #         print(1)
#     #         print(0)
#     #         c = 0
#     #         break
# if c!=0:
#     print(c)

# a = int(input())
# if a<10 and a>=0 or a<0 and a>-9:
#     print('Enter a number greater than 2 digits')
# else:
#     if a<0:
#         a = str(a*(-1))
#         print("-"+a[::-1])
#     else:
#         a = str(a[::-1])
#         print(a)

# m = input()
# l = []
# for i in range(0,len(m)-1):
#     if m[i] == m[i+1]:
#         pass
#     else:
#         l.append(m.count(m[i]))
#
# print(l)
# if len(l) == 3:
#     print('Wonder')
# else:
#     print(-1)
#
# b = re.compile('[1234567890@_!#$%^&*()<>?/\|}{~:]')
# a = 1
# print(b.search('5'))
# while a!=0:
#     username = input("Enter your username or email ID")
#     if b.search(username[0]) is None:
#         a = 0
#     else:
#         print("Invalid username, please do not use numbers or special characters in the beginning")
a = 1
b = 2
with open('geek1.txt','a+') as f:
    f.write('vignesh' +' ' + 'password')
    f.write('\n')
    f.seek(0)
    a = f.read()
    b = a.split()
    print(b)

