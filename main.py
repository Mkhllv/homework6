# # Exercise №1

from random import randint

# # Var №1
number = 1000
zero = str(number)
print(f'Number of zeros:', zero.count('0'))

# # Var №2
number = int(input('Enter the number: '))
zero = str(number)
count = 0
for i in zero:
    if i == '0':
        count += 1
print(f'Number of zeros:', count)

# # Exercise №2

number = 102000000
n = str(number)
zero = 0
for i in n[::-1]:
    if i == '0':
        zero += 1
    else:
        break
print(f'Number of zeros:', zero)

# # Exercise №3

my_list1 = [randint(1, 15) for a in range(15)]
my_list2 = [randint(1, 15) for b in range(15)]
print(f'my_list1:', my_list1)
print(f'my_list2:', my_list2)
my_result = my_list1[1::2] + my_list2[::2]
print(f'my_result:', my_result)

# # Exercise №4

my_list = [randint(1, 9) for i in range(4)]
print(f'my_list:', my_list)
print(f'revers:', my_list[1::] + my_list[0:1:1])

# # Exercise №5

my_list = [1, 2, 3, 4]
n = my_list.pop(0)
my_list.append(n)
print(f'revers:', my_list)

# # Exercise №6

a = '5 55 555'
b = a.split()
c = 0
for i in b:
    if i.isdigit():
        c += int(i)
print(c)

# # Exercise №7

my_str = "My long string"
l_limit = "o"
r_limit = "g"
a = my_str.find(l_limit)
b = my_str.rfind(r_limit)
find = my_str[a + 1: b]
print(find)

# Exercise №8

my_str = 'abcde'
a = []
b = len(my_str)
for i in range(0, b, 2):
    if i < b - 1:
        a.append(my_str[i] + my_str[i + 1])
    else:
        a.append(my_str[i] + '_')
print(a)

# Exercise №11

my_str = 'aaab'
a = []
for i in my_str:
    if my_str.count(i) == 1:
        a.append(i)
        print(i, end='')
print()

# Exercise №12

a = 'qwerty'
b = '1234qwer'
c = list(set(a) & set(b))
print(c)
