import math

def quadratic_equation():
    print("The quadratic equation is of the form: ax^2 + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    print(f"\nThe equation you entered is: {a}x^2 + {b}x + {c} = 0")

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"\nThe equation has two real solutions: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"\nThe equation has one real solution: x = {x}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print(f"\nThe equation has complex solutions:")
        print(f"x1 = {real_part} + {imaginary_part}i")
        print(f"x2 = {real_part} - {imaginary_part}i")

if __name__ == "__main__":
    quadratic_equation()