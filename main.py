import random 

pos_el = 0 #счётчик положительных знач
neg_el = 0 #счётчик отрицательных знач
null_el = 0 #счётчик нулей
numbers = [random.randint(-50, 50) for i in range(25)] #список
print("Список: ", numbers)#вывод списка
for i in numbers: #высчитывание количества полож отриц и 0
    if i > 0:
        pos_el += 1
    elif i < 0:
        neg_el +=1
    else:
        null_el +=1
print(f"Положительных элементов: {pos_el}, {float(pos_el)/25*100:.0f}%") #вывод кол-ва положительных знач
print(f"Отрицательных элементов: {neg_el}, {float(neg_el)/25*100:.0f}%") #вывод кол-ва отрицательных знач
print(f"Нулевых элементов: {null_el}, {float(null_el)/25*100:.0f}%") #вывод кол-ва 0
print(f"Минимальное значение: {min(numbers)}", f"Максимальное значение: {max(numbers)}", sep="\n") #вывод max и min 