import time

def is_prime(n):
    if n <= 1:
        return False
    if n <=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_first_n_primes(N):
    count = 0
    num = 2
    total = 0
    while count < N:
        if is_prime(num):
            total += num
            count += 1
        num += 1
    return total

def main():
    start_time = time.perf_counter()
    total = sum_first_n_primes(10000)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    # Guardar el resultado en output.txt
    with open('python/output.txt', 'w') as f:
        f.write(str(total))

    # Imprimir el tiempo de ejecución en milisegundos
    print(int(execution_time_ms))

if __name__ == "__main__":
    main()