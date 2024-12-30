numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for j in range(2, i):
        if i % j == 0:              # Если остаток от деления "0", значит число разделилось
            not_primes.append(i)
            break                   # Число 12, например, поделится и на 2, и на 3, и на 4, и на 6 (12 вернется 4 раза)
                                    # необходимо прервать цикл после первого успешного деления

for a in numbers:                   # если в условии выше использовать функцию else, то вернутся все числа т.к.
    if a not in not_primes:         # остаток от деления, когда делитель больше знаменателя - знаменатель, который не 0
        primes.append(a)


primes.remove(1)


print('primes:', primes)
print('not_primes:', not_primes)