int_number = 3
float_number = 3.3
complex_number = 3.3 + 2j

s1 = "Hello"
s2 = "world!"
joined_string = s1 + " " + s2

name = "Oleg"
hello_string = f"Hello, {name}!"

s1 = 'Hello'
s2 = 'world!'
joined_string = f"{s1} {s2}"  # Hello world!

x1 = 10
y1 = 10
x2 = 25
y2 = 25
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

pi = float('3.14')

pi_str = str(3.14)
age_str = str(29)

bool(0)  # False
bool(1)  # True

a = float(input("Введіть сторону квадрата a: "))
P = 4 * a
print(f"Периметр квадрата дорівнює {P}")

# Встановлюємо ціни на продукти
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")