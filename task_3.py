# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Напишите номер четверти от 1 до 4: "))

if number == 1:
    print("возможные координаты точек: X < 0, Y > 0.")

elif number == 2:
    print("возможные координаты точек: X > 0, Y > 0.")

elif number == 3:
    print("возможные координаты точек: X < 0, Y < 0.")

elif number == 4:
    print("возможные координаты точек: X < 0, Y > 0.")

else:
    print("Необходимо ввести число от 1 до 4.")
