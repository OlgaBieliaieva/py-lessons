# for element in sequence:
    # виконувати дії з element

# while condition:
    # виконувати дії, поки condition є True

fruit = 'apple'
for char in fruit:
    print(char)
# Console:
# a
# p
# p
# l
# e

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")

some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)

# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1

# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")


k = 0
while k < 10:
    k = k + 1
print(k)

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break

a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)

for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} є парним числом.")
    else:
        print(f"{i} є непарним числом.")


for i in range(0, 10, 2):
    print(i)


some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

for number, letter in zip(list1, list2):
    print(number, letter)


numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)

for key in numbers.keys():
    print(key)

for val in numbers.values():
    print(val)

for key, value in numbers.items():
    print(key, value)

