import random

print("Введите число DELTA:")
try:
    count = 0
    delta = int(input())
    array = [0] * 10 
    for i in range(len(array)):
        array[i] = random.randint(0,99)
    print(array)
    minimum = min(array)

    for j in array:
        if j - minimum == delta:
            count+=1

    print("Общее число элементов в массиве, отличающихся от минимального на DELTA = " + str(count))
except ValueError:
    print("Введите ЦЕЛОЕ ЧИСЛО")
    quit()