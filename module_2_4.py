numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = [] # Создаем пустой список primes.
not_primes = [] # Создаем пустой список not_primes.
for i in numbers: # Перебираем список numbers.
    if i == 1:  # Пропускаем значение 1.
        continue    # 
    prime_1 = True  # Создаем новую переменную и присваиваем ей значение True.
    for j in range(2, i): # Перебираем значения в диапазоне от 2 до значения i не включая i.
        if i %  j == 0: # Проверяем каждое значение в цикле на остаток от деления.
            prime_1 = False # Если остаток от деления равен нулю, то при нахождении в цикле первого
            break                # такого значения присваиваем переменной prime_1 значение False и выходим из цикла.
       
    if prime_1 == True: # Если остаток от деления не равен нулю, то присваиваем значение prime_1 True.
        primes.append(i)    # Добавляем это значение в список primes.
    else:
        not_primes.append(i) # Если иначе, то добавляем это значение в список not_prime

print(primes)   # Выводим список простых чисел на экран.
print(not_primes) # Выводим список не простых чисел на экран.
