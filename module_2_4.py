numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                not_primes.append(i)
                break
            is_prime = True
        else:
            primes.append(i)
else:
    not_primes.append(i)

print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)

# я не поняла, как сделать и как работает пункт 4 из задания: Отметить простоту числа можно переменной is_prime,
# записав в нее значение True перед проверкой.
# Но я просто вписала после команд for, без понимания
# P.S. в принципе просидела очень долго над задачей, и часть интуитивно получилась, методом проб и ошибок