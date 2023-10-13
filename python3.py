#1
a = int(input('Введите число a '))
b = int(input('Введите число b '))

for i in range(a, b + 1):
    print(i, end=' ')
#2
a = int(input('Введите число a '))
b = int(input('Введите число b '))
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end = ' ')
#3
repeat = int(input('Введите кол-во повторов, за тем напишите все чиста: '))
nums = int(0)
for i in range(repeat):
    nums += int(input())

print(nums)
#4
n = int(input('Введите число n! '))
nums = 1
for i in range(1, n + 1):
    nums *= i

print(nums)
#5
num = int(input('Введите кол-во ступенек: '))
if num > 9:
    print('Введите число от 1 до 9')
else:
    for i in range(num + 1):
        for l in range(1, i + 1):
            print(l, end='')
        print()
#6
n = int(input('Введите число n: '))
x = 1
while x ** 2 < n:
    print(x ** 2)
    x += 1
#7
num = int(input('Введите число: '))
st = 2
p = 1
while st <= num:
    st *= 2
    p += 1
print(p - 1, st // 2)
#8
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
line = x
day = 0

while line <= y:
    line += 0.1 * line
    day += 1
print(day)
#9
num = 0

while int(input('Введите число: ')) != 0:
    num += 1

print(num)
#10
first_num = int(input('Введите число: '))
nums = 0
while first_num != 0:
    plus = int(input('Введите число: '))
    if plus > first_num:
        nums += 1
    first_num = plus    
print(nums)
#11
nums = []

num = int(input('Введите число: '))

while num != 0:
    nums.append(num)
    num = int(input('Введите число: '))

print('Второе число максимальное число: ', sorted(nums, reverse=True)[1])
#12
def func(nums):
    if nums == 1 or nums == 2:
        return 1
    else:
        return func(nums - 1) + func(nums - 2)


num = int(input('Введите число: '))
print('Число Фибоначчи: ', func(num))
#13
nums = []
num = int(input('Введите число (0 для завершения): '))

while num != 0:
    nums.append(num)
    num = int(input('Введите число (0 для завершения): '))

max_repeat = 1
repeat = 1

for i in range(1, len(nums)):
    
    if nums[i] == nums[i-1]:
        repeat += 1
    else:
        repeat = 1
    if repeat > max_repeat:
        max_repeat = repeat


print('Максимальное кол-во повторов: ', max_repeat)
#14
a = input().split()
for i in range(0, len(a), 2):
    print(a[i])
#15
a = input('Введите числа: ').split()

for i in range(0, len(a), 2):
    print(a[i])
#16
nums = input('Введите список чисел через пробел: ').split()

nums = [int(num) for num in nums]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        print(nums[i])
#17
nums = input('Введите числа через пробел: ').split()

nums = [int(num) for num in nums]

max_num = max(nums)
index = nums.index(max_num)

print('Наибольшее число: ', max_num)
print('Индекс наибольшего числа: ', index)
#18
hs = input('Введите рост людей в строю через пробел: ').split()
hs = [int(h) for h in hs]
h_p = int(input('Рост Пети: '))
stay = 1

for h in hs:

    if h >= h_p:
        stay += 1
    else:
        break


print('Петин номер в строю: ', stay)
#19
nums = input('Введите чисела через пробел: ').split()

nums = [int(num) for num in nums]

for i in range(0, len(nums)-1, 2):
    nums[i], nums[i+1] = nums[i+1], nums[i]

print('Измененный список чисел: ', nums)
#20
nums = input('Введите список чисел через пробел: ').split()

nums = [int(num) for num in nums]

min = min(nums)
max = max(nums)
min_index = nums.index(min)
max_index = nums.index(max)

nums[min_index], nums[max_index] = nums[max_index], nums[min_index]

print('Обмен местами макс. и мин. числами: ', nums)
#21
nums = input('Введите числа через пробел: ').split()
nums = [int(num) for num in nums]

k = int(input('Введите индекс который нужно удалить: '))

for i in range(k, len(nums)-1):
    nums[i] = nums[i+1]

nums.pop()

print('Измененный список чисел: ', nums)
#22
nums = input('Введите числа через пробел: ').split()

nums = [int(num) for num in nums]

k = int(input('Введите индекс куда вставить число: '))
c = int(input('Введите число которое вставить: '))

if k > len(nums):
    k = len(nums)

nums.append(0) 
for i in range(len(nums)-1, k, -1):
    nums[i] = nums[i-1]
    nums[k] = c
    nums.pop()

print('Измененный список чисел: ', nums)
#23
queen = []

for a in range(8):
    x, y = map(int, input('Введите координаты ферзя (x, y) через пробел: ').split())
    queen.append((x, y))

attack = False

for i in range(8):
    for j in range(i+1, 8):
        x1, y1 = queen[i]
        x2, y2 = queen[j]
    if x1 == x2 or y1 == y2 or abs(x2-x1) == abs(y2-y1):
        attack = True
    break

if attack:
    print('YES')
else:
    print('NO')