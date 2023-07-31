# n=(int(input("Введите число N элементов: ")))
# num_list_one=[]
# for i in range(n):
#     num = int(input("Введите число для первого массива "))
#     num_list_one.append(num)
# print(num_list_one)


# m=(int(input("Введите число M элементов: ")))
# num_list_two = []
# for i in range(m):
#     num = int(input("Введите число для второго массива "))
#     num_list_two.append(num)
# print(num_list_two)


# num_list3 = num_list_one+num_list_two

# for i in set(num_list3):
#     if num_list3.count(i) > 1:
#         print(i)


import random
kust_quantity = int(input("введите количество кустов: "))
berries = list(random.randint(0, 10) for i in range(kust_quantity))

result = []
i = 0
sum = 0

while (i < kust_quantity):
    if (i == kust_quantity - 1):
        sum = berries[i] + berries[i - 1] + berries[0]
    else:
        sum = berries[i] + berries[i - 1] + berries[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(berries)

print(f"максимальное число ягод за один проход {result[-1]}")

