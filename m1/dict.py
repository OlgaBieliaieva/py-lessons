my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

del my_dict["age"]
print(my_dict)
# {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}

print("name" in my_dict)
print("age" in my_dict)
# True
# False

my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

name = my_dict["name"]  # Поверне 'Alice'
gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику



