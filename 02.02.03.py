print('Введите максимальный вес, который может выдержать 1 лодка')
m = int(input()) #лодка

print('Введите количество людей')
n = int(input()) #кол людей

summa = [] #список для подсчета общего веса всех людей
print('Введите вес каждого человека')
for i in range(n):
    a = int(input()) #вес каждого человека
    summa.append(a)
    
b = 0
for i in summa:
    b += i #подсчет общего веса

if b % m == 0:
    print('Минимальное количество лодок, необходимое для перевозки всех рыбаков на противоположный берег:', (b // m))
    
if b % m != 0:
    print('Минимальное количество лодок, необходимое для перевозки всех рыбаков на противоположный берег:', (b // m + 1))