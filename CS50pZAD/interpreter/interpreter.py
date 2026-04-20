stroka = input("Expression: ")

x, y, z = stroka.split(" ")

x = float(x)
z = float(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    result = None

if result is not None:
    print(f"{result:.1f}")
