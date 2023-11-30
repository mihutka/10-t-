#t=0
#for x in range(15):
#    a = float(input("Sisesta A: "))
#    if a.is_integer():
#        t+=1
#print(t)

from random import random
from re import X
from tkinter.tix import INTEGER


summa=0
a = int(input("sisesta a: "))
for x in range(1, a+1, 1):
    summa+=x
print("summa: {0}".format(summa))



#a=0

#bsumma = 1
#while a < 8:
#    b = float(input("Введите число: "))
#    bsumma *=b
#    a+=1
#print("Произведение чисел: " + str(bsumma))    


# 4 Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
#for x in range (10, 21):
#    y = x**2
#    print(y)



#5 Составьте программу, которая вычисляет сумму только отрицательных из N чисел. Значение N вводится с клавиатуры.
#while True:
#    N = int(input("Введите число: "))
#    if N < 0:
#      summa = N + N
#      print("Сумма отрицательных чисел: " + str(summa))
#    else:
#     print("Ошибка, введите отрицательное число число")


#6.    С клавиатуры вводятся N чисел.

#Составьте программу, которая определяет количество отрицательных,

# количество положительных и количество нулей среди введенных чисел.  

#Значение N вводится с клавиатуры.

#minus = 0 
#plus = 0
#nuli = 0

#while True:
#    chislo = int(input("Введите число: "))
#    if chislo > 0:
#        plus +=1
#    elif chislo < 0:
#        minus +=1
#    elif chislo == 0:
#        nuli +=1
#    print("Вы ввели " + str(plus) + " положительное число")
#    print("Вы ввели " + str(minus) + " отрицательное число")
#    print("Вы ввели " + str(nuli) + " нулей")



#7 Вывести на экран числа, кратные К из промежутка [А,В].    

#A = int(input("Введите первое число промежутка: "))
#B = int(input("Введите второе число промежутка:  "))
#K = int(input("Введите число которое будет проверяться на кратность: "))

#for X in range(A, B + 1):
#    if X % K == 0 :

#     print("Это число " + str(X) + " являтся кратным числу " + str(K))




# 8.    Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =
# 2,5 см) для значений длин от 1 до 20 дюймов.

#for x in range (1,20):
#    s = x * 2.5
#    print( str(s) + " см")


#9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?

#while True:
#     euro = float(input("Введите количество евро: "))
#     let = float(input("Введите количество лет: "))
#     if let > 0:
#         summa_vklada = euro *(1 + 3 /100)**let
#         print("Сумма вклада через " + str(int(let)) + " лет,будет " + str(round(summa_vklada, 2)) + " евро")
#     elif let < 0 or euro < 0:
#         print("Ошибка!!!!")



# 10. Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.

#for X in range(10):
#   first = int(input("Первое число: "))
#   second = int(input("Второе число: "))
#   if first > second:
#       print(str(first) + " больше " + str(second))
#   elif second > first:
#       print(str(second) + " больше " + str(first))
#   else:
#       print("Они равны")


# Мини лоторея
#a = random
#print(a)















#15
#for y in range(10):

#    for X in range (10):
#       print(X, end=" ")
#    print()







#29
#for i in range(9):
#    for x in range(9):
#        if x==0 or i==x:
#            print("x", end=" ")
#        else:
#            print("0", end=" ")
#    print()


    









    







